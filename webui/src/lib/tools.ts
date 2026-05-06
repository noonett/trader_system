import { z } from "zod";
import { readFile, writeFile, listFiles, gitCommit } from "./repo";

export function createTools(traderId = "default") {
  return {
    readTraderFile: {
      description:
        "Read a file from the trader's data directory or shared templates/knowledge. Returns file content.",
      parameters: z.object({
        filePath: z.string().describe("Relative path from workspace root"),
      }),
      execute: async ({ filePath }: { filePath: string }) => {
        const content = await readFile(filePath);
        return content.slice(0, 12000);
      },
    },

    writeTraderFile: {
      description:
        "Write/create a markdown file in the trader's data directory. Use for pre-market daily files, trade records, EMA entries, and reviews.",
      parameters: z.object({
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
    },

    listTraderFiles: {
      description: "List markdown files in a directory. Useful for finding trades, daily files, or reviews.",
      parameters: z.object({
        directory: z.string().describe("Relative directory path"),
      }),
      execute: async ({ directory }: { directory: string }) => {
        const files = await listFiles(directory);
        return files.length > 0 ? files.join("\n") : "No .md files found";
      },
    },

    gitCommit: {
      description: "Stage and commit files to git. Use after writing pre-market rules, trade records, or reviews.",
      parameters: z.object({
        files: z.array(z.string()).describe("File paths to stage"),
        message: z.string().describe("Git commit message"),
      }),
      execute: async ({ files, message }: { files: string[]; message: string }) => {
        const hash = await gitCommit(files, message);
        return `Committed: ${hash} — ${message}`;
      },
    },

    getTodayInfo: {
      description: "Get today's date, day of week, and trading session info.",
      parameters: z.object({}),
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
    },

    readTemplate: {
      description:
        "Read a shared σ template (pre-market, decision-chain, post-trade-ema, weekly-review, monthly-calibration, ai-roles).",
      parameters: z.object({
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
    },
  };
}
