#!/usr/bin/env bash
# σ 后台 AI 周读报告生成（B 类后台批处理）
#
# 对应 design_proposal_2026.md §三.2.2 + sigma/ai-roles.md §三。
# 由 Makefile 的 `make weekly-report` 调用。
#
# 流程：
#   1. 收集本周 git log + trades/ + sigma/daily/ 内容
#   2. 拼接 sigma/ai-roles.md §三 的 prompt
#   3. 调用 LLM（当前方案：用户手动复制 prompt 到 Cursor / ChatGPT；
#      自动化方案：调用 API，需要用户配置 API key）
#   4. 输出写入 reviews/weekly/YYYY-WW-auto.md + git commit

set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
YEAR=$(date +%G)
WEEK=$(date +%V)
OUTPUT_FILE="$WORKSPACE/reviews/weekly/${YEAR}-W${WEEK}-auto.md"

echo "=== σ 后台周读报告生成 ==="
echo "Week: ${YEAR}-W${WEEK}"
echo "Output: ${OUTPUT_FILE}"
echo ""

# 1. Collect data
echo "--- Collecting git log (this week) ---"
WEEK_START=$(date -d "last monday" +%Y-%m-%d 2>/dev/null || date -v-mon +%Y-%m-%d 2>/dev/null || echo "unknown")
GIT_LOG=$(cd "$WORKSPACE" && git log --oneline --since="$WEEK_START" --until="now" -- trades/ sigma/daily/ 2>/dev/null || echo "(no commits this week)")

echo "--- Collecting trades/ files ---"
TRADES_CONTENT=""
for f in "$WORKSPACE"/trades/????/??/*.md; do
    [ -f "$f" ] || continue
    fname=$(basename "$f")
    # Check if file date is this week (simplified: just include recent files)
    TRADES_CONTENT="${TRADES_CONTENT}
--- FILE: ${fname} ---
$(head -60 "$f")
--- END ---
"
done

echo "--- Collecting sigma/daily/ files ---"
DAILY_CONTENT=""
for f in "$WORKSPACE"/sigma/daily/????-??/*.md; do
    [ -f "$f" ] || continue
    fname=$(basename "$f")
    DAILY_CONTENT="${DAILY_CONTENT}
--- FILE: ${fname} ---
$(cat "$f")
--- END ---
"
done

# 2. Build prompt
PROMPT_TEMPLATE=$(cat "$WORKSPACE/sigma/ai-roles.md" | sed -n '/^## 三、后台周读报告/,/^---$/p')

FULL_PROMPT="$PROMPT_TEMPLATE

=== 本周 Git Log ===
$GIT_LOG

=== 本周 Trades 文件 ===
$TRADES_CONTENT

=== 本周 Daily 文件 ===
$DAILY_CONTENT
"

# 3. Generate report
# 当前方案（v0 最简）：把 prompt 写到临时文件，用户手动复制到 Cursor / ChatGPT
PROMPT_FILE="$WORKSPACE/reviews/weekly/${YEAR}-W${WEEK}-prompt.txt"
mkdir -p "$(dirname "$PROMPT_FILE")"
echo "$FULL_PROMPT" > "$PROMPT_FILE"

echo ""
echo "=== Prompt 已生成 ==="
echo "文件：$PROMPT_FILE"
echo ""
echo "请打开上面的文件，复制全部内容到 Cursor AI / ChatGPT，"
echo "将 AI 输出保存到：$OUTPUT_FILE"
echo ""
echo "（或者如果已配置 API key，自动调用 API 生成——Phase 3b 强化）"
echo ""

# 如果输出文件已存在（用户已手动填入 AI 输出），自动 git commit
if [ -f "$OUTPUT_FILE" ]; then
    cd "$WORKSPACE"
    git add "$OUTPUT_FILE"
    git commit -m "auto(weekly-report): ${YEAR}-W${WEEK} AI 周读报告" || true
    echo "Auto report committed."
fi

# 清理 prompt 文件（不 commit 到仓库——它是中间产物）
echo "$PROMPT_FILE" >> "$WORKSPACE/.gitignore" 2>/dev/null || true
