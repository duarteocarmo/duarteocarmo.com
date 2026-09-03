const API_HEADERS = {
  "Access-Control-Allow-Headers": "Content-Type",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Origin": "*",
  "Cache-Control": "public, max-age=300",
  "Content-Type": "application/json; charset=utf-8",
};

function jsonResponse({ body, status = 200, headers = {} }) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...API_HEADERS, ...headers },
  });
}

function markdownResponse({ body }) {
  return new Response(body, {
    headers: { ...API_HEADERS, "Content-Type": "text/markdown; charset=utf-8" },
  });
}

function errorResponse({ status, code, message, hint }) {
  return jsonResponse({
    status,
    body: { error: { code, message, hint } },
  });
}

async function readContent({ context }) {
  const assetUrl = new URL("/api/data/content.json", context.request.url);
  const response = await context.env.ASSETS.fetch(assetUrl);
  if (!response.ok) {
    throw new Error(`Content data returned HTTP ${response.status}`);
  }
  return response.json();
}

function decodeCursor({ cursor }) {
  if (!cursor) return 0;
  const offset = Number.parseInt(atob(cursor), 10);
  if (!Number.isInteger(offset) || offset < 0)
    throw new Error("Invalid cursor");
  return offset;
}

function serializePost({ post }) {
  return {
    id: post.slug,
    title: post.title,
    url: post.url,
    publishedAt: post.published || null,
    summary: post.description,
  };
}

function listPosts({ posts, url }) {
  const query = (url.searchParams.get("q") || "").trim().toLowerCase();
  const requestedLimit = Number.parseInt(
    url.searchParams.get("limit") || "20",
    10,
  );
  if (
    !Number.isInteger(requestedLimit) ||
    requestedLimit < 1 ||
    requestedLimit > 100
  ) {
    return errorResponse({
      status: 400,
      code: "INVALID_LIMIT",
      message: "limit must be an integer between 1 and 100",
      hint: "Remove limit to use the default value of 20.",
    });
  }

  let offset;
  try {
    offset = decodeCursor({ cursor: url.searchParams.get("cursor") });
  } catch {
    return errorResponse({
      status: 400,
      code: "INVALID_CURSOR",
      message: "cursor is not valid",
      hint: "Use the nextCursor value from the previous response.",
    });
  }

  const matches = query
    ? posts.filter((post) =>
        [post.title, post.description].join(" ").toLowerCase().includes(query),
      )
    : posts;
  const data = matches
    .slice(offset, offset + requestedLimit)
    .map((post) => serializePost({ post }));
  const nextOffset = offset + data.length;
  const nextCursor =
    nextOffset < matches.length ? btoa(String(nextOffset)) : null;
  return jsonResponse({ body: { data, pagination: { nextCursor } } });
}

export async function handleApiRequest({ context, resource }) {
  if (context.request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: API_HEADERS });
  }
  if (context.request.method !== "GET") {
    return errorResponse({
      status: 405,
      code: "METHOD_NOT_ALLOWED",
      message: "This API is read-only and accepts GET requests.",
      hint: "Retry the same URL with GET.",
    });
  }

  try {
    if (resource === "index") {
      return jsonResponse({
        body: {
          data: {
            name: "Duarte O.Carmo public API",
            version: "1",
            readOnly: true,
            authentication: "none",
          },
        },
      });
    }

    const content = await readContent({ context });
    if (["about", "consulting"].includes(resource)) {
      const page = content.pages.find((item) => item.slug === resource);
      if (!page) throw new Error(`Page not found: ${resource}`);
      return markdownResponse({ body: page.markdown });
    }
    if (resource === "contact") {
      return jsonResponse({ body: { data: content.contact } });
    }
    if (resource === "posts") {
      return listPosts({
        posts: content.posts,
        url: new URL(context.request.url),
      });
    }
    return errorResponse({
      status: 404,
      code: "NOT_FOUND",
      message: "The requested API resource does not exist.",
      hint: "See /openapi.json for the available endpoints.",
    });
  } catch (error) {
    return errorResponse({
      status: 500,
      code: "CONTENT_UNAVAILABLE",
      message: "The website content could not be loaded.",
      hint: "Retry the request later.",
    });
  }
}
