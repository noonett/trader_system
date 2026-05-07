import { describe, it, expect, vi, beforeEach } from "vitest";

const { streamTextMock, toUIMessageStreamResponse } = vi.hoisted(() => {
  const toUIMessageStreamResponse = vi.fn(() => new Response("mock-ui-stream", { status: 200 }));
  const streamTextMock = vi.fn(() => ({
    toUIMessageStreamResponse,
  }));
  return { streamTextMock, toUIMessageStreamResponse };
});

vi.mock("@/lib/model", () => ({
  getModel: vi.fn(() => "mock-language-model"),
}));

vi.mock("@/lib/tools", () => {
  const { z } = require("zod");
  return {
    createTools: vi.fn(() => ({
      readTraderFile: {
        description: "t",
        inputSchema: z.object({ ping: z.string().optional() }),
        execute: async () => "",
      },
    })),
  };
});

vi.mock("ai", async (importOriginal) => {
  const actual = await importOriginal<typeof import("ai")>();
  return {
    ...actual,
    streamText: streamTextMock,
  };
});

import { POST } from "@/app/api/chat/route";

describe("POST /api/chat (functional wiring)", () => {
  beforeEach(() => {
    vi.clearAllMocks();
    streamTextMock.mockImplementation(() => ({
      toUIMessageStreamResponse,
    }));
  });

  it("parses UIMessages, converts them, calls streamText with tools, returns streaming response", async () => {
    const body = {
      messages: [{ id: "u1", role: "user", parts: [{ type: "text", text: "hello sigma" }] }],
    };
    const req = new Request("http://localhost/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    const res = await POST(req);

    expect(res.status).toBe(200);
    expect(streamTextMock).toHaveBeenCalledTimes(1);

    const call = streamTextMock.mock.calls[0][0];
    expect(call.model).toBe("mock-language-model");
    expect(typeof call.system).toBe("string");
    expect(call.system!.length).toBeGreaterThan(20);
    expect(Array.isArray(call.messages)).toBe(true);
    expect(call.messages!.length).toBeGreaterThanOrEqual(1);
    expect(call.messages![0].role).toBe("user");
    expect(call.tools).toBeDefined();
    expect(toUIMessageStreamResponse).toHaveBeenCalledTimes(1);
  });

  it("rejects invalid JSON body", async () => {
    const req = new Request("http://localhost/api/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: "{not-json",
    });
    await expect(POST(req)).rejects.toThrow();
  });
});
