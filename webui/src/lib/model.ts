import { anthropic } from "@ai-sdk/anthropic";
import { createOpenAI } from "@ai-sdk/openai";
import { createDeepSeekRequestFetch } from "@/lib/deepseek-fetch";

/**
 * Resolve LLM provider + model from environment variables.
 *
 * Supported SIGMA_PROVIDER values:
 *   "anthropic"  — Claude (needs ANTHROPIC_API_KEY)
 *   "openai"     — GPT (needs OPENAI_API_KEY)
 *   "ollama"     — Local Ollama (free, needs Ollama running)
 *   "openrouter" — OpenRouter gateway (needs OPENROUTER_API_KEY)
 *   "deepseek"   — DeepSeek (needs DEEPSEEK_API_KEY)
 *   "custom"     — Any OpenAI-compatible API (needs CUSTOM_API_KEY + CUSTOM_BASE_URL)
 */
export function getModel() {
  const provider = (process.env.SIGMA_PROVIDER || "anthropic").toLowerCase();
  const modelId = process.env.SIGMA_MODEL || "";

  switch (provider) {
    case "anthropic":
      return anthropic(modelId || "claude-sonnet-4-20250514");

    case "openai": {
      const openai = createOpenAI({ apiKey: process.env.OPENAI_API_KEY });
      return openai(modelId || "gpt-4o");
    }

    case "ollama": {
      const ollama = createOpenAI({
        baseURL: process.env.OLLAMA_BASE_URL || "http://localhost:11434/v1",
        apiKey: "ollama",
        name: "ollama",
      });
      // OpenAI-compat servers implement Chat Completions, not OpenAI Responses API.
      return ollama.chat(modelId || "llama3.2");
    }

    case "openrouter": {
      const openrouter = createOpenAI({
        baseURL: "https://openrouter.ai/api/v1",
        apiKey: process.env.OPENROUTER_API_KEY,
        name: "openrouter",
      });
      return openrouter.chat(modelId || "anthropic/claude-sonnet-4");
    }

    case "deepseek": {
      const deepseek = createOpenAI({
        baseURL: "https://api.deepseek.com/v1",
        apiKey: process.env.DEEPSEEK_API_KEY,
        name: "deepseek",
        fetch: createDeepSeekRequestFetch(),
      });
      return deepseek.chat(modelId || "deepseek-chat");
    }

    case "custom": {
      const custom = createOpenAI({
        baseURL: process.env.CUSTOM_BASE_URL,
        apiKey: process.env.CUSTOM_API_KEY,
        name: "custom-openai-compat",
      });
      return custom.chat(modelId || "default");
    }

    default:
      throw new Error(`Unknown provider: ${provider}. Set SIGMA_PROVIDER to one of: anthropic, openai, ollama, openrouter, deepseek, custom`);
  }
}
