(() => {
  const modelContext = document.modelContext || navigator.modelContext;
  if (!modelContext || typeof modelContext.registerTool !== "function") return;

  const register = (tool) => {
    try {
      Promise.resolve(modelContext.registerTool(tool)).catch(() => {});
    } catch {}
  };
  const readResponse = (response, markdown = false) => {
    if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
    return markdown ? response.text() : response.json();
  };

  register({
    name: "search_posts",
    description:
      "Search Duarte O.Carmo's public blog posts by title or description.",
    inputSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Words to search for." },
        limit: { type: "integer", minimum: 1, maximum: 20, default: 5 },
      },
      required: ["query"],
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: (input = {}, options) => {
      if (typeof input.query !== "string" || !input.query.trim()) {
        throw new TypeError("search_posts requires a non-empty query string");
      }
      const limit = Math.min(Math.max(Number(input.limit) || 5, 1), 20);
      const url = `/api/posts?q=${encodeURIComponent(input.query)}&limit=${limit}`;
      return fetch(url, { signal: options && options.signal })
        .then((response) => readResponse(response))
        .then((body) => JSON.stringify(body));
    },
  });

  register({
    name: "get_page",
    description: "Read Duarte O.Carmo's About or Consulting page as Markdown.",
    inputSchema: {
      type: "object",
      properties: {
        page: {
          type: "string",
          enum: ["about", "consulting"],
          description: "The page to read.",
        },
      },
      required: ["page"],
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: (input = {}, options) => {
      if (!["about", "consulting"].includes(input.page)) {
        throw new TypeError("get_page requires page to be about or consulting");
      }
      return fetch(`/api/${input.page}`, {
        signal: options && options.signal,
      }).then((response) => readResponse(response, true));
    },
  });

  register({
    name: "get_contact_info",
    description:
      "Get Duarte O.Carmo's public contact details for a general or consulting inquiry.",
    inputSchema: {
      type: "object",
      properties: {
        reason: {
          type: "string",
          enum: ["general", "consulting"],
          description: "The reason for making contact.",
        },
      },
      required: ["reason"],
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: (input = {}, options) => {
      if (!["general", "consulting"].includes(input.reason)) {
        throw new TypeError(
          "get_contact_info requires reason to be general or consulting",
        );
      }
      return fetch("/api/contact", { signal: options && options.signal })
        .then((response) => readResponse(response))
        .then((body) => {
          const data =
            input.reason === "consulting"
              ? body.data
              : { email: body.data.email };
          return JSON.stringify({ data });
        });
    },
  });
})();
