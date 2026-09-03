import { handleApiRequest } from "./_lib/api.js";

const MCP_HEADERS = {
  "Access-Control-Allow-Headers": "Content-Type, MCP-Protocol-Version",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Origin": "*",
  "Content-Type": "application/json; charset=utf-8",
};

const SUPPORTED_PROTOCOL_VERSIONS = ["2025-06-18", "2025-03-26", "2024-11-05"];

const TOOLS = [
  {
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
    annotations: { readOnlyHint: true, destructiveHint: false },
  },
  {
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
    annotations: { readOnlyHint: true, destructiveHint: false },
  },
  {
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
    annotations: { readOnlyHint: true, destructiveHint: false },
  },
];

function rpcResponse({ id, result, error, status = 200 }) {
  const body = { jsonrpc: "2.0", id: id ?? null };
  if (error) body.error = error;
  else body.result = result;
  return new Response(JSON.stringify(body), { status, headers: MCP_HEADERS });
}

function rpcError({ id, code, message, status = 200 }) {
  return rpcResponse({ id, status, error: { code, message } });
}

async function callApi({ context, resource, query = "", markdown = false }) {
  const url = new URL(`/api/${resource}${query}`, context.request.url);
  const response = await handleApiRequest({
    context: { ...context, request: new Request(url) },
    resource,
  });
  if (!response.ok) throw new Error(`API returned HTTP ${response.status}`);
  return markdown ? response.text() : response.json();
}

async function callTool({ context, name, args }) {
  if (name === "search_posts") {
    if (!args || typeof args.query !== "string" || !args.query.trim()) {
      throw new TypeError("search_posts requires a non-empty query string");
    }
    const limit = Math.min(Math.max(Number(args.limit) || 5, 1), 20);
    const query = `?q=${encodeURIComponent(args.query)}&limit=${limit}`;
    return callApi({ context, resource: "posts", query });
  }
  if (name === "get_page") {
    if (!args || !["about", "consulting"].includes(args.page)) {
      throw new TypeError("get_page requires page to be about or consulting");
    }
    const markdown = await callApi({
      context,
      resource: args.page,
      markdown: true,
    });
    return { page: args.page, markdown };
  }
  if (name === "get_contact_info") {
    if (!args || !["general", "consulting"].includes(args.reason)) {
      throw new TypeError(
        "get_contact_info requires reason to be general or consulting",
      );
    }
    const contact = await callApi({ context, resource: "contact" });
    if (args.reason === "consulting") return contact;
    return { data: { email: contact.data.email } };
  }
  throw new TypeError(`Unknown tool: ${name}`);
}

export async function onRequest(context) {
  if (context.request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: MCP_HEADERS });
  }
  if (context.request.method !== "POST") {
    return rpcError({
      id: null,
      status: 405,
      code: -32600,
      message: "Use POST for MCP requests.",
    });
  }

  let request;
  try {
    request = await context.request.json();
  } catch {
    return rpcError({ id: null, code: -32700, message: "Invalid JSON." });
  }
  if (request.jsonrpc !== "2.0" || typeof request.method !== "string") {
    return rpcError({
      id: request.id,
      code: -32600,
      message: "Invalid JSON-RPC request.",
    });
  }
  if (request.method === "notifications/initialized") {
    return new Response(null, { status: 202, headers: MCP_HEADERS });
  }
  if (request.method === "initialize") {
    const requestedVersion = request.params && request.params.protocolVersion;
    const protocolVersion = SUPPORTED_PROTOCOL_VERSIONS.includes(
      requestedVersion,
    )
      ? requestedVersion
      : SUPPORTED_PROTOCOL_VERSIONS[0];
    return rpcResponse({
      id: request.id,
      result: {
        protocolVersion,
        capabilities: { tools: { listChanged: false } },
        serverInfo: { name: "duarteocarmo-content", version: "1.0.0" },
        instructions:
          "Use these read-only tools to search posts, read key pages, and find public contact details.",
      },
    });
  }
  if (request.method === "ping")
    return rpcResponse({ id: request.id, result: {} });
  if (request.method === "tools/list") {
    return rpcResponse({ id: request.id, result: { tools: TOOLS } });
  }
  if (request.method === "tools/call") {
    try {
      const output = await callTool({
        context,
        name: request.params && request.params.name,
        args: (request.params && request.params.arguments) || {},
      });
      return rpcResponse({
        id: request.id,
        result: {
          content: [{ type: "text", text: JSON.stringify(output) }],
          structuredContent: output,
          isError: false,
        },
      });
    } catch (error) {
      return rpcError({ id: request.id, code: -32602, message: error.message });
    }
  }
  return rpcError({
    id: request.id,
    code: -32601,
    message: "Method not found.",
  });
}
