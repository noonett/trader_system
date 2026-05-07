import { tool } from "ai";
import { z } from "zod";
import { readFile, writeFile, listFiles, gitCommit } from "./repo";

/**
 * AI SDK v6 expects `inputSchema` on each tool (not `parameters`).
 * Use `tool()` for a typed tool object compatible with streamText.
 */
export function createTools(traderId = "default") {
  return {
    readTraderFile: tool({
      description:
        "Read a file from the trader's data directory or shared templates/knowledge. Returns file content.",
      inputSchema: z.object({
        filePath: z.string().describe("Relative path from workspace root"),
      }),
      execute: async ({ filePath }: { filePath: string }) => {
        const content = await readFile(filePath);
        return content.slice(0, 12000);
      },
    }),

    writeTraderFile: tool({
      description:
        "Write/create a markdown file in the trader's data directory. Use for pre-market daily files, trade records, EMA entries, and reviews.",
      inputSchema: z.object({
        filePath: z.string().describe("Relative path, must be under traders/{id}/"),
        content: z.string().describe("Full file content to write"),
      }),
      execute: async ({ filePath, content }: { filePath: string; content: string }) => {
        if (!filePath.startsWith(`traders/${traderId}/`)) {
          return `ERROR: Can only write to traders/${traderId}/ directory`;
        }
        await writeFile(filePath, content);
        return `Written: ${filePath}`;
      },
    }),

    listTraderFiles: tool({
      description: "List markdown files in a directory. Useful for finding trades, daily files, or reviews.",
      inputSchema: z.object({
        directory: z.string().describe("Relative directory path"),
      }),
      execute: async ({ directory }: { directory: string }) => {
        const files = await listFiles(directory);
        return files.length > 0 ? files.join("\n") : "No .md files found";
      },
    }),

    gitCommit: tool({
      description: "Stage and commit files to git. Use after writing pre-market rules, trade records, or reviews.",
      inputSchema: z.object({
        files: z.array(z.string()).describe("File paths to stage"),
        message: z.string().describe("Git commit message"),
      }),
      execute: async ({ files, message }: { files: string[]; message: string }) => {
        const hash = await gitCommit(files, message);
        return `Committed: ${hash} — ${message}`;
      },
    }),

    getTodayInfo: tool({
      description: "Get today's date, day of week, and trading session info.",
      inputSchema: z.object({
        localeHint: z
          .string()
          .optional()
          .describe("Optional locale hint for wording (e.g. zh-CN); does not change computed dates."),
      }),
      execute: async () => {
        const now = new Date();
        const yyyy = now.getFullYear();
        const mm = String(now.getMonth() + 1).padStart(2, "0");
        const dd = String(now.getDate()).padStart(2, "0");
        const dayNames = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        const day = dayNames[now.getDay()];
        const isWeekday = now.getDay() >= 1 && now.getDay() <= 5;
        const hour = now.getHours();

        let session = "non-trading";
        if (isWeekday) {
          if (hour >= 8 && hour < 9) session = "pre-market (盘前规则时间)";
          else if (hour >= 9 && hour < 12) session = "morning-session";
          else if (hour >= 13 && hour < 15) session = "afternoon-session";
          else if (hour >= 15 && hour < 16) session = "post-close (盘后 EMA 时间)";
          else if (hour >= 20 && hour < 24) session = "us-futures-session";
        }
        if (now.getDay() === 0) session = "weekend (周复盘时间)";

        return JSON.stringify({
          date: `${yyyy}-${mm}-${dd}`,
          day,
          isWeekday,
          session,
          dailyFilePath: `traders/${traderId}/daily/${yyyy}-${mm}/${yyyy}-${mm}-${dd}-pre.md`,
        });
      },
    }),

    readTemplate: tool({
      description:
        "Read a shared σ template (pre-market, decision-chain, post-trade-ema, weekly-review, monthly-calibration, ai-roles).",
      inputSchema: z.object({
        templateName: z.enum([
          "pre-market",
          "decision-chain",
          "post-trade-ema",
          "weekly-review",
          "monthly-calibration",
          "ai-roles",
        ]),
      }),
      execute: async ({ templateName }: { templateName: string }) => {
        const content = await readFile(`sigma/templates/${templateName}.md`);
        return content;
      },
    }),
  };
}
