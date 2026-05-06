# WebUI + 多交易员目录结构设计

> **位置**：本文件是 Phase 3c+ 的补充设计文档。
> **输入**：design_proposal_2026.md v0.1（N=1 目录结构）+ 用户 2026-05-06 "WebUI 嵌入 Agent + 多交易员记录隔离" 需求。
> **当前版本**：v0.1（2026-05-06）

---

## 一、设计原则

1. **数据底层不变**：仍是 markdown + git。WebUI 是"更好的前端"，不替代数据层
2. **共享/专属分明**：系统模板和知识库全交易员共享；交易记录、复盘、画像每人独立
3. **N=1 启动无摩擦**：单交易员使用时不需要关心多用户机制；目录结构本身兼容但不强制
4. **脚本零改动原则**：新结构下现有 scripts/ 只需传入一个 `--trader` 参数或读环境变量即可定位数据目录
5. **git 友好**：多交易员可在同一 repo（目录隔离）或多 repo（物理隔离）——目录结构对两种模式兼容

---

## 二、内容分类

### 2.1 共享层（所有交易员共用，升级时统一更新）

| 内容 | 当前位置 | 新位置 | 说明 |
|---|---|---|---|
| σ 模板（盘前/决策链/EMA/周复盘/月校准） | sigma/*.md | sigma/templates/ | 模板是"空白表"，所有人共用 |
| AI 角色约束 | sigma/ai-roles.md | sigma/templates/ai-roles.md | 9 条 prompt 约束所有人共用 |
| 提醒模板 | sigma/reminders/ | sigma/templates/reminders/ | Calendar/cron 配置参考 |
| 知识库 | knowledge/ | knowledge/ | glossary/risk_rules/meta-rule 等 |
| 调研档案 | research/ | research/ | foundation/design/notes |
| 后台脚本 | scripts/ | scripts/ | 不含交易员数据；接受 --trader 参数 |
| 归档 | archive/ | archive/ | 历史文档 |
| 项目元文件 | AGENTS.md / Makefile / .cursor/ | 根目录 | 不变 |

### 2.2 交易员专属层（每个交易员独立，互不可见）

| 内容 | 当前位置 | 新位置 | 说明 |
|---|---|---|---|
| 盘前 if-then 实例 | sigma/daily/ | traders/{id}/daily/ | 每日记录 |
| 交易记录 | trades/ | traders/{id}/trades/ | 含 frontmatter (account, fund_type) |
| 复盘报告 | reviews/ | traders/{id}/reviews/ | weekly/monthly/violations/alerts/reconcile |
| 交易员画像 | memory/trader-profile.md | traders/{id}/profile/trader-profile.md | 认知积累 |
| 行为偏误 | memory/bias-patterns.md | traders/{id}/profile/bias-patterns.md | 偏误记录 |
| 阶段进度 | memory/stage.md | traders/{id}/profile/stage.md | KPI 跟踪 |
| 临床基线 | memory/clinical_baseline.md | traders/{id}/profile/clinical_baseline.md | PHQ-9/GAD-7 分数 |
| 个人风控定制 | 无 | traders/{id}/config.yaml | 账户列表、个人阈值覆盖 |

---

## 三、新目录结构

```
/workspace/
├── AGENTS.md
├── Makefile
├── .cursor/rules/
│
├── sigma/
│   └── templates/                    ← 共享：σ 模板（所有交易员的"空白表"）
│       ├── pre-market.md
│       ├── post-trade-ema.md
│       ├── decision-chain.md
│       ├── weekly-review.md
│       ├── monthly-calibration.md
│       ├── ai-roles.md
│       └── reminders/
│           ├── calendar-templates.md
│           └── email-cron-config.md
│
├── traders/                          ← 交易员数据根目录
│   ├── default/                      ← N=1 默认交易员（你自己）
│   │   ├── config.yaml               ← 个人配置（账户列表、阈值覆盖）
│   │   ├── daily/                    ← 盘前 if-then 实例
│   │   │   └── YYYY-MM/
│   │   │       └── YYYY-MM-DD-pre.md
│   │   ├── trades/                   ← 交易记录
│   │   │   ├── TEMPLATE.md           ← 交易模板（共享模板的副本或 symlink）
│   │   │   └── YYYY/MM/
│   │   │       └── YYYY-MM-DD-<symbol>-<dir>.md
│   │   ├── reviews/                  ← 复盘 + 风控输出
│   │   │   ├── weekly/
│   │   │   ├── monthly/
│   │   │   ├── violations/
│   │   │   ├── alerts/
│   │   │   └── reconcile/
│   │   └── profile/                  ← 交易员画像（原 memory/）
│   │       ├── trader-profile.md
│   │       ├── bias-patterns.md
│   │       ├── stage.md
│   │       └── clinical_baseline.md
│   │
│   └── {another-trader}/             ← 未来第二个交易员
│       ├── config.yaml
│       ├── daily/
│       ├── trades/
│       ├── reviews/
│       └── profile/
│
├── knowledge/                        ← 共享：知识库
│   ├── INDEX.md
│   ├── glossary.md
│   ├── risk_rules.md
│   ├── meta-rule.md
│   └── clinical_self_check.md
│
├── research/                         ← 共享：调研档案
│   ├── foundation_2026.md
│   ├── entry_form_research_2026.md
│   ├── design_proposal_2026.md
│   ├── design_webui_multitrader_2026.md  ← 本文件
│   └── notes/
│
├── scripts/                          ← 共享：后台脚本
│   ├── weekly_report.sh
│   ├── monthly_calibration.sh
│   ├── violations_scan.py
│   ├── kpi_alert.py
│   ├── reconcile_funds.py
│   └── install_hooks.sh
│
├── webui/                            ← WebUI 应用代码
│   ├── package.json
│   ├── src/
│   └── ...
│
└── archive/                          ← 共享：历史归档
    ├── deprecated_stage0/
    └── ...
```

---

## 四、config.yaml 交易员配置文件

```yaml
# traders/{id}/config.yaml
trader_id: default
display_name: "交易员 A"

# 账户列表
accounts:
  - id: cme-training
    broker: "Interactive Brokers"
    market: futures-cme
    fund_type: training
    currency: USD
  - id: a-share-main
    broker: "华泰证券"
    market: a-share
    fund_type: training
    currency: CNY
  - id: passive-etf
    broker: "华泰证券"
    market: a-share
    fund_type: long-term
    currency: CNY

# 个人阈值覆盖（覆盖 knowledge/risk_rules.md 的默认值）
overrides:
  max_single_position_pct: 20        # 默认 20%，可按个人情况调
  max_daily_loss_pct: 3              # 默认 3%
  yellow_weekly_limit: 3             # 黄区每周最多开仓次数
  black_swan_window_minutes: 30      # 黑天鹅前后窗口

# WebUI 偏好
preferences:
  timezone: "Asia/Shanghai"
  language: "zh-CN"
  mobile_readonly: true              # 手机端只读（§收敛信号 2）
```

---

## 五、脚本适配方案

所有脚本加一个 `--trader` 参数（默认 "default"）。核心变更是路径解析：

```python
# 通用路径解析（所有脚本共用）
import os
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

def get_trader_root(trader_id="default"):
    """获取交易员数据根目录。"""
    root = WORKSPACE / "traders" / trader_id
    if not root.exists():
        raise FileNotFoundError(f"交易员目录不存在: {root}")
    return root

def get_paths(trader_id="default"):
    """返回交易员的所有关键路径。"""
    root = get_trader_root(trader_id)
    return {
        "daily": root / "daily",
        "trades": root / "trades",
        "reviews": root / "reviews",
        "violations": root / "reviews" / "violations",
        "alerts": root / "reviews" / "alerts",
        "reconcile": root / "reviews" / "reconcile",
        "profile": root / "profile",
        "config": root / "config.yaml",
    }
```

Makefile 适配：

```makefile
TRADER ?= default

weekly-report: violations-scan
	@bash scripts/weekly_report.sh $(TRADER)

violations-scan:
	@python3 scripts/violations_scan.py --trader $(TRADER)

# 用法：make weekly-report TRADER=alice
```

---

## 六、WebUI Agent 的 Trader Context

Agent 在每次会话中绑定一个 trader context：

```
用户登录 → Auth 确定 trader_id → Agent 加载 trader context:
  - repo_path = /workspace/traders/{trader_id}/
  - config = traders/{trader_id}/config.yaml
  - templates = sigma/templates/ (共享)
  - knowledge = knowledge/ (共享)

Agent 的所有 file read/write 操作：
  - 只允许在 traders/{trader_id}/ 下写入
  - 可以读 sigma/templates/ 和 knowledge/（只读）
  - 不允许读/写其他 trader 的目录
```

---

## 七、迁移方案（从当前结构到新结构）

### 自动化迁移脚本（一次性执行）

```bash
# 1. 创建新目录结构
mkdir -p traders/default/{daily,trades,reviews/{weekly,monthly,violations,alerts,reconcile},profile}

# 2. 移动模板到 sigma/templates/
mkdir -p sigma/templates/reminders
mv sigma/pre-market.md sigma/templates/
mv sigma/post-trade-ema.md sigma/templates/
mv sigma/decision-chain.md sigma/templates/
mv sigma/weekly-review.md sigma/templates/
mv sigma/monthly-calibration.md sigma/templates/
mv sigma/ai-roles.md sigma/templates/
mv sigma/reminders/* sigma/templates/reminders/
rmdir sigma/reminders

# 3. 移动交易员数据到 traders/default/
mv sigma/daily/* traders/default/daily/ 2>/dev/null
mv trades/YYYY traders/default/trades/ 2>/dev/null
mv trades/TEMPLATE.md traders/default/trades/
mv trades/README.md traders/default/trades/
mv trades/SCREENSHOTS.md traders/default/trades/
# reviews/ 内容（如有生成的报告）
mv reviews/weekly/* traders/default/reviews/weekly/ 2>/dev/null
mv reviews/monthly/* traders/default/reviews/monthly/ 2>/dev/null
mv reviews/violations/* traders/default/reviews/violations/ 2>/dev/null
mv reviews/alerts/* traders/default/reviews/alerts/ 2>/dev/null
mv reviews/reconcile/* traders/default/reviews/reconcile/ 2>/dev/null

# 4. 移动 memory/ 到 profile/
mv memory/trader-profile.md traders/default/profile/
mv memory/bias-patterns.md traders/default/profile/
mv memory/stage.md traders/default/profile/

# 5. 清理旧目录
rm -rf sigma/daily trades/ reviews/ memory/
```

### 向后兼容

迁移后在根目录留 symlink（可选，过渡期后删除）：

```bash
ln -s traders/default/trades trades
ln -s traders/default/reviews reviews
```

---

## 八、与 design_proposal 的关系

本设计是 design_proposal_2026.md 的**补充**，不替代。具体关系：

| design_proposal 原条目 | 本文件的变更 |
|---|---|
| §3.1 目录结构 | 重构为 traders/{id}/ 分层 + sigma/templates/ 共享 |
| §3.2 工作流 | 不变（Agent 在 WebUI 中执行同样的工作流） |
| §3.2.3 后台强制 | 脚本加 --trader 参数 |
| §4 KPI | 按 trader 独立计算 |
| §5 退出协议 | 按 trader 独立触发 |
| §6 相容性 | 不受影响（数据底层仍是 markdown + git） |

---

## 附：修订记录

| 日期 | 版本 | 修订内容 |
|---|---|---|
| 2026-05-06 | v0.1 | 初版：多交易员目录结构 + config.yaml + 脚本适配 + WebUI Agent context + 迁移方案 |

---

*完成日期：2026-05-06 | 上游 Design：design_proposal_2026.md v0.1*
