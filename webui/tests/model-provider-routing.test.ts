import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";

const chatMock = vi.fn((modelId: string) => ({ provider: "chat", modelId }));
const defaultModelMock = vi.fn((modelId: string) => ({ provider: "responses", modelId }));

const createOpenAIMock = vi.fn(() => {
  const fn = Object.assign(defaultModelMock, { chat: chatMock });
  return fn;
});

vi.mock("@ai-sdk/openai", () => ({
  createOpenAI: (...args: unknown[]) => createOpenAIMock(...args),
}));

vi.mock("@ai-sdk/anthropic", () => ({
  anthropic: vi.fn((modelId: string) => ({ provider: "anthropic", modelId })),
}));

describe("getModel provider routing", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    delete process.env.SIGMA_PROVIDER;
    delete process.env.SIGMA_MODEL;
    delete process.env.DEEPSEEK_API_KEY;
    delete process.env.OPENAI_API_KEY;
    delete process.env.OPENROUTER_API_KEY;
    delete process.env.CUSTOM_BASE_URL;
    delete process.env.CUSTOM_API_KEY;
    delete process.env.DEEPSEEK_THINKING;
  });

  afterEach(() => {
    vi.resetModules();
  });

  it("deepseek uses Chat Completions (.chat), not Responses API", async () => {
    process.env.SIGMA_PROVIDER = "deepseek";
    process.env.DEEPSEEK_API_KEY = "test-key";
    process.env.SIGMA_MODEL = "deepseek-v4-flash";
    vi.resetModules();
    const { getModel } = await import("../src/lib/model");
    const m = getModel();
    expect(m).toEqual({ provider: "chat", modelId: "deepseek-v4-flash" });
    expect(chatMock).toHaveBeenCalledWith("deepseek-v4-flash");
    expect(defaultModelMock).not.toHaveBeenCalled();
    expect(createOpenAIMock).toHaveBeenCalledWith(
      expect.objectContaining({
        baseURL: "https://api.deepseek.com/v1",
        name: "deepseek",
        fetch: expect.any(Function),
      }),
    );
  });

  it("openrouter uses .chat", async () => {
    process.env.SIGMA_PROVIDER = "openrouter";
    process.env.OPENROUTER_API_KEY = "or-key";
    vi.resetModules();
    const { getModel } = await import("../src/lib/model");
    getModel();
    expect(chatMock).toHaveBeenCalled();
    expect(defaultModelMock).not.toHaveBeenCalled();
  });

  it("openai uses default provider entrypoint (Responses)", async () => {
    process.env.SIGMA_PROVIDER = "openai";
    process.env.OPENAI_API_KEY = "sk-test";
    vi.resetModules();
    const { getModel } = await import("../src/lib/model");
    getModel();
    expect(defaultModelMock).toHaveBeenCalledWith("gpt-4o");
    expect(chatMock).not.toHaveBeenCalled();
  });

  it("anthropic path uses anthropic()", async () => {
    process.env.SIGMA_PROVIDER = "anthropic";
    process.env.SIGMA_MODEL = "claude-test";
    vi.resetModules();
    const { getModel } = await import("../src/lib/model");
    const { anthropic } = await import("@ai-sdk/anthropic");
    const m = getModel();
    expect(m).toEqual({ provider: "anthropic", modelId: "claude-test" });
    expect(anthropic).toHaveBeenCalledWith("claude-test");
    expect(createOpenAIMock).not.toHaveBeenCalled();
  });
});
