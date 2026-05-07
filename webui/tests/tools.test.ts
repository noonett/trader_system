import * as fs from "fs";
import * as os from "os";
import * as path from "path";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

describe("createTools", () => {
  let tmp: string;

  beforeEach(() => {
    tmp = fs.mkdtempSync(path.join(os.tmpdir(), "webui-tools-test-"));
    process.env.SIGMA_WORKSPACE = tmp;
    vi.resetModules();
  });

  afterEach(() => {
    fs.rmSync(tmp, { recursive: true, force: true });
    delete process.env.SIGMA_WORKSPACE;
  });

  it("writeTraderFile rejects paths outside traders/{id}/", async () => {
    const { createTools } = await import("../src/lib/tools");
    const tools = createTools("default");
    const out = await tools.writeTraderFile.execute({
      filePath: "sigma/templates/pre-market.md",
      content: "x",
    });
    expect(out).toMatch(/ERROR/);
  });

  it("writeTraderFile allows traders/default subtree", async () => {
    const { createTools } = await import("../src/lib/tools");
    const tools = createTools("default");
    const rel = "traders/default/daily/2099-01/smoke-tool.md";
    const out = await tools.writeTraderFile.execute({
      filePath: rel,
      content: "# tool write",
    });
    expect(out).toContain("Written:");
    expect(fs.readFileSync(path.join(tmp, rel), "utf-8")).toBe("# tool write");
  });

  it("getTodayInfo returns JSON with dailyFilePath", async () => {
    const { createTools } = await import("../src/lib/tools");
    const tools = createTools("default");
    const raw = await tools.getTodayInfo.execute({});
    const j = JSON.parse(String(raw));
    expect(j.dailyFilePath).toMatch(/^traders\/default\/daily\/\d{4}-\d{2}\//);
  });
});
