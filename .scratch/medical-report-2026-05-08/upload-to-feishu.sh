#!/usr/bin/env bash
# 飞书文档批量上传脚本
# 前置条件：你已经在本机完成 lark-cli 安装 + 授权（详见 README）
# 用法：bash upload-to-feishu.sh [可选：父文件夹 token]

set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
FOLDER_TOKEN="${1:-}"

# 检查 lark-cli 是否已安装
if ! command -v lark-cli >/dev/null 2>&1; then
  echo "❌ lark-cli 未安装。请先运行：npm install -g @larksuite/cli"
  exit 1
fi

# 检查授权状态
if ! lark-cli auth status >/dev/null 2>&1; then
  echo "❌ lark-cli 未完成授权。请先运行："
  echo "   1) lark-cli config init --new   # 创建/绑定应用（浏览器中完成）"
  echo "   2) lark-cli auth login --domain docs,drive,wiki   # 设备码授权"
  exit 1
fi

# 文档清单（标题 → 文件）
declare -a TITLES=(
  "00 必读 · 今晚行动 - 钟钊灵病情家属备查"
  "01 病情整合分析 - 钟钊灵病情家属备查"
  "02 问医生清单 + 红线症状 - 钟钊灵病情家属备查"
  "03 家庭行动方案 - 钟钊灵病情家属备查"
  "04 医生评估 + 二诊路径 - 钟钊灵病情家属备查"
  "00 索引 - 钟钊灵病情家属备查"
)

declare -a FILES=(
  "00_必读_今晚行动.md"
  "01_病情整合分析.md"
  "02_问医生清单_红线症状.md"
  "03_家庭行动方案.md"
  "04_医生评估_二诊路径.md"
  "README_索引.md"
)

# 构建 folder 参数（如有）
FOLDER_ARG=""
if [[ -n "$FOLDER_TOKEN" ]]; then
  FOLDER_ARG="--folder-token $FOLDER_TOKEN"
fi

echo "📤 开始上传 6 份文档到飞书..."
echo

for i in "${!FILES[@]}"; do
  TITLE="${TITLES[$i]}"
  FILE="$DIR/${FILES[$i]}"

  if [[ ! -f "$FILE" ]]; then
    echo "⚠️  文件不存在：$FILE （跳过）"
    continue
  fi

  echo "[$((i+1))/${#FILES[@]}] 上传：$TITLE"

  RESULT=$(lark-cli docs +create \
    --title "$TITLE" \
    --markdown "@$FILE" \
    $FOLDER_ARG \
    2>&1) || {
    echo "❌ 上传失败：$TITLE"
    echo "$RESULT"
    continue
  }

  # 提取 URL（如返回中含 url 字段）
  URL=$(echo "$RESULT" | grep -oE 'https://[^"]+\.feishu\.cn/[^"]+' | head -1 || true)
  TOKEN=$(echo "$RESULT" | grep -oE '"document_id":"[^"]+"' | sed 's/.*"document_id":"\([^"]*\)".*/\1/' | head -1 || true)

  if [[ -n "$URL" ]]; then
    echo "✅ 完成：$URL"
  elif [[ -n "$TOKEN" ]]; then
    echo "✅ 完成：document_id=$TOKEN"
  else
    echo "✅ 完成（未解析 URL）"
  fi
  echo
done

echo "🎉 全部上传完成。"
echo "建议：在飞书中新建一个文件夹「钟钊灵病情家属备查」，把 6 份文档移入。"
