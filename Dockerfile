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

FROM nginxinc/nginx-unprivileged:1.27-alpine

COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/output /usr/share/nginx/html

EXPOSE 1111
