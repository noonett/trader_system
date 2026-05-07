"use client";

import { useChat } from "@ai-sdk/react";
import { useRef, useEffect, useState, type FormEvent } from "react";

const QUICK_ACTIONS = [
  { label: "盘前规则", message: "我要写今天的盘前规则" },
  { label: "开仓决策链", message: "我想开一笔新交易，请引导我走决策链 5 问" },
  { label: "盘后 EMA", message: "我刚平仓了，请帮我记录盘后 EMA" },
  { label: "周复盘", message: "开始本周的周复盘" },
];

export function Chat() {
  const { messages, sendMessage, status, error, stop } = useChat();
  const [input, setInput] = useState("");
  const scrollRef = useRef<HTMLDivElement>(null);
  const isLoading = status === "streaming" || status === "submitted";

  useEffect(() => {
    scrollRef.current?.scrollTo({ top: scrollRef.current.scrollHeight, behavior: "smooth" });
  }, [messages]);

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    sendMessage({ text: input.trim() });
    setInput("");
  }

  function handleQuickAction(message: string) {
    if (isLoading) return;
    sendMessage({ text: message });
  }

  return (
    <div className="flex flex-col h-screen bg-zinc-950 text-zinc-100">
      <header className="flex items-center justify-between px-6 py-3 border-b border-zinc-800 shrink-0">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 rounded-lg bg-amber-600 flex items-center justify-center font-bold text-sm">
            σ
          </div>
          <div>
            <h1 className="text-sm font-semibold">σ Trading System</h1>
            <p className="text-xs text-zinc-500">Agent-assisted workflow</p>
          </div>
        </div>
        <div className="flex gap-2">
          {QUICK_ACTIONS.map((qa) => (
            <button
              key={qa.label}
              onClick={() => handleQuickAction(qa.message)}
              disabled={isLoading}
              className="px-3 py-1.5 text-xs bg-zinc-900 hover:bg-zinc-800 border border-zinc-700 rounded-lg transition text-zinc-400 hover:text-zinc-200 disabled:opacity-50"
            >
              {qa.label}
            </button>
          ))}
        </div>
      </header>

      <div ref={scrollRef} className="flex-1 overflow-y-auto px-6 py-4 space-y-4">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-zinc-600">
            <div className="w-16 h-16 rounded-2xl bg-zinc-900 flex items-center justify-center text-2xl font-bold mb-4 border border-zinc-800">
              σ
            </div>
            <p className="text-lg mb-1">σ 交易员训练系统</p>
            <p className="text-sm text-zinc-700 max-w-md text-center">
              点击上方快捷按钮开始工作流，或直接输入你的需求。
              所有记录自动保存到 git 仓库。
            </p>
          </div>
        )}

        {messages.map((m) => (
          <div
            key={m.id}
            data-testid={m.role === "user" ? "message-user" : "message-assistant"}
            className={`flex ${m.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-xl px-4 py-3 text-sm leading-relaxed whitespace-pre-wrap ${
                m.role === "user"
                  ? "bg-amber-900/40 text-amber-100 border border-amber-800/50"
                  : "bg-zinc-900 text-zinc-200 border border-zinc-800"
              }`}
            >
              {m.parts?.map((part, i) => {
                if (part.type === "text") return <span key={i}>{part.text}</span>;
                if (part.type?.startsWith("tool-")) {
                  const p = part as { type: string; toolCallId?: string; state?: string; output?: unknown; [k: string]: unknown };
                  const name = (p as Record<string, unknown>).toolName as string | undefined;
                  return (
                    <div key={i} className="mt-1 flex items-center gap-1.5 text-xs text-zinc-500">
                      <span className="text-amber-600">⚡</span>
                      <span>{name || p.type}</span>
                      {p.state === "result" && p.output != null && (
                        <span className="text-zinc-600 truncate max-w-xs">
                          → {String(p.output).slice(0, 80)}
                        </span>
                      )}
                    </div>
                  );
                }
                return null;
              })}
            </div>
          </div>
        ))}

        {isLoading && messages.length > 0 && messages[messages.length - 1].role === "user" && (
          <div className="flex justify-start">
            <div className="bg-zinc-900 border border-zinc-800 rounded-xl px-4 py-3 text-sm text-zinc-500">
              <span className="inline-block animate-pulse">思考中...</span>
            </div>
          </div>
        )}

        {error && (
          <div
            data-testid="chat-error"
            className="bg-red-950/50 border border-red-800 rounded-xl px-4 py-3 text-sm text-red-300"
          >
            错误: {error.message}
          </div>
        )}
      </div>

      <form onSubmit={handleSubmit} className="px-6 py-4 border-t border-zinc-800 shrink-0">
        <div className="flex gap-3">
          <input
            data-testid="chat-input"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="输入消息..."
            className="flex-1 bg-zinc-900 border border-zinc-700 rounded-xl px-4 py-3 text-sm text-zinc-100 placeholder-zinc-600 focus:outline-none focus:border-amber-700 transition"
            disabled={isLoading}
          />
          {isLoading ? (
            <button
              type="button"
              onClick={stop}
              className="px-6 py-3 bg-red-800 hover:bg-red-700 text-sm font-medium rounded-xl transition"
            >
              停止
            </button>
          ) : (
            <button
              type="submit"
              disabled={!input.trim()}
              className="px-6 py-3 bg-amber-700 hover:bg-amber-600 disabled:bg-zinc-800 disabled:text-zinc-600 text-sm font-medium rounded-xl transition"
            >
              发送
            </button>
          )}
        </div>
      </form>
    </div>
  );
}
