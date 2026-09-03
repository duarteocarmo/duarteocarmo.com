title: API documentation
slug: developers
description: Public API and agent integration documentation for duarteocarmo.com.

The API provides public information from this website. It is read only. Most endpoints return JSON; About and Consulting return Markdown.

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

Fetch the About page as Markdown:

```bash
curl -H "Accept: text/markdown" "https://duarteocarmo.com/api/about"
```

A successful list response contains `data` and `pagination`. Pass the returned `nextCursor` as the `cursor` parameter to fetch the next page.

## Endpoints

| Method | Path | Description |
| --- | --- | --- |
| GET | `/api` | API version and access details |
| GET | `/api/about` | About page as Markdown |
| GET | `/api/consulting` | Consulting page as Markdown |
| GET | `/api/contact` | Public contact details |
| GET | `/api/posts` | Posts with search and cursor pagination |

The [OpenAPI specification](/openapi.json) defines every parameter and response schema.

About and Consulting return a Markdown string with `Content-Type: text/markdown`. Contact returns JSON contact details. Contact is read-only and does not submit messages or create bookings.

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
