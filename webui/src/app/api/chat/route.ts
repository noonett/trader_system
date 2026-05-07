import { convertToModelMessages, streamText, stepCountIs } from "ai";
import { createTools } from "@/lib/tools";
import { SYSTEM_PROMPT } from "@/lib/system-prompt";
import { getModel } from "@/lib/model";

export const maxDuration = 60;

export async function POST(req: Request) {
  const { messages } = await req.json();

  const traderId = "default";
  const tools = createTools(traderId);
  // useChat() sends UIMessage[]; streamText expects ModelMessage[] (AI SDK v6)
  const modelMessages = await convertToModelMessages(messages, {
    ignoreIncompleteToolCalls: true,
  });

  const result = streamText({
    model: getModel(),
    system: SYSTEM_PROMPT,
    messages: modelMessages,
    tools,
    stopWhen: stepCountIs(10),
  });

  return result.toUIMessageStreamResponse();
}
