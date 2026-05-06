#!/usr/bin/env bash
# σ 后台 AI 月校准报告生成
#
# 对应 design_proposal_2026.md §三.2.2 + sigma/ai-roles.md §四。
# 由 Makefile 的 `make monthly-calibration` 调用。
# 流程与 weekly_report.sh 同构，时间范围改为本月。

set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
YEAR=$(date +%Y)
MONTH=$(date +%m)
OUTPUT_FILE="$WORKSPACE/reviews/monthly/${YEAR}-${MONTH}-auto.md"

echo "=== σ 后台月校准报告生成 ==="
echo "Month: ${YEAR}-${MONTH}"
echo "Output: ${OUTPUT_FILE}"
echo ""

MONTH_START="${YEAR}-${MONTH}-01"
GIT_LOG=$(cd "$WORKSPACE" && git log --oneline --since="$MONTH_START" --until="now" -- trades/ sigma/daily/ reviews/weekly/ 2>/dev/null || echo "(no commits this month)")

PROMPT_TEMPLATE=$(cat "$WORKSPACE/sigma/ai-roles.md" | sed -n '/^## 四、后台月校准报告/,/^---$/p')

FULL_PROMPT="$PROMPT_TEMPLATE

=== 本月 Git Log ===
$GIT_LOG
"

PROMPT_FILE="$WORKSPACE/reviews/monthly/${YEAR}-${MONTH}-prompt.txt"
mkdir -p "$(dirname "$PROMPT_FILE")"
echo "$FULL_PROMPT" > "$PROMPT_FILE"

echo "Prompt 已生成：$PROMPT_FILE"
echo "请复制到 Cursor AI / ChatGPT，将输出保存到：$OUTPUT_FILE"

if [ -f "$OUTPUT_FILE" ]; then
    cd "$WORKSPACE"
    git add "$OUTPUT_FILE"
    git commit -m "auto(monthly-calibration): ${YEAR}-${MONTH} AI 月校准报告" || true
fi
