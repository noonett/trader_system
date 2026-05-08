#!/usr/bin/env bash
# σ 后台 AI 周读报告生成（B 类后台批处理）
#
# 对应 design_proposal_2026.md §三.2.2 + sigma/templates/ai-roles.md §三。
# 由 Makefile 的 `make weekly-report` 调用。
#
# 流程：
#   1. 收集本周 git log + traders/{id}/trades/ + traders/{id}/daily/ 内容
#   2. 拼接 sigma/templates/ai-roles.md §三 的 prompt
#   3. 调用 LLM（当前方案：用户手动复制 prompt 到 Cursor / ChatGPT；
#      自动化方案：调用 API，需要用户配置 API key）
#   4. 输出写入 traders/{id}/reviews/weekly/YYYY-WW-auto.md + git commit

set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
TRADER="${SIGMA_TRADER:-default}"
TRADER_ROOT="$WORKSPACE/traders/$TRADER"
YEAR=$(date +%G)
WEEK=$(date +%V)
OUTPUT_FILE="$TRADER_ROOT/reviews/weekly/${YEAR}-W${WEEK}-auto.md"

echo "=== σ 后台周读报告生成（trader: $TRADER）==="
echo "Week: ${YEAR}-W${WEEK}"
echo "Output: ${OUTPUT_FILE}"
echo ""

# 1. Collect data
echo "--- Collecting git log (this week) ---"
WEEK_START=$(date -d "last monday" +%Y-%m-%d 2>/dev/null || date -v-mon +%Y-%m-%d 2>/dev/null || echo "unknown")
GIT_LOG=$(cd "$WORKSPACE" && git log --oneline --since="$WEEK_START" --until="now" -- "traders/$TRADER/trades/" "traders/$TRADER/daily/" 2>/dev/null || echo "(no commits this week)")

echo "--- Collecting trades/ files ---"
TRADES_CONTENT=""
for f in "$TRADER_ROOT"/trades/????/??/*.md; do
    [ -f "$f" ] || continue
    fname=$(basename "$f")
    [[ "$fname" == "TEMPLATE.md" || "$fname" == "README.md" || "$fname" == "SCREENSHOTS.md" ]] && continue
    TRADES_CONTENT="${TRADES_CONTENT}
--- FILE: ${fname} ---
$(head -60 "$f")
--- END ---
"
done

echo "--- Collecting daily/ files ---"
DAILY_CONTENT=""
for f in "$TRADER_ROOT"/daily/????-??/*.md; do
    [ -f "$f" ] || continue
    fname=$(basename "$f")
    DAILY_CONTENT="${DAILY_CONTENT}
--- FILE: ${fname} ---
$(cat "$f")
--- END ---
"
done

# 2. Build prompt
AI_ROLES="$WORKSPACE/sigma/templates/ai-roles.md"
PROMPT_TEMPLATE=""
if [ -f "$AI_ROLES" ]; then
    PROMPT_TEMPLATE=$(sed -n '/^## 三、后台周读报告/,/^---$/p' "$AI_ROLES")
fi

FULL_PROMPT="$PROMPT_TEMPLATE

=== 本周 Git Log ===
$GIT_LOG

=== 本周 Trades 文件 ===
$TRADES_CONTENT

=== 本周 Daily 文件 ===
$DAILY_CONTENT
"

# 3. Generate report
PROMPT_FILE="$TRADER_ROOT/reviews/weekly/${YEAR}-W${WEEK}-prompt.txt"
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

if [ -f "$OUTPUT_FILE" ]; then
    cd "$WORKSPACE"
    git add "$OUTPUT_FILE"
    git commit -m "auto(weekly-report): ${YEAR}-W${WEEK} AI 周读报告 (trader: $TRADER)" || true
    echo "Auto report committed."
fi
