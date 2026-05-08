import * as fs from "fs";
import * as os from "os";
import * as path from "path";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

describe("repo (workspace discovery from cwd)", () => {
  let repoRoot: string;

  beforeEach(() => {
    repoRoot = fs.mkdtempSync(path.join(os.tmpdir(), "webui-repo-cwd-"));
    const tplDir = path.join(repoRoot, "sigma", "templates");
    fs.mkdirSync(tplDir, { recursive: true });
    fs.writeFileSync(path.join(tplDir, "pre-market.md"), "# template");
    delete process.env.SIGMA_WORKSPACE;
    vi.resetModules();
  });

  afterEach(() => {
    fs.rmSync(repoRoot, { recursive: true, force: true });
  });

  it("finds repo root when cwd is webui subdirectory", async () => {
    const webuiDir = path.join(repoRoot, "webui");
    fs.mkdirSync(webuiDir, { recursive: true });
    const cwdSpy = vi.spyOn(process, "cwd").mockReturnValue(webuiDir);
    const { traderRoot } = await import("../src/lib/repo");
    expect(traderRoot("default")).toBe(path.join(repoRoot, "traders", "default"));
    cwdSpy.mockRestore();
  });
});

describe("repo (SIGMA_WORKSPACE isolation)", () => {
  let tmp: string;

  beforeEach(() => {
    tmp = fs.mkdtempSync(path.join(os.tmpdir(), "webui-repo-test-"));
    process.env.SIGMA_WORKSPACE = tmp;
    vi.resetModules();
  });

  afterEach(() => {
    fs.rmSync(tmp, { recursive: true, force: true });
    delete process.env.SIGMA_WORKSPACE;
  });

  it("traderRoot resolves under workspace", async () => {
    const { traderRoot } = await import("../src/lib/repo");
    expect(traderRoot("default")).toBe(path.join(tmp, "traders", "default"));
  });

  it("readFile rejects path traversal outside workspace", async () => {
    const { readFile } = await import("../src/lib/repo");
    await expect(readFile("../../../windows/system.ini")).rejects.toThrow("Path traversal blocked");
  });

  it("writeFile then readFile round-trip under workspace", async () => {
    const { writeFile, readFile } = await import("../src/lib/repo");
    const rel = "traders/default/daily/2026-05/smoke.md";
    await writeFile(rel, "# hello");
    expect(await readFile(rel)).toBe("# hello");
    expect(fs.existsSync(path.join(tmp, rel))).toBe(true);
  });
});
