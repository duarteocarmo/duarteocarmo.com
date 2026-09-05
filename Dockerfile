# syntax=docker/dockerfile:1.7

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PYTHONUNBUFFERED=1

WORKDIR /app

ARG PHOTO_BUCKET_URL
ARG PHOTO_BUCKET_PUBLIC_URL
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG PHOTO_BUCKET_NAME

ENV PHOTO_BUCKET_URL=$PHOTO_BUCKET_URL \
    PHOTO_BUCKET_PUBLIC_URL=$PHOTO_BUCKET_PUBLIC_URL \
    AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
    AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
    PHOTO_BUCKET_NAME=$PHOTO_BUCKET_NAME

COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev --no-install-project

COPY . .
RUN --mount=type=cache,target=/root/.cache/uv \
    uv run --no-sync pelican -s publishconf.py -t theme -o output

FROM oven/bun:1.3.14-alpine

WORKDIR /app
ENV NODE_ENV=production \
    PORT=1111 \
    STATIC_DIR=/app/output

COPY --from=builder --chown=bun:bun /app/output ./output
COPY --chown=bun:bun server.js ./server.js
COPY --chown=bun:bun functions ./functions

USER bun
EXPOSE 1111
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD bun -e 'const response = await fetch("http://127.0.0.1:" + process.env.PORT + "/api"); process.exit(response.ok ? 0 : 1)'
CMD ["bun", "run", "server.js"]
