title: API documentation
slug: developers
description: Public API and agent integration documentation for duarteocarmo.com.

The API provides profile information and an index of the public writing on this website. It is read only and returns JSON.

- Base URL: `https://duarteocarmo.com`
- OpenAPI specification: [`/openapi.json`](/openapi.json)
- MCP endpoint: `https://duarteocarmo.com/mcp`

## Quickstart

Fetch the latest posts with curl:

```bash
curl "https://duarteocarmo.com/api/posts?limit=5"
```

Search for posts about MCP:

```bash
curl "https://duarteocarmo.com/api/posts?q=mcp&limit=5"
```

A successful list response contains `data` and `pagination`. Pass the returned `nextCursor` as the `cursor` parameter to fetch the next page.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api` | API version and access details |
| GET | `/api/profile` | Public profile |
| GET | `/api/posts` | Posts with search and cursor pagination |
| GET | `/api/pages` | Public website pages |

The [OpenAPI specification](/openapi.json) defines every parameter and response schema.

## Authentication and API keys

No API key or account is required. All endpoints expose information that is already public on the website, and no endpoint can change data.

The API has no application rate limit. Cloudflare may still limit abusive traffic. Clients should cache responses and retry temporary errors with backoff.

## Errors

API errors use one JSON shape:

```json
{
  "error": {
    "code": "INVALID_LIMIT",
    "message": "limit must be an integer between 1 and 100",
    "hint": "Remove limit to use the default value of 20."
  }
}
```

## Sandbox

`GET /api/sandbox/posts` returns fixed sample records with the same response shape as the posts endpoint. Use it to test parsing and pagination without depending on live site content.
