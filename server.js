import { realpath } from "node:fs/promises";
import { resolve, sep } from "node:path";
import { handleApiRequest } from "./functions/_lib/api.js";
import { handleMcpRequest } from "./functions/mcp.js";

export function createServer({ root, port = 1111, hostname = "0.0.0.0" }) {
  const contentPath = resolve(root, "api/data/content.json");
  const rootPath = realpath(root);

  async function findFile({ path }) {
    const directory = await rootPath;
    try {
      const filename = await realpath(resolve(directory, `.${path}`));
      if (!filename.startsWith(`${directory}${sep}`)) return null;
      const file = Bun.file(filename);
      return (await file.stat()).isFile() ? file : null;
    } catch (error) {
      if (["ENOENT", "ENOTDIR"].includes(error.code)) return null;
      throw error;
    }
  }

  return Bun.serve({
    port,
    hostname,
    async fetch(request) {
      const url = new URL(request.url);
      let path;
      try {
        path = decodeURIComponent(url.pathname);
      } catch {
        return new Response("Bad request", { status: 400 });
      }
      if (
        path.includes("\0") ||
        path.includes("\\") ||
        path.split("/").includes("..")
      ) {
        return new Response("Bad request", { status: 400 });
      }

      if (path === "/mcp" || path === "/.well-known/mcp") {
        return handleMcpRequest({ request, contentPath });
      }
      if (path === "/api" || path.startsWith("/api/")) {
        if (!path.startsWith("/api/data/")) {
          return handleApiRequest({
            request,
            contentPath,
            resource: path.replace(/^\/api\/?/, "") || "index",
          });
        }
      }
      if (!["GET", "HEAD"].includes(request.method)) {
        return new Response("Method not allowed", {
          status: 405,
          headers: { Allow: "GET, HEAD" },
        });
      }

      function redirect({ pathname }) {
        // Keep redirects relative, even for paths beginning with two slashes.
        return new Response(null, {
          status: 308,
          headers: {
            Location: `/${pathname.replace(/^\/+/, "")}${url.search}`,
          },
        });
      }

      if (path === "/index.html") return redirect({ pathname: "/" });
      if (path.endsWith(".html")) {
        return redirect({ pathname: url.pathname.slice(0, -5) });
      }
      if (path !== "/" && path.endsWith("/")) {
        const page = await findFile({ path: `${path.slice(0, -1)}.html` });
        if (page) return redirect({ pathname: url.pathname.slice(0, -1) });
      }

      const headers = { "Cache-Control": "public, max-age=300" };
      let file;
      if (path === "/") {
        const markdown = request.headers
          .get("Accept")
          ?.toLowerCase()
          .includes("text/markdown");
        file = await findFile({ path: markdown ? "/llms.txt" : "/index.html" });
        headers.Vary = "Accept";
        // Cloudflare's default cache key does not distinguish Accept headers.
        headers["Cache-Control"] = "no-store";
        if (markdown) headers["Content-Type"] = "text/markdown; charset=utf-8";
      } else {
        file =
          (await findFile({ path: `${path}.html` })) ||
          (await findFile({ path })) ||
          (await findFile({ path: `${path.replace(/\/$/, "")}/index.html` }));
      }

      const status = file ? 200 : 404;
      if (!file) {
        file = await findFile({ path: "/404.html" });
        headers["Cache-Control"] = "no-store";
        headers["Content-Type"] = "text/html; charset=utf-8";
      }
      headers["Content-Type"] ??= file?.type || "text/plain; charset=utf-8";
      return new Response(
        request.method === "HEAD" ? null : file || "Not found",
        { status, headers },
      );
    },
    error(error) {
      console.error(error);
      return new Response("Internal server error", {
        status: 500,
        headers: { "Cache-Control": "no-store" },
      });
    },
  });
}

if (import.meta.main) {
  const server = createServer({
    root: process.env.STATIC_DIR || "output",
    port: Number(process.env.PORT || 1111),
  });
  console.log(`Serving website on ${server.url}`);
}
