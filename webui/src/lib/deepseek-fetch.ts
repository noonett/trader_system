type FetchLike = typeof fetch;

/**
 * DeepSeek Chat Completions default to thinking mode. With tools, follow-up
 * requests must echo `reasoning_content` on assistant turns; `@ai-sdk/openai`
 * drops that field when mapping messages. Injecting `thinking.type=disabled`
 * avoids the 400 without changing message conversion.
 *
 * - Default: add `thinking: { type: "disabled" }` to JSON POST bodies for
 *   `/chat/completions` when the body does not already set `thinking`.
 * - Set `DEEPSEEK_THINKING=enabled` to omit this (API default thinking on;
 *   multi-turn tools may error until the SDK preserves `reasoning_content`).
 */
export function createDeepSeekRequestFetch(baseFetch: FetchLike = globalThis.fetch.bind(globalThis)): FetchLike {
  return async (input, init) => {
    const method = (init?.method ?? "GET").toUpperCase();
    if (method !== "POST" || !init?.body || typeof init.body !== "string") {
      return baseFetch(input, init);
    }

    const urlStr =
      typeof input === "string" ? input : input instanceof URL ? input.href : (input as Request).url;
    if (!urlStr.includes("chat/completions")) {
      return baseFetch(input, init);
    }

    if (process.env.DEEPSEEK_THINKING === "enabled") {
      return baseFetch(input, init);
    }

    try {
      const body = JSON.parse(init.body) as Record<string, unknown>;
      if (body == null || typeof body !== "object" || Array.isArray(body)) {
        return baseFetch(input, init);
      }
      if ("thinking" in body && body.thinking != null) {
        return baseFetch(input, init);
      }
      body.thinking = { type: "disabled" };
      return baseFetch(input, { ...init, body: JSON.stringify(body) });
    } catch {
      return baseFetch(input, init);
    }
  };
}
