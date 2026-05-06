import path from "path";
import fs from "fs/promises";
import simpleGit from "simple-git";

const WORKSPACE = process.env.SIGMA_WORKSPACE || path.resolve(__dirname, "../../../..");

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
  return fs.readFile(resolved, "utf-8");
}

export async function writeFile(filePath: string, content: string): Promise<void> {
  const resolved = path.resolve(WORKSPACE, filePath);
  if (!resolved.startsWith(WORKSPACE)) {
    throw new Error("Path traversal blocked");
  }
  await fs.mkdir(path.dirname(resolved), { recursive: true });
  await fs.writeFile(resolved, content, "utf-8");
}

export async function listFiles(dirPath: string): Promise<string[]> {
  const resolved = path.resolve(WORKSPACE, dirPath);
  if (!resolved.startsWith(WORKSPACE)) {
    throw new Error("Path traversal blocked");
  }
  try {
    const entries = await fs.readdir(resolved, { withFileTypes: true, recursive: true });
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
