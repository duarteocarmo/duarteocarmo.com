title: API documentation
slug: developers
description: Public API and agent integration documentation for duarteocarmo.com.

The API provides public information from this website. It is read only. Most endpoints return JSON; About and Consulting return Markdown. Every page and blog post also has a Markdown version advertised through an HTML `rel="alternate"` link.

- Base URL: `https://duarteocarmo.com`
- LLM-readable index: [`/llms.txt`](/llms.txt)
- Full key pages: [`/llms-full.txt`](/llms-full.txt)
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
curl "https://duarteocarmo.com/about.html.md"
```

`llms.txt` is a concise index of pages and posts. `llms-full.txt` contains the complete About, Consulting, and API documentation pages. Blog post bodies are available through their individual Markdown URLs but are not included in `llms-full.txt`.

For any page or post, inspect its HTML for the exact Markdown URL:

```html
<link rel="alternate" type="text/markdown" href="https://duarteocarmo.com/about.html.md">
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
