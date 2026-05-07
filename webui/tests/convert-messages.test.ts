import { describe, expect, it } from "vitest";
import { convertToModelMessages } from "ai";

/**
 * Regression: useChat sends UIMessage[]; streamText needs ModelMessage[] after conversion.
 */
describe("convertToModelMessages", () => {
  it("converts a minimal user UIMessage from useChat shape", async () => {
    const modelMessages = await convertToModelMessages([
      {
        id: "test-1",
        role: "user",
        parts: [{ type: "text", text: "hello" }],
      },
    ]);
    expect(modelMessages).toHaveLength(1);
    expect(modelMessages[0].role).toBe("user");
    expect(modelMessages[0].content).toEqual([
      expect.objectContaining({ type: "text", text: "hello" }),
    ]);
  });
});
