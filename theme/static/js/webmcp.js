(() => {
  const modelContext = document.modelContext || navigator.modelContext;
  if (!modelContext || typeof modelContext.registerTool !== "function") return;

  const register = (tool) => {
    try {
      Promise.resolve(modelContext.registerTool(tool)).catch(() => {});
    } catch {}
  };
  const readJson = (response) => {
    if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
    return response.json();
  };

  register({
    name: "search_posts",
    description: "Search Duarte O.Carmo's public blog posts by title, description, or tag.",
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
        .then(readJson)
        .then((body) => JSON.stringify(body));
    },
  });

  register({
    name: "get_profile",
    description: "Get Duarte O.Carmo's public profile and areas of work.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true },
    execute: (_input, options) =>
      fetch("/api/profile", { signal: options && options.signal })
        .then(readJson)
        .then((body) => JSON.stringify(body)),
  });

  register({
    name: "list_pages",
    description: "List the public pages on duarteocarmo.com.",
    inputSchema: { type: "object", properties: {}, additionalProperties: false },
    annotations: { readOnlyHint: true },
    execute: (_input, options) =>
      fetch("/api/pages", { signal: options && options.signal })
        .then(readJson)
        .then((body) => JSON.stringify(body)),
  });
})();
