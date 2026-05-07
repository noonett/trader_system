#!/usr/bin/env bash
# 安装 σ 系统 git hooks
# 当前含：pre-commit hook（红区 schema 拒绝 — C 类后台强制）
#
# 使用：bash scripts/install_hooks.sh

set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$WORKSPACE/.git/hooks"

echo "Installing σ pre-commit hook..."

cat > "$HOOKS_DIR/pre-commit" << 'HOOK_EOF'
#!/usr/bin/env bash
# σ pre-commit hook — 红区 schema 拒绝（C 类后台强制）
# 对应 design_proposal_2026.md §三.2.3 C 类 + foundation §三.10 红区"技术性禁入"
#
# 检测 trades/*.md frontmatter 的 product_class: red → 拒绝 commit
# 绕过方式：git commit --no-verify（但 A 类违规扫描会抓到）

RED_FOUND=0

for file in $(git diff --cached --name-only --diff-filter=ACM | grep 'trades/.*\.md$'); do
    # Skip TEMPLATE.md and README.md
    basename=$(basename "$file")
    if [ "$basename" = "TEMPLATE.md" ] || [ "$basename" = "README.md" ]; then
        continue
    fi

    # Check frontmatter for product_class: red
    if head -20 "$file" | grep -q 'product_class:.*red'; then
        echo "❌ σ 红区产品拦截：$file"
        echo "   product_class: red — 红区产品不可记录到 σ 训练资金账户"
        echo "   (foundation §三.10：0DTE 期权 / 超高杠杆永续合约 / 无法定义最大损失的产品)"
        echo ""
        echo "   如果确认需要绕过：git commit --no-verify"
        echo "   ⚠ 绕过将被后台违规扫描（reviews/violations/）记录"
        echo ""
        RED_FOUND=1
    fi
done

if [ "$RED_FOUND" -eq 1 ]; then
    exit 1
fi

exit 0
HOOK_EOF

chmod +x "$HOOKS_DIR/pre-commit"
echo "Done. Pre-commit hook installed at $HOOKS_DIR/pre-commit"
