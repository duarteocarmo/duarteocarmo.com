import { afterAll, beforeAll, describe, expect, test } from "bun:test";
import { mkdir, mkdtemp, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createServer } from "./server.js";

const content = {
  contact: { email: "me@example.com" },
  posts: [
    {
      slug: "first",
      title: "First post",
      description: "hello",
      url: "https://example.com/blog/first",
      published: "2025-01-01",
    },
    {
      slug: "second",
      title: "Second post",
      description: "hello",
      url: "https://example.com/blog/second",
    },
  ],
  pages: [{ slug: "about", markdown: "# About" }],
};

let root;
let outside;
let server;
const request = (path, options) =>
  fetch(new URL(path, server.url), { redirect: "manual", ...options });
const json = (path, options) =>
  request(path, options).then((response) => response.json());

beforeAll(async () => {
  root = await mkdtemp(join(tmpdir(), "bun-coolify-"));
  await mkdir(join(root, "api/data"), { recursive: true });
  await mkdir(join(root, "nested"), { recursive: true });
  await Promise.all([
    writeFile(join(root, "index.html"), "<h1>Home</h1>"),
    writeFile(join(root, "about.html"), "<h1>About</h1>"),
    writeFile(join(root, "404.html"), "<h1>Not found</h1>"),
    writeFile(join(root, "style.css"), "body { color: red }"),
    writeFile(join(root, "notes.txt"), "notes"),
    writeFile(join(root, "llms.txt"), "# LLMs\n"),
    writeFile(join(root, "api/data/content.json"), JSON.stringify(content)),
    writeFile(join(root, "nested/index.html"), "<h1>Nested</h1>"),
  ]);
  outside = await mkdtemp(join(tmpdir(), "bun-coolify-outside-"));
  await writeFile(join(outside, "secret.txt"), "private");
  await symlink(outside, join(root, "outside"));
  server = createServer({ root, port: 0, hostname: "127.0.0.1" });
});

afterAll(async () => {
  server.stop();
  await rm(root, { recursive: true, force: true });
  await rm(outside, { recursive: true, force: true });
});

describe("static files", () => {
  test("serves HTML and markdown negotiation with cache headers", async () => {
    const html = await request("/");
    expect(html.status).toBe(200);
    expect(await html.text()).toContain("Home");
    expect(html.headers.get("Vary")).toContain("Accept");
    expect(html.headers.get("Cache-Control")).toBe("no-store");

    const markdown = await request("/", {
      headers: { Accept: "text/markdown" },
    });
    expect(markdown.status).toBe(200);
    expect(await markdown.text()).toContain("# LLMs");
    expect(markdown.headers.get("Content-Type")).toContain("text/markdown");
  });

  test("supports HEAD, MIME types, redirects, and nested indexes", async () => {
    const head = await request("/style.css", { method: "HEAD" });
    expect(head.status).toBe(200);
    expect(await head.text()).toBe("");
    expect(head.headers.get("Content-Type")).toContain("text/css");

    expect((await request("/about.html?x=1")).status).toBe(308);
    expect((await request("/about.html?x=1")).headers.get("Location")).toBe(
      "/about?x=1",
    );
    expect((await request("/about/")).headers.get("Location")).toBe("/about");
    expect(await (await request("/nested/")).text()).toContain("Nested");
  });

  test("protects the root and uses the custom 404 page", async () => {
    const missing = await request("/missing");
    expect(missing.status).toBe(404);
    expect(await missing.text()).toContain("Not found");
    expect((await request("/%2e%2e/%2e%2e/etc/passwd")).status).toBe(404);
    expect((await request("/..%2foutside.txt")).status).toBe(400);
    expect((await request("/%00")).status).toBe(400);
    expect((await request("/%ZZ")).status).toBe(400);
    expect((await request("/outside/secret.txt")).status).toBe(404);
    const api = await request("/api/unknown");
    expect(api.status).toBe(404);
    expect(api.headers.get("Content-Type")).toContain("application/json");
  });
});

describe("API", () => {
  test("serves index, filtered posts, pages, and contact", async () => {
    expect((await json("/api")).data.readOnly).toBe(true);
    expect((await json("/api/posts?q=first&limit=1")).data[0].id).toBe("first");
    expect(await (await request("/api/about")).text()).toBe("# About");
    expect((await json("/api/contact")).data.email).toBe("me@example.com");
  });

  test("paginates and rejects invalid parameters", async () => {
    const first = await json("/api/posts?limit=1");
    const second = await json(
      `/api/posts?limit=1&cursor=${encodeURIComponent(first.pagination.nextCursor)}`,
    );
    expect(second.data[0].id).toBe("second");
    expect(second.pagination.nextCursor).toBeNull();
    expect((await request("/api/posts?limit=0")).status).toBe(400);
    expect((await request("/api/posts?cursor=!invalid")).status).toBe(400);
  });

  test("handles API methods and OPTIONS", async () => {
    expect((await request("/api/posts", { method: "OPTIONS" })).status).toBe(
      204,
    );
    expect((await request("/api/posts", { method: "POST" })).status).toBe(405);
  });
});

describe("MCP", () => {
  const call = (method, params = {}, id = 1) =>
    json("/mcp", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ jsonrpc: "2.0", id, method, params }),
    });

  test("serves the discovery alias and rejects malformed requests", async () => {
    const response = await request("/.well-known/mcp", {
      method: "POST",
      body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "initialize" }),
    });
    expect((await response.json()).result.serverInfo.name).toBe(
      "duarteocarmo-content",
    );
    expect(response.headers.get("Cache-Control")).toBe("no-store");
    expect(
      (await json("/mcp", { method: "POST", body: "null" })).error.code,
    ).toBe(-32600);
    expect((await json("/mcp", { method: "POST", body: "{" })).error.code).toBe(
      -32700,
    );
  });

  test("supports discovery and tools", async () => {
    expect((await request("/.well-known/mcp")).status).toBe(405);
    expect((await request("/mcp", { method: "OPTIONS" })).status).toBe(204);
    expect((await call("initialize")).result.serverInfo.name).toBe(
      "duarteocarmo-content",
    );
    expect((await call("tools/list")).result.tools.length).toBeGreaterThan(0);
    const posts = await call("tools/call", {
      name: "search_posts",
      arguments: { query: "first", limit: 1 },
    });
    expect(JSON.parse(posts.result.content[0].text).data[0].id).toBe("first");
    const page = await call("tools/call", {
      name: "get_page",
      arguments: { page: "about" },
    });
    expect(JSON.parse(page.result.content[0].text).markdown).toBe("# About");
    const contact = await call("tools/call", {
      name: "get_contact_info",
      arguments: { reason: "general" },
    });
    expect(JSON.parse(contact.result.content[0].text).data.email).toBe(
      "me@example.com",
    );
  });
});
