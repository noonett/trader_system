import path from "path";
import fs from "fs";
import fsp from "fs/promises";
import simpleGit from "simple-git";

/**
 * Resolve the σ repo root (contains sigma/templates/, traders/, etc.).
 * Next.js bundles server code deep under .next/, so __dirname-based hops are unreliable.
 * Prefer SIGMA_WORKSPACE, then walk up from cwd until pre-market template exists.
 */
function resolveSigmaWorkspace(): string {
  const env = process.env.SIGMA_WORKSPACE?.trim();
  if (env) {
    return path.resolve(env);
  }
  let dir = process.cwd();
  for (let i = 0; i < 16; i++) {
    const marker = path.join(dir, "sigma", "templates", "pre-market.md");
    if (fs.existsSync(marker)) {
      return dir;
    }
    const parent = path.dirname(dir);
    if (parent === dir) {
      break;
    }
    dir = parent;
  }
  return path.resolve(__dirname, "../../../..");
}

const WORKSPACE = resolveSigmaWorkspace();

export function traderRoot(traderId = "default") {
  return path.join(WORKSPACE, "traders", traderId);
}

export function traderPaths(traderId = "default") {
  const root = traderRoot(traderId);
  return {
    root,
    daily: path.join(root, "daily"),
    trades: path.join(root, "trades"),
    reviews: path.join(root, "reviews"),
    weekly: path.join(root, "reviews", "weekly"),
    monthly: path.join(root, "reviews", "monthly"),
    violations: path.join(root, "reviews", "violations"),
    alerts: path.join(root, "reviews", "alerts"),
    reconcile: path.join(root, "reviews", "reconcile"),
    profile: path.join(root, "profile"),
    config: path.join(root, "config.yaml"),
  };
}

export function sharedPaths() {
  return {
    templates: path.join(WORKSPACE, "sigma", "templates"),
    knowledge: path.join(WORKSPACE, "knowledge"),
  };
}

export function git() {
  return simpleGit(WORKSPACE);
}

export async function readFile(filePath: string): Promise<string> {
  const resolved = path.resolve(WORKSPACE, filePath);
  if (!resolved.startsWith(WORKSPACE)) {
    throw new Error("Path traversal blocked");
  }
  return fsp.readFile(resolved, "utf-8");
}

export async function writeFile(filePath: string, content: string): Promise<void> {
  const resolved = path.resolve(WORKSPACE, filePath);
  if (!resolved.startsWith(WORKSPACE)) {
    throw new Error("Path traversal blocked");
  }
  await fsp.mkdir(path.dirname(resolved), { recursive: true });
  await fsp.writeFile(resolved, content, "utf-8");
}

export async function listFiles(dirPath: string): Promise<string[]> {
  const resolved = path.resolve(WORKSPACE, dirPath);
  if (!resolved.startsWith(WORKSPACE)) {
    throw new Error("Path traversal blocked");
  }
  try {
    const entries = await fsp.readdir(resolved, { withFileTypes: true, recursive: true });
    return entries
      .filter((e) => e.isFile() && e.name.endsWith(".md"))
      .map((e) => path.relative(WORKSPACE, path.join((e as unknown as { parentPath?: string }).parentPath || "", e.name)));
  } catch {
    return [];
  }
}

export async function gitCommit(files: string[], message: string): Promise<string> {
  const g = git();
  await g.add(files.map((f) => path.resolve(WORKSPACE, f)));
  const result = await g.commit(message);
  return result.commit || "no changes";
}
