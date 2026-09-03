import { handleApiRequest } from "../_lib/api.js";

export function onRequest(context) {
  return handleApiRequest({ context, resource: "posts" });
}
