import path from "path";
import { fileURLToPath } from "url";
import { defineConfig, devices } from "@playwright/test";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const baseURL = process.env.PLAYWRIGHT_BASE_URL || "http://127.0.0.1:3000";

/**
 * Real browser E2E: starts `npm run dev` (loads `.env.local`) unless CI/reuse server.
 * Requires a valid LLM key in webui/.env.local — no mocks.
 */
export default defineConfig({
  testDir: path.join(__dirname, "e2e"),
  fullyParallel: false,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 1 : 0,
  workers: 1,
  reporter: [["list"]],
  timeout: 180_000,
  expect: { timeout: 20_000 },
  use: {
    baseURL,
    ...devices["Desktop Chrome"],
    trace: "on-first-retry",
    screenshot: "only-on-failure",
    // 本地快测：优先系统浏览器（避免未下载 Playwright Chromium）；可用 PW_CHANNEL=msedge / chrome 覆盖
    ...(process.env.CI
      ? {}
      : {
          channel: process.env.PW_CHANNEL || "msedge",
        }),
  },
  webServer: {
    command: "npm run dev",
    url: baseURL,
    reuseExistingServer: !process.env.CI,
    timeout: 180_000,
    cwd: __dirname,
  },
});
