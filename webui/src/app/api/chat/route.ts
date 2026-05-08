import { convertToModelMessages, streamText, stepCountIs } from "ai";
import { createTools } from "@/lib/tools";
import { SYSTEM_PROMPT } from "@/lib/system-prompt";
import { getModel } from "@/lib/model";

/** 盘后 EMA / 决策链等多 tool 轮次需 >60s；本地与部署均受益（部署需在平台允许范围内调高）。 */
export const maxDuration = 300;

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
    stopWhen: stepCountIs(25),
  });

  return result.toUIMessageStreamResponse();
}
