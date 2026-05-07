/**
 * End-to-end functional tests (real stack):
 * - Next.js dev server + `.env.local` LLM credentials
 * - Real POST /api/chat and streaming UI — no mocks.
 *
 * Prerequisite (once): `cd webui && npx playwright install chromium`
 *
 * Run: `npm run test:e2e` (full) or `npm run test:e2e:quick` (one real chat round) from `webui/`
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

function waitForChatOk(page: Page) {
  return page.waitForResponse(
    (res) =>
      res.url().includes("/api/chat") &&
      res.request().method() === "POST" &&
      res.ok(),
    { timeout: 120_000 },
  );
}

test.describe("σ WebUI — real API chat", () => {
  test("首页加载 + 手动发送一条消息并完成流式回复", async ({ page }) => {
    await page.goto("/");

    await expect(page.getByRole("heading", { name: "σ Trading System" })).toBeVisible();

    const marker = `e2e-marker-${Date.now()}`;
    const prompt = `请用一两句话回复。必须包含这段标记：${marker}`;

    await Promise.all([
      waitForChatOk(page),
      (async () => {
        await fillChatInput(page, prompt);
        await page.getByRole("button", { name: "发送" }).click();
        await expect(page.getByRole("button", { name: "停止" })).toBeVisible({ timeout: 45_000 });
      })(),
    ]);

    await expect(page.getByRole("button", { name: "停止" })).not.toBeVisible({ timeout: 120_000 });

    await expect(page.getByTestId("chat-error")).toHaveCount(0);

    await expect(page.getByTestId("message-user").getByText(marker, { exact: false })).toBeVisible();

    await expect
      .poll(
        async () => {
          const last = page.getByTestId("message-assistant").last();
          return (await last.innerText()).trim().length;
        },
        { timeout: 90_000 },
      )
      .toBeGreaterThan(5);
  });

  test("快捷「盘前规则」触发真实对话并完成（无 chat-error）", async ({ page }) => {
    await page.goto("/");

    await Promise.all([
      waitForChatOk(page),
      page.getByRole("button", { name: "盘前规则" }).click(),
    ]);

    await expect(page.getByRole("button", { name: "停止" })).toBeVisible({ timeout: 45_000 });

    await expect(page.getByRole("button", { name: "停止" })).not.toBeVisible({ timeout: 180_000 });

    await expect(page.getByTestId("chat-error")).toHaveCount(0);

    await expect(page.getByTestId("message-user").first()).toContainText("盘前规则");

    await expect
      .poll(
        async () => {
          const last = page.getByTestId("message-assistant").last();
          return (await last.innerText()).trim().length;
        },
        { timeout: 90_000 },
      )
      .toBeGreaterThan(10);
  });
});
