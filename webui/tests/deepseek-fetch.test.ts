import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { createDeepSeekRequestFetch } from "../src/lib/deepseek-fetch";

describe("createDeepSeekRequestFetch", () => {
  beforeEach(() => {
    delete process.env.DEEPSEEK_THINKING;
  });

  afterEach(() => {
    delete process.env.DEEPSEEK_THINKING;
  });

  it("merges thinking disabled into chat/completions JSON POST body", async () => {
    const base = vi.fn(async (_input: RequestInfo | URL, init?: RequestInit) => {
      expect(typeof init?.body).toBe("string");
      const parsed = JSON.parse(init!.body as string);
      expect(parsed.thinking).toEqual({ type: "disabled" });
      return new Response("ok");
    });
    const wrapped = createDeepSeekRequestFetch(base as typeof fetch);
    await wrapped("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      body: JSON.stringify({ model: "x", messages: [] }),
    });
    expect(base).toHaveBeenCalledTimes(1);
  });

  it("does not override existing thinking", async () => {
    const base = vi.fn(async (_input: RequestInfo | URL, init?: RequestInit) => {
      const parsed = JSON.parse(init!.body as string);
      expect(parsed.thinking).toEqual({ type: "enabled" });
      return new Response("ok");
    });
    const wrapped = createDeepSeekRequestFetch(base as typeof fetch);
    await wrapped("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      body: JSON.stringify({ model: "x", messages: [], thinking: { type: "enabled" } }),
    });
    expect(base).toHaveBeenCalledTimes(1);
  });

  it("skips merge when DEEPSEEK_THINKING=enabled", async () => {
    process.env.DEEPSEEK_THINKING = "enabled";
    const base = vi.fn(async (_input: RequestInfo | URL, init?: RequestInit) => {
      const parsed = JSON.parse(init!.body as string);
      expect(parsed.thinking).toBeUndefined();
      return new Response("ok");
    });
    const wrapped = createDeepSeekRequestFetch(base as typeof fetch);
    await wrapped("https://api.deepseek.com/v1/chat/completions", {
      method: "POST",
      body: JSON.stringify({ model: "x", messages: [] }),
    });
    expect(base).toHaveBeenCalledTimes(1);
  });

  it("ignores non-chat/completions URLs", async () => {
    const base = vi.fn(async () => new Response("ok"));
    const wrapped = createDeepSeekRequestFetch(base as typeof fetch);
    await wrapped("https://example.com/other", {
      method: "POST",
      body: JSON.stringify({ foo: 1 }),
    });
    expect(base).toHaveBeenCalledTimes(1);
    const init = base.mock.calls[0][1] as RequestInit;
    expect(JSON.parse(init.body as string).thinking).toBeUndefined();
  });
});
