export async function onRequest(context) {
  const acceptsMarkdown = context.request.headers
    .get("Accept")
    ?.toLowerCase()
    .includes("text/markdown");

  const response = acceptsMarkdown
    ? await context.env.ASSETS.fetch(new URL("/llms.txt", context.request.url))
    : await context.next();
  const headers = new Headers(response.headers);
  const vary = headers.get("Vary");

  headers.set("Vary", vary ? `${vary}, Accept` : "Accept");
  if (acceptsMarkdown)
    headers.set("Content-Type", "text/markdown; charset=utf-8");

  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}
