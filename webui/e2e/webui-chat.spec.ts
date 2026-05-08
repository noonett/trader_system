/**
 * End-to-end functional tests (real stack):
 * - Next.js dev server + `.env.local` LLM credentials
 * - Real POST /api/chat and streaming UI — no mocks.
 *
 * Prerequisite (once): `cd webui && npx playwright install chromium`
 *
 * Run (from `webui/`):
 * - `npm run test:e2e` — full suite
 * - `npm run test:e2e:quick` — first test only (short chat)
 * - `npm run test:e2e:ema` — 盘后 EMA 快捷流（多 tool，最耗时）
 * - `npm run test:e2e:quick-actions` — 全部快捷按钮
 */
import { test, expect, type Page } from "@playwright/test";

test.describe.configure({ mode: "serial" });

/** React 受控 input：确保触发 input 事件，`发送` 才会启用 */
async function fillChatInput(page: Page, text: string) {
  const input = page.getByTestId("chat-input");
  await input.click();
  await input.clear();
  await input.pressSequentially(text, { delay: 5 });
  await expect(page.getByRole("button", { name: "发送" })).toBeEnabled({ timeout: 10_000 });
}

function waitForChatPostOk(page: Page) {
  return page.waitForResponse(
    (res) =>
      res.url().includes("/api/chat") &&
      res.request().method() === "POST" &&
      res.ok(),
    { timeout: 180_000 },
  );
}

/** 等待流式结束：`停止` 消失且可选检测 assistant 有实质内容 */
async function waitForAssistantStreamDone(page: Page, opts: { streamTimeoutMs: number; minChars: number }) {
  await expect(page.getByRole("button", { name: "停止" })).not.toBeVisible({ timeout: opts.streamTimeoutMs });
  await expect(page.getByTestId("chat-error")).toHaveCount(0);
  await expect
    .poll(
      async () => {
        const last = page.getByTestId("message-assistant").last();
        return (await last.innerText()).trim().length;
      },
      { timeout: 120_000 },
    )
    .toBeGreaterThan(opts.minChars);
}

/**
 * 点击快捷按钮并跑完一整轮对话。
 * 「盘后 EMA / 决策链」常会触发 list/read/write/gitCommit，需更长 streamTimeoutMs。
 */
async function runQuickAction(
  page: Page,
  buttonLabel: string,
  options: {
    streamTimeoutMs: number;
    userSubstring: string;
    minAssistantChars?: number;
  },
) {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "σ Trading System" })).toBeVisible();

  await Promise.all([
    waitForChatPostOk(page),
    page.getByRole("button", { name: buttonLabel }).click(),
  ]);

  await expect(page.getByRole("button", { name: "停止" })).toBeVisible({ timeout: 60_000 });

  await waitForAssistantStreamDone(page, {
    streamTimeoutMs: options.streamTimeoutMs,
    minChars: options.minAssistantChars ?? 12,
  });

  await expect(page.getByTestId("message-user").first()).toContainText(options.userSubstring);
}

test.describe("σ WebUI — real API chat", () => {
  test("首页加载 + 手动发送一条消息并完成流式回复", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByRole("heading", { name: "σ Trading System" })).toBeVisible();

    const marker = `e2e-marker-${Date.now()}`;
    const prompt = `请用一两句话回复。必须包含这段标记：${marker}`;

    await Promise.all([
      waitForChatPostOk(page),
      (async () => {
        await fillChatInput(page, prompt);
        await page.getByRole("button", { name: "发送" }).click();
        await expect(page.getByRole("button", { name: "停止" })).toBeVisible({ timeout: 45_000 });
      })(),
    ]);

    await waitForAssistantStreamDone(page, { streamTimeoutMs: 180_000, minChars: 5 });

    await expect(page.getByTestId("message-user").getByText(marker, { exact: false })).toBeVisible();
  });

  test("快捷「盘前规则」触发真实对话并完成（无 chat-error）", async ({ page }) => {
    await runQuickAction(page, "盘前规则", {
      streamTimeoutMs: 240_000,
      userSubstring: "盘前规则",
      minAssistantChars: 10,
    });
  });

  test("快捷「盘后 EMA」触发真实对话并完成（无 chat-error） @ema-tools", async ({ page }) => {
    await runQuickAction(page, "盘后 EMA", {
      /** 多轮 tool（列目录 / 读模板或交易档 / 写 §四 / commit）易超过普通对话 */
      streamTimeoutMs: 280_000,
      userSubstring: "盘后 EMA",
      minAssistantChars: 15,
    });

    const lastAssistant = page.getByTestId("message-assistant").last();
    const body = (await lastAssistant.innerText()).trim();
    /** 工具调用会在气泡内渲染 ⚡；若模型仅口头引导而未调用工具，上面 minChars 仍兜底 */
    const hasToolOrSubstantive = body.includes("⚡") || body.length > 80;
    expect(hasToolOrSubstantive).toBeTruthy();
  });

  test("快捷「开仓决策链」触发真实对话并完成（无 chat-error）", async ({ page }) => {
    await runQuickAction(page, "开仓决策链", {
      streamTimeoutMs: 280_000,
      userSubstring: "决策链",
      minAssistantChars: 20,
    });
  });

  test("快捷「周复盘」触发真实对话并完成（无 chat-error）", async ({ page }) => {
    await runQuickAction(page, "周复盘", {
      streamTimeoutMs: 260_000,
      userSubstring: "周复盘",
      minAssistantChars: 15,
    });
  });

  test("手动输入：盘后 EMA 窄指令（优先短回复，检测管线不死锁）", async ({ page }) => {
    await page.goto("/");
    await expect(page.getByRole("heading", { name: "σ Trading System" })).toBeVisible();

    const marker = `ema-smoke-${Date.now()}`;
    const prompt =
      `【E2E】请不要调用任何工具。仅用两句话说明盘后 EMA §四 四个字段名称（结果、执行、情绪、信号），并包含标记 ${marker}`;

    await Promise.all([
      waitForChatPostOk(page),
      (async () => {
        await fillChatInput(page, prompt);
        await page.getByRole("button", { name: "发送" }).click();
        await expect(page.getByRole("button", { name: "停止" })).toBeVisible({ timeout: 45_000 });
      })(),
    ]);

    await waitForAssistantStreamDone(page, { streamTimeoutMs: 120_000, minChars: 20 });

    await expect(page.getByTestId("message-user").getByText(marker, { exact: false })).toBeVisible();
    await expect(page.getByTestId("message-assistant").last()).toContainText(/情绪|执行|结果|信号/, {
      timeout: 15_000,
    });
  });
});
