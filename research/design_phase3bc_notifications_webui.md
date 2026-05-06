# Phase 3b/3c 详细设计 — 消息系统 + WebUI 渲染层 + 策略指标体系

> **位置**：本文件是 `design_proposal_2026.md` v0.1 §三.2.4（提醒层）+ §三.2.5（呈现层）的**工程级详细设计**。
>
> **输入**：design_proposal v0.1 §零（Phase 拆分总表）+ §二 D1/D4（入口形态 + 端策略）+ §三.2.3-2.5（后台强制 + 提醒 + 呈现）+ Phase 3a 已落地的 `scripts/` 基础设施。
>
> **当前版本**：v0.1（2026-05-06）
>
> **触发条件**：Phase 3b = v0 启动 4 周 P0 KPI 达标后；Phase 3c = v0.1 启动 8 周 KPI 持续达标后。**本设计先行产出，待触发条件满足后按此施工。**
>
> **v0.1 修订**：(1) 消息系统改为全自动定时推送（非手动 `make`）；(2) 新增 §七 策略/Setup 指标体系调研与设计。

---

## 一、消息系统（Phase 3b — 提醒 + 触发型通知）

### 1.1 设计目标

**全自动定时推送**——用户不需要手动跑任何 `make` 命令。系统自动在固定时间点完成：数据收集 → 分析/报告生成 → 推送到用户。

| 类型 | 含义 | 时机 | 示例 |
|------|------|------|------|
| **固定时刻提醒** | 每天/每周/每月的周期性 nudge | 可预测，定时 | "盘前规则书写时间到" |
| **定时批处理 + 推送** | 自动跑分析脚本 + 生成报告 + 推送结果 | 可预测，定时 | 周日 20:00 自动生成周报 + 推送摘要 |
| **触发型 alert** | 系统检测到异常后主动通知 | 不可预测 | "KPI 退化到 L4-warning" / "本周有 3 条违规" |

### 1.2 架构总览

```
┌──────────────────────────────────────────────────────────────────┐
│                        消息系统架构（全自动）                         │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ 调度层（cron / systemd timer / launchd）                    │    │
│  │                                                          │    │
│  │  08:30 盘前提醒                                            │    │
│  │  15:30 盘后 EMA 检查（有未填 EMA → 推送）                    │    │
│  │  周日 20:00 → 自动跑周报 + 违规扫描 + 推送摘要                │    │
│  │  月末 20:00 → 自动跑月校准 + KPI alert + 推送摘要            │    │
│  │  每日 21:00 → 检查是否有未 acknowledge alert → 推送          │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                         │ 触发                                    │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ 执行层                                                     │    │
│  │ • scripts/sigma_scheduler.py（统一调度入口）                  │    │
│  │   ├─ weekly_report.sh → AI 周报生成                         │    │
│  │   ├─ violations_scan.py → 违规扫描                          │    │
│  │   ├─ kpi_alert.py → KPI 退化检测                            │    │
│  │   ├─ reconcile_funds.py → 训练资金对账                       │    │
│  │   └─ inject_banner.py → Banner 注入                         │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                         │ 结果                                    │
│                         ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │ 推送层                                                     │    │
│  │ • 邮件 (SMTP) — 周报摘要 / 违规通知 / KPI alert             │    │
│  │ • 桌面通知 (osascript / notify-send) — 盘前/盘后提醒        │    │
│  │ • 文件 Banner — 未确认 alert 时 daily/ 顶部                 │    │
│  │ • macOS/iOS 日历 — 固定时刻提醒（辅助通道）                   │    │
│  └──────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

**核心改变**：用户不再需要手动 `make weekly-report`。系统自己在周日 20:00 跑完所有分析 → 生成报告 → commit → 推送邮件摘要给你。你只需要**打开邮件看结果 + 去仓库里 acknowledge**。

### 1.3 全自动调度 — 详细规格

#### 1.3.1 调度时间表（全部自动执行，无需手动触发）

| # | 时间 | 自动执行内容 | 推送内容 |
|---|------|-------------|----------|
| 1 | 工作日 08:30 | 检查昨日是否有未填 EMA 的已平仓交易 | 桌面通知"盘前规则书写时间到" + 未填 EMA 提醒 |
| 2 | 工作日 09:15 | — | 桌面通知"9:20 集合竞价将至" |
| 3 | 工作日 15:30 | 检查今日 trades/ 是否有新平仓但没 EMA | 桌面通知"盘后 EMA 截止" |
| 4 | **每日 21:00** | 检查未 acknowledge alert + 注入 Banner | 如有未处理 alert → 邮件提醒 |
| 5 | **周日 20:00** | **自动执行**：violations_scan → weekly_report → 策略指标计算 → git commit | 邮件推送**周报摘要**（KPI + 违规 + 策略表现） |
| 6 | **月末 20:00** | **自动执行**：monthly_calibration → kpi_alert → reconcile_funds → git commit | 邮件推送**月报摘要**（KPI 趋势 + 退化判定 + 策略复盘） |

#### 1.3.2 实现方式：统一调度器

**核心组件**：`scripts/sigma_scheduler.py`

```python
# 统一调度入口 — 一个脚本处理所有定时任务
# 安装到 cron / systemd / launchd 后完全无人值守

SCHEDULE = {
    "pre_market_remind": {"cron": "30 8 * * 1-5", "action": "remind_pre_market"},
    "auction_remind":    {"cron": "15 9 * * 1-5", "action": "remind_auction"},
    "post_close_check":  {"cron": "30 15 * * 1-5", "action": "check_ema_pending"},
    "daily_alert_check": {"cron": "0 21 * * *",    "action": "check_pending_alerts"},
    "weekly_auto":       {"cron": "0 20 * * 0",    "action": "run_weekly_full"},
    "monthly_auto":      {"cron": "0 20 L * *",    "action": "run_monthly_full"},
}
```

`run_weekly_full` 自动执行的完整流程：

```
1. violations_scan.py → reviews/violations/YYYY-WW.md
2. weekly_report.sh → reviews/weekly/YYYY-WW-auto.md（调 LLM API）
3. strategy_metrics.py → reviews/weekly/YYYY-WW-metrics.md（策略指标）
4. inject_banner.py → 更新 daily/ banner
5. git add + commit "auto(weekly): YYYY-WW"
6. send_alert_email.py → 邮件推送周报摘要
```

#### 1.3.3 安装方式（一键）

```bash
# 安装全自动调度（执行一次即可）
make install-scheduler

# 等同于：
# macOS: 安装 launchd plist 到 ~/Library/LaunchAgents/
# Linux: 安装 systemd timer 或写入 crontab
```

`scripts/install_scheduler.sh`：

```bash
#!/usr/bin/env bash
WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS: launchd
    PLIST="$HOME/Library/LaunchAgents/com.sigma.scheduler.plist"
    cat > "$PLIST" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" ...>
<plist version="1.0"><dict>
  <key>Label</key><string>com.sigma.scheduler</string>
  <key>ProgramArguments</key><array>
    <string>python3</string>
    <string>${WORKSPACE}/scripts/sigma_scheduler.py</string>
    <string>--daemon</string>
  </array>
  <key>StartInterval</key><integer>60</integer>
  <key>RunAtLoad</key><true/>
</dict></plist>
EOF
    launchctl load "$PLIST"
    echo "σ 调度器已安装（launchd）。开机自动运行。"
else
    # Linux: crontab
    (crontab -l 2>/dev/null; echo "* * * * * python3 ${WORKSPACE}/scripts/sigma_scheduler.py --tick") | crontab -
    echo "σ 调度器已安装（crontab）。每分钟检查是否有待执行任务。"
fi
```

#### 1.3.4 日历辅助通道（补充，非必须）

提供 `.ics` 文件作为**备份通道**（万一电脑关机，手机日历仍会响）：

```
sigma/reminders/sigma-calendar.ics
```

五条重复事件与 §1.3.1 时间表对应。用户双击导入 macOS/iOS 日历即可。

#### 1.3.5 LLM API 自动调用（周报/月报生成）

当前 `weekly_report.sh` 需要手动复制 prompt。全自动版本直接调 API：

```python
# scripts/llm_call.py — 调用 LLM 生成周报
import os
import requests

def call_llm(prompt: str) -> str:
    """调用 LLM API 生成报告。支持 OpenAI / Claude / 本地模型。"""
    api_key = os.environ.get("SIGMA_LLM_API_KEY")
    base_url = os.environ.get("SIGMA_LLM_BASE_URL", "https://api.openai.com/v1")
    model = os.environ.get("SIGMA_LLM_MODEL", "gpt-4o")

    resp = requests.post(f"{base_url}/chat/completions", headers={
        "Authorization": f"Bearer {api_key}",
    }, json={
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
    })
    return resp.json()["choices"][0]["message"]["content"]
```

配置（`~/.sigma/config.yaml`）：

```yaml
llm:
  api_key: ${SIGMA_LLM_API_KEY}  # 环境变量
  base_url: https://api.openai.com/v1  # 或 Claude / 本地
  model: gpt-4o

email:
  smtp_host: smtp.example.com
  smtp_port: 587
  from: sigma@example.com
  to: user@example.com
```

### 1.4 触发型 Alert — 详细规格

#### 1.4.1 触发源（已有基础设施）

| 触发源 | 脚本 | 产出 |
|--------|------|------|
| KPI 退化 | `scripts/kpi_alert.py` | `reviews/alerts/YYYY-MM-DD-alert.md` |
| 违规扫描 | `scripts/violations_scan.py` | `reviews/violations/YYYY-WW.md` |
| 训练资金对账异常 | `scripts/reconcile_funds.py`（待建） | `reviews/reconcile/YYYY-WW.md` |

#### 1.4.2 通知通道

**通道 1：邮件推送（主通道）**

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ 脚本检测到异常  │ →  │ 生成 alert 文件 │ →  │ 发送邮件通知   │
└──────────────┘    └──────────────┘    └──────────────┘
```

实现：`scripts/send_alert_email.py`

```python
# 核心逻辑（伪代码）
import smtplib
from email.mime.text import MIMEText
from pathlib import Path
import yaml

def send_alert(alert_path: Path, config: dict):
    content = alert_path.read_text()
    msg = MIMEText(content, "plain", "utf-8")
    msg["Subject"] = f"[σ Alert] {extract_title(content)}"
    msg["From"] = config["from"]
    msg["To"] = config["to"]

    with smtplib.SMTP(config["smtp_host"], config["smtp_port"]) as s:
        s.starttls()
        s.login(config["smtp_user"], config["smtp_pass"])
        s.send_message(msg)
```

配置文件：`~/.sigma/notify.yaml`（不入 git）

```yaml
email:
  smtp_host: smtp.example.com
  smtp_port: 587
  smtp_user: user@example.com
  smtp_pass: ${SIGMA_SMTP_PASS}  # 环境变量
  from: sigma-system@example.com
  to: user@example.com
```

**通道 2：文件 Banner（兜底——确保用户必经路径看到）**

即使邮件失败/被忽略，用户每次打开 `sigma/daily/` 写盘前规则时会看到 banner：

```
⚠ σ 有未确认的 alert：reviews/alerts/2026-05-20-alert.md
```

实现方式：`scripts/inject_banner.py`（周复盘/月校准跑完后自动执行）

- 扫描 `reviews/alerts/` 中未 acknowledge 的文件（`- [ ]` 还在）
- 如果有，在当天的 `sigma/daily/` 模板顶部注入 banner
- 用户 acknowledge 后（checkbox 改为 `- [x]`），下次执行时移除 banner

**通道 3：系统桌面通知（辅助）**

与固定时刻提醒共用 `scripts/notify.sh`，在脚本检测到异常时直接弹通知。

#### 1.4.3 通知内容模板

```markdown
# [σ Alert] KPI 退化警告 — 2026-05-20

**级别**：L4-warning
**触发**：盘前规则完成率 65%（< 80% 阈值）

## 需要你做的

1. 打开 reviews/alerts/2026-05-20-alert.md
2. 阅读 KPI 数据
3. 在 acknowledge 区域填写你的决定

## 一句话

如果你选择不 acknowledge，下次写盘前规则时顶部会有 banner 提醒。
```

#### 1.4.4 通知频率控制（防 fatigue）

| 规则 | 逻辑 |
|------|------|
| 同类 alert 去重 | 同一周内同一 level 只发一次邮件 |
| 每日邮件上限 | 最多 1 封/天（多条合并为单封摘要） |
| 静默时段 | 22:00-07:00 不发邮件（本地 cron 控制） |
| 降级策略 | 连续 3 次邮件未 acknowledge → 仅保留文件 banner（用户主动忽略 = 退化路径触发条件之一） |

### 1.5 消息系统 — 文件结构

```
sigma/reminders/
├── sigma-calendar.ics          ← 5 条日历事件的 ICS 导入文件
├── README.md                    ← 使用说明（如何导入 + 如何配置邮件）
└── cron-examples.md             ← cron 示例（方案 B 用户）

scripts/
├── notify.sh                    ← 跨平台桌面通知（已有通知逻辑复用）
├── send_alert_email.py          ← 邮件发送
├── inject_banner.py             ← 未 acknowledge alert 时注入 daily/ banner
└── ... (已有：kpi_alert.py / violations_scan.py)
```

### 1.6 消息系统 — 集成到 Makefile

```makefile
# 新增 targets
notify-setup: ## 显示通知配置指引
	@echo "=== σ 通知配置 ==="
	@echo "1. 导入日历事件：open sigma/reminders/sigma-calendar.ics"
	@echo "2. 配置邮件：cp sigma/reminders/notify.yaml.example ~/.sigma/notify.yaml"
	@echo "3. 设置 cron（可选）：crontab -e 参考 sigma/reminders/cron-examples.md"

weekly-report: violations-scan inject-banner ## 周末：AI 周读 + 违规扫描 + banner 检查
	@bash scripts/weekly_report.sh
	@python3 scripts/send_alert_email.py --check-pending || true

inject-banner: ## 检查未确认 alert 并注入 banner
	@python3 scripts/inject_banner.py
```

### 1.7 消息系统 — 工程量估算

| 组件 | 工时 | 依赖 |
|------|------|------|
| `scripts/sigma_scheduler.py`（统一调度器） | 3h | Python |
| `scripts/llm_call.py`（API 自动调用） | 2h | LLM API key |
| `scripts/send_alert_email.py`（邮件推送） | 2h | SMTP 配置 |
| `scripts/inject_banner.py`（Banner 注入） | 2h | 无 |
| `scripts/notify.sh`（桌面通知） | 0.5h | 无 |
| `scripts/install_scheduler.sh`（一键安装） | 1.5h | launchd/cron |
| `sigma/reminders/sigma-calendar.ics` | 0.5h | 无 |
| `~/.sigma/config.yaml` 模板 + README | 1h | 无 |
| Makefile 集成 + 端到端测试 | 1.5h | 上述全部 |
| **总计** | **~14h** | |

---

## 二、WebUI 渲染层（Phase 3c — Read-Only Dashboard）

### 2.1 设计目标

在**不改变数据底层**（仍是 markdown + git）的前提下，提供一个**视觉化的只读界面**，让复盘体验从"读 markdown 文件"升级为"看 dashboard"。

**不做的事**：
- 不做 write 功能（写入仍在 Cursor + markdown）
- 不做用户认证（本地运行 / 私有部署）
- 不做 SaaS 化
- 不引入数据库（所有数据实时从 markdown 解析）

### 2.2 技术选型

| 候选 | 优势 | 劣势 | 判定 |
|------|------|------|------|
| **Vite + Vue/React SPA** | 灵活、现代前端栈、热更新 | 需维护 node_modules | **采纳**（Vite + Vue 3） |
| MkDocs Material | 零配置 markdown 渲染 | 不适合 dashboard / 图表 | 拒绝（更适合文档站） |
| Quartz (Obsidian publish) | 漂亮的 note graph | 依赖 Obsidian 生态 | 拒绝（用户不用 Obsidian） |
| Python Flask/FastAPI | 用户熟悉 Python 生态 | 需要后端进程 + 模板 | 备选 |

**最终选择：Vite + Vue 3 + Tailwind CSS + Chart.js**

理由：
- 用户可以 `npm run dev` 一键启动本地 dashboard
- 纯静态前端，不需要后端进程
- 数据通过读取 markdown 文件（build 时解析 / dev 时 watch）
- 部署简单：可 `npm run build` 后用 GitHub Pages 私有仓库 serve

### 2.3 架构

```
┌─────────────────────────────────────────────────────────────┐
│                     WebUI 架构                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────┐                                          │
│  │ Markdown 数据层 │  trades/*.md / reviews/*.md / sigma/*    │
│  └───────┬───────┘                                          │
│          │ build 时解析 (gray-matter + remark)                │
│          ▼                                                  │
│  ┌───────────────┐                                          │
│  │ JSON 数据文件    │  webui/src/data/ (auto-generated)        │
│  │ • trades.json │                                          │
│  │ • kpis.json   │                                          │
│  │ • weekly.json │                                          │
│  └───────┬───────┘                                          │
│          │ import                                            │
│          ▼                                                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │ Vue 3 SPA                                              │  │
│  │                                                        │  │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌────────────┐  │  │
│  │  │Dashboard│ │ Trades  │ │ Weekly  │ │Screenshots │  │  │
│  │  │ (Home)  │ │  List   │ │ Review  │ │  Gallery   │  │  │
│  │  └─────────┘ └─────────┘ └─────────┘ └────────────┘  │  │
│  │                                                        │  │
│  │  渲染：Chart.js 图表 + Tailwind 卡片                     │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2.4 数据流水线

```
┌──────────────────────────────────────────────────────┐
│ scripts/build_webui_data.py                           │
│                                                      │
│ 输入：                                                │
│   trades/YYYY/MM/*.md        → 解析 frontmatter      │
│   reviews/weekly/*-auto.md   → 提取 KPI 数字          │
│   reviews/violations/*.md    → 提取违规计数            │
│   reviews/alerts/*.md        → 提取 alert 状态        │
│   trades/YYYY/MM/screenshots/* → 列出截图路径          │
│                                                      │
│ 输出：                                                │
│   webui/src/data/trades.json                         │
│   webui/src/data/kpis.json                           │
│   webui/src/data/weekly_reports.json                  │
│   webui/src/data/violations.json                     │
│   webui/src/data/screenshots.json                    │
│                                                      │
│ 触发：                                                │
│   • make build-webui-data (手动)                      │
│   • git hook post-commit (自动，可选)                  │
│   • Vite dev server watch mode (开发时)               │
└──────────────────────────────────────────────────────┘
```

### 2.5 页面设计

#### 2.5.1 Dashboard（首页）

```
┌────────────────────────────────────────────────────────────┐
│  σ Dashboard                                    2026-05    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ 盘前完成率  │  │ EMA完成率  │  │ 决策链完整率 │  │ 本月盈亏   │  │
│  │   85%    │  │   72%    │  │   92%    │  │  +¥1,200 │  │
│  │  ▓▓▓▓░   │  │  ▓▓▓░░   │  │  ▓▓▓▓░   │  │   ↑12%  │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│                                                            │
│  ┌────────────────────────────────┐  ┌─────────────────┐  │
│  │ KPI 趋势（折线图 · 最近 8 周）      │  │ 本周违规          │  │
│  │                                │  │                 │  │
│  │  100% ─┐                       │  │ • 止损穿越 ×1    │  │
│  │        │  ╱╲    ╱╲             │  │ • 决策链跳过 ×0  │  │
│  │   80% ─┤╱  ╲──╱  ╲──          │  │                 │  │
│  │        │                       │  │ 待 acknowledge  │  │
│  │   60% ─┤                       │  │ → alerts/05-18  │  │
│  │        └───────────────────    │  │                 │  │
│  │        W18 W19 W20 W21 W22     │  └─────────────────┘  │
│  └────────────────────────────────┘                        │
│                                                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │ 最近交易                                              │    │
│  │ 日期        标的        方向   盈亏    决策链  EMA      │    │
│  │ 2026-05-18  MGC 06    long  +¥400   ✓      ✓       │    │
│  │ 2026-05-15  MGC 06    short -¥200   ✓      ✗       │    │
│  │ 2026-05-12  沪深300ETF  long  +¥150   ✓      ✓       │    │
│  └────────────────────────────────────────────────────┘    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

#### 2.5.2 Trades（交易列表）

| 功能 | 描述 |
|------|------|
| 列表视图 | 按时间倒序排列所有交易，显示 frontmatter 关键字段 |
| 筛选器 | 按 symbol / direction / product_class / 日期范围 |
| 单笔详情 | 点击展开：完整决策链内容 + EMA + 截图缩略图 |
| 统计摘要 | 顶部卡片：总笔数 / 胜率 / 平均盈亏 / 最大回撤 |

#### 2.5.3 Weekly Review（周报可视化）

| 功能 | 描述 |
|------|------|
| AI 报告渲染 | 将 `reviews/weekly/*-auto.md` 渲染为格式化卡片 |
| 违规详情 | 嵌入当周 `reviews/violations/` 内容 |
| 对比视图 | 本周 vs 上周 KPI 变化（颜色标注） |
| 历史回溯 | 左右切换周次 |

#### 2.5.4 Screenshots（截图画廊）

| 功能 | 描述 |
|------|------|
| 时间线视图 | 按交易日期排列截图，entry / exit / context 分组 |
| 对照视图 | 同一笔交易的 entry + exit 截图并排显示 |
| 放大查看 | 点击截图全屏 lightbox |
| 关联交易 | 每张截图旁标注对应 trade 文件链接 |

**这是截图系统的核心复盘价值——"当时你看到了什么 vs 后来发生了什么"可视化对照**：

```
┌────────────────────────────────────────────────────┐
│  2026-05-18 MGC 202606 Long                        │
│                                                    │
│  ┌─────────────────┐    ┌─────────────────┐       │
│  │   ENTRY 截图      │    │   EXIT 截图       │       │
│  │                  │    │                  │       │
│  │  [K线图 + 入场位]  │ →  │  [K线图 + 出场位]  │       │
│  │                  │    │                  │       │
│  └─────────────────┘    └─────────────────┘       │
│                                                    │
│  决策链摘要：论据 = xxx，止损 = 2145，EV = +¥80       │
│  结果：盈 +¥400，按计划执行：是                        │
│  偏差：无                                           │
└────────────────────────────────────────────────────┘
```

#### 2.5.5 KPI（绩效指标页）

| 功能 | 描述 |
|------|------|
| 仪表盘 | 三个 P0 KPI 的当前值 + 阈值线 |
| 趋势图 | 最近 12 周 KPI 折线图 |
| 退化路径可视化 | 当前 Level（L4/L3/L2/L1）+ 下一退化触发条件 |
| 校准指标 | 预估胜率 vs 实际胜率散点图（月度更新） |

### 2.6 技术实现细节

#### 2.6.1 项目结构

```
webui/
├── package.json
├── vite.config.ts
├── tailwind.config.js
├── index.html
├── src/
│   ├── main.ts
│   ├── App.vue
│   ├── router/
│   │   └── index.ts          ← Vue Router（Dashboard/Trades/Weekly/Screenshots/KPI）
│   ├── components/
│   │   ├── KpiCard.vue        ← 单个 KPI 指标卡片
│   │   ├── KpiTrend.vue       ← KPI 折线图（Chart.js）
│   │   ├── TradeList.vue      ← 交易列表 + 筛选
│   │   ├── TradeDetail.vue    ← 单笔交易详情（含截图）
│   │   ├── WeeklyReport.vue   ← 周报渲染
│   │   ├── ScreenshotGallery.vue ← 截图画廊
│   │   ├── AlertBanner.vue    ← 未确认 alert 提示
│   │   └── ViolationList.vue  ← 违规列表
│   ├── composables/
│   │   ├── useTradeData.ts    ← 加载 + 计算交易数据
│   │   └── useKpiData.ts      ← 加载 + 计算 KPI
│   ├── data/                   ← build 时自动生成（不入 git）
│   │   ├── trades.json
│   │   ├── kpis.json
│   │   ├── weekly_reports.json
│   │   ├── violations.json
│   │   └── screenshots.json
│   └── assets/
│       └── tailwind.css
├── scripts/
│   └── build_data.py          ← Markdown → JSON 转换器
└── README.md
```

#### 2.6.2 数据解析器（`scripts/build_data.py`）

核心职责：将 markdown frontmatter + 内容解析为 JSON。

```python
# 伪代码 — trades.json 生成逻辑
def parse_trades():
    trades = []
    for md_file in glob("trades/????/??/*.md"):
        if md_file.name in ("TEMPLATE.md", "README.md", "SCREENSHOTS.md"):
            continue
        fm = parse_frontmatter(md_file)
        content = parse_content(md_file)
        trades.append({
            "id": md_file.stem,
            "date": fm.get("date"),
            "symbol": fm.get("symbol"),
            "direction": fm.get("direction"),
            "product_class": fm.get("product_class"),
            "market": fm.get("market"),
            "entry_price": fm.get("entry_price"),
            "exit_price": fm.get("exit_price"),
            "pnl_net": fm.get("pnl_net"),
            "stop_loss_price": fm.get("stop_loss_price"),
            "has_decision_chain": check_decision_chain(content),
            "has_ema": check_ema(content),
            "screenshots": find_screenshots(md_file),
        })
    return sorted(trades, key=lambda t: t["date"], reverse=True)
```

#### 2.6.3 开发 & 运行方式

```bash
# 首次设置
cd webui && npm install

# 开发模式（hot reload + 自动 rebuild data）
npm run dev
# → 浏览器打开 http://localhost:5173

# 生产构建
npm run build
# → dist/ 可以用 GitHub Pages 或任何静态托管

# 仅更新数据（不重启 dev server）
npm run build:data
# 等同于：python3 scripts/build_data.py
```

#### 2.6.4 截图显示方案

截图在仓库中是相对路径（`trades/2026/05/screenshots/*.png`）。WebUI 中显示方式：

- **Dev mode**：Vite 配置 `publicDir` 指向仓库根目录的 `trades/`，截图路径直接可访问
- **Build mode**：`build_data.py` 将截图拷贝到 `webui/dist/screenshots/` 下（或生成软链接）
- **data JSON**：`screenshots.json` 记录每张截图的 `{ tradeId, type, seq, path }`

```typescript
// vite.config.ts
export default defineConfig({
  server: {
    fs: {
      allow: ['..']  // 允许 dev server 访问仓库根目录
    }
  }
})
```

### 2.7 WebUI — 设计约束

| 约束 | 来源 | 实现 |
|------|------|------|
| Read-only | design_proposal D1 | 无任何写入接口；数据修改必须回 Cursor + git |
| 数据底层不变 | design_proposal D3 | 所有数据仍是 markdown + git；WebUI 只是渲染层 |
| 无 SaaS lock-in | notes/08 caveat | 纯本地运行；可选 GitHub Pages 私有部署 |
| 无 gamification | notes/06 Q3 | 无积分/徽章/排行榜；纯信息呈现 |
| 4 周不用就关 | design_proposal §零.3 | 退化路径：WebUI 上线 4 周后用户不打开 → 关掉 |

### 2.8 WebUI — 工程量估算

| 组件 | 工时 | 依赖 |
|------|------|------|
| 项目脚手架（Vite + Vue 3 + Tailwind） | 2h | Node.js |
| `scripts/build_data.py` 数据解析器 | 4h | Python gray-matter |
| Dashboard 页面（KPI 卡片 + 趋势图） | 4h | Chart.js |
| Trades 列表 + 详情 | 3h | 数据解析器 |
| Weekly Review 渲染 | 2h | 数据解析器 |
| Screenshots 画廊 + 对照视图 | 3h | 截图路径解析 |
| KPI 绩效页 | 2h | Chart.js |
| Makefile 集成 + README | 1h | — |
| **总计** | **~21h** | |

### 2.9 WebUI — 未来扩展路径（Phase 3d 评估）

| 扩展 | 触发条件 | 工时 |
|------|----------|------|
| 部署到 GitHub Pages 私有 | 手机查看周报需求强烈 | +2h |
| 增加月度校准可视化 | 月校准数据累积 ≥ 3 月 | +3h |
| 增加行为偏误热力图 | 违规数据累积 ≥ 8 周 | +4h |
| 增加 AI 周报对话式展开 | 用户反馈"想在 WebUI 里追问 AI" | +8h（需后端） |

---

## 三、两系统的集成关系

```
┌─────────────────────────────────────────────────────────────────────┐
│                          集成全景                                     │
│                                                                     │
│   用户日常操作（Cursor + git）                                         │
│      │                                                              │
│      ▼                                                              │
│   trades/*.md + sigma/daily/*.md                                    │
│      │                                                              │
│      │  ┌────────────────────────────────────────────────────┐      │
│      │  │ sigma_scheduler.py（全自动，后台常驻）                 │      │
│      │  │                                                    │      │
│      │  │  周日 20:00 自动执行：                                │      │
│      │  │    violations_scan.py                              │      │
│      │  │    → llm_call.py（AI 生成周报）                      │      │
│      │  │    → strategy_metrics.py（策略指标）                  │      │
│      │  │    → git commit                                    │      │
│      │  │    → send_alert_email.py（推送邮件摘要）              │      │
│      │  │                                                    │      │
│      │  │  每日 08:30/09:15/15:30 桌面通知                     │      │
│      │  │  每日 21:00 检查未确认 alert → 邮件                   │      │
│      │  └─────────────────────┬──────────────────────────────┘      │
│      │                        │                                     │
│      │                        ▼                                     │
│      │         ┌──────────────────────────────┐                     │
│      │         │ 产出：                         │                     │
│      │         │ reviews/weekly/*-auto.md      │                     │
│      │         │ reviews/weekly/*-metrics.md   │                     │
│      │         │ reviews/violations/*.md       │                     │
│      │         │ reviews/alerts/*.md           │                     │
│      │         └──────────────┬───────────────┘                     │
│      │                        │                                     │
│      └────────────────────────┼─────────────────────────────┐       │
│                               │                             │       │
│                               ▼                             ▼       │
│              ┌─────────────────────────┐   ┌─────────────────────┐  │
│              │ 消息推送（自动）           │   │ WebUI（按需打开）      │  │
│              │ • 邮件：周报/月报/alert   │   │ • Dashboard + KPI   │  │
│              │ • 桌面通知：盘前/盘后     │   │ • Trades + 截图      │  │
│              │ • Banner：daily/ 顶部    │   │ • Strategy（筛选）   │  │
│              └─────────────────────────┘   └─────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 关键原则

1. **全自动**——用户只需要写 markdown + git commit；所有分析/报告/推送自动发生
2. **消息系统是"推"**（主动通知你 + 推送分析结果）—— Phase 3b
3. **WebUI 是"拉"**（你主动来看 dashboard + 策略筛选）—— Phase 3c
4. **两者都不写数据**——写入路径唯一性在 Cursor + git
5. **两者都可关掉**——消息系统关 = 回到纯自律；WebUI 关 = 回到读 markdown

---

## 四、实施时间线

| 阶段 | 触发条件 | 交付 |
|------|----------|------|
| **Phase 3b-1** | v0 运行 4 周 P0 达标 | 全自动调度器 + 消息推送：sigma_scheduler + llm_call + send_alert_email + inject_banner + notify.sh + install_scheduler |
| **Phase 3b-2** | Phase 3b-1 后 1 周 | 策略指标计算 + 训练资金对账：strategy_metrics.py + reconcile_funds.py |
| **Phase 3c-1** | v0.1 运行 8 周 KPI 达标 | WebUI 骨架：Vite + Vue 3 + build_data.py + Dashboard 页 |
| **Phase 3c-2** | Phase 3c-1 后 2 周 | WebUI 完整：Trades + Weekly + Screenshots + Strategy + KPI 五页 |
| **Phase 3c-3** | 用户需求 | GitHub Pages 私有部署（手机看周报） |

---

## 五、风险与缓解

| 风险 | 概率 | 缓解 |
|------|------|------|
| SMTP 配置对非技术用户有门槛 | 低（用户是 git 用户） | 提供详细 README + 支持 Gmail App Password |
| WebUI 增加维护负担 | 中 | 4 周不用即关；数据层不变所以关掉无损 |
| 通知频率导致疲劳 | 中 | 频率控制规则（§1.4.4）+ 静默时段 |
| 截图体积增长 | 低（v0 交易频率低） | 预留 Git LFS 迁移路径；WebUI build 时可压缩 |
| Node.js 环境依赖 | 低 | `package.json` 锁版本；可选 Docker 运行 |

---

## 六、决策记录

| 决策 | 选择 | 拒绝候选 | 理由 |
|------|------|----------|------|
| 固定提醒通道 | ICS 日历导入 | Telegram bot / 微信 | 零依赖 + 原生跨设备；Telegram/微信有反向证据 |
| 触发通知通道 | 邮件 SMTP | Webhook / 微信 | 跨平台 + 可靠 + 用户已有邮箱 |
| WebUI 框架 | Vite + Vue 3 | MkDocs / Flask / Next.js | 轻量 SPA + 热更新 + 不需要后端 |
| 数据解析 | Python 脚本 build 时生成 JSON | 运行时 markdown 解析 | 性能好 + 前端不依赖 markdown parser |
| 截图显示 | Vite dev server fs.allow | 复制到 public/ | 避免重复存储；dev 时直接引用原文件 |
| 部署 | 默认本地；可选 GitHub Pages | Vercel / Netlify | 私有数据不适合公开平台；GH Pages 支持私有仓库 |

---

## 七、策略/Setup 指标体系 — 调研与设计

### 7.1 调研问题

当前 σ 系统只追踪**行为合规指标**（盘前完成率、EMA 完成率、决策链完整率）。用户提出：是否应该追踪**策略表现指标**（夏普率、胜率、期望值、按 setup 筛选等）？

### 7.2 调研结论

**结论：应该追踪，但有严格的样本量诚实约束。**

#### 7.2.1 支持追踪的证据

| 证据 | 等级 | 含义 |
|------|------|------|
| Profit Factor by Setup 是诊断的关键（trading-journals.com 综合） | M/W | 账户级 profit factor 无法诊断；按 setup 拆分才能发现"哪个策略拖后腿" |
| Expectancy 是证明 edge 存在的基础指标（行业共识） | M | 没有 expectancy 就无法回答"我的交易系统有正期望值吗" |
| 处置效应人为膨胀胜率（SSRN 4636623, 2024）| S | 真实胜率 47% 被处置效应膨胀到 52%——如果只看胜率会系统性高估自己 |
| Setup-specific 追踪能发现"A+ trade 贡献大部分利润"（ACY 2025 综合） | M/W | 职业交易台用 setup quality scoring 区分 A+/B/C 级交易 |
| 市场环境条件化：setup 往往只在特定 regime 下有效 | M | 需要按 trending/ranging/high-vol 分类统计 |

#### 7.2.2 样本量硬约束（**必须诚实标注**）

| 胜率假设 | 95% 置信需要的交易笔数 | 含义 |
|---------|----------------------|------|
| 52% | ~2,400 笔 | 接近随机的策略几乎不可能在小样本中被证伪 |
| 55% | ~380 笔 | 中等 edge 需要大半年到一年 |
| 60% | ~95 笔 | 较强 edge 约 3-6 个月可初步验证 |

**关键发现**：

- Profit Factor 在 20 笔交易时提供的信息极少，需要 100+ 笔才稳定（CrossTrade 分析）
- 55% 真实胜率在 30 笔交易中有 **40% 的概率看起来不赚钱**（M1NDTR8DE 统计模拟）
- Sharpe Ratio 在小样本下极不可靠，自相关结构进一步恶化（Ledoit & Wolf 2008）
- 500 笔交易跨 6 个月（单一 regime）不如 100 笔交易跨 5 年（多 regime）

**对 σ 系统的硬约束**：

> 当 setup 样本量 < 30 笔时，**所有策略指标必须标注"U 级 / 可能是噪音 / n=___"**。这与 foundation §三.5（样本量诚实）+ ai-roles.md 第 5 条 prompt 约束完全一致。

#### 7.2.3 应该追踪的指标（分层）

**Layer 1：每笔交易自动计算（≥ 1 笔即可计算，但意义随 n 增长）**

| 指标 | 公式 | 所需数据 |
|------|------|----------|
| **R 倍数** | (exit - entry) / (entry - stop) | entry_price, exit_price, stop_loss_price |
| **实际风险金额** | position_size × abs(entry - stop) | position_size, entry_price, stop_loss_price |
| **持仓时间** | exit_date - entry_date | 日期 |

**Layer 2：累计指标（≥ 10 笔可初看趋势，≥ 30 笔初步可信，≥ 100 笔稳定）**

| 指标 | 公式 | 诚实标注 |
|------|------|----------|
| **胜率** | win_count / total_count | n < 30 时标"U 级噪音" |
| **期望值 (Expectancy)** | (win_rate × avg_win_R) - (loss_rate × avg_loss_R) | 核心！证明 edge 存在与否 |
| **Profit Factor** | gross_profit / gross_loss | < 1.0 = 无 edge；1.2-2.0 = 现实区间；> 3.0 = 可能过拟合 |
| **平均 R 倍数** | sum(R) / n | 正 = 每笔平均赚多少 R |
| **最大连续亏损** | max consecutive losses | 用于止损心理准备 |
| **最大回撤** | max drawdown from equity peak | 直觉理解风险 |

**Layer 3：高级指标（≥ 50 笔 + 跨 regime 才有意义）**

| 指标 | 公式 | 诚实标注 |
|------|------|----------|
| **Sharpe Ratio** | mean(R) / std(R) × sqrt(252) | 年化；n < 50 时极不可靠 |
| **Sortino Ratio** | mean(R) / downside_std × sqrt(252) | 只惩罚下行波动 |
| **Calmar Ratio** | annual_return / max_drawdown | 需要 ≥ 6 个月数据 |
| **Recovery Factor** | net_profit / max_drawdown | |

#### 7.2.4 按 Setup 筛选 — 设计

**核心需求**：用户有不同的交易策略（setup），需要**分别追踪每个 setup 的表现**，判断哪个有 edge、哪个在拖后腿。

**实现方式**：在 trades/ frontmatter 中增加 `setup_tag` 字段。

```yaml
---
date: 2026-05-18
symbol: MGC-202606
direction: long
product_class: yellow-small-future
setup_tag: breakout-retest    # ← 新增：策略标签
stop_type: structure          # ← 新增：止损类型
target_type: fixed-rr         # ← 新增：止盈类型
target_rr: 2.0                # ← 新增：目标盈亏比
market_condition: trending    # ← 新增：当时市场状态
---
```

**字段设计**：

| 新字段 | 值域 | 用途 |
|--------|------|------|
| `setup_tag` | 用户自定义（如 `breakout-retest` / `mean-reversion` / `trend-follow`） | 按策略分组统计 |
| `stop_type` | `structure` / `atr` / `percent` / `time` | 按止损方式分组 |
| `target_type` | `fixed-rr` / `trailing` / `structure` / `time` | 按止盈方式分组 |
| `target_rr` | 数字（目标盈亏比） | 与实际 R 倍数对比 |
| `market_condition` | `trending` / `ranging` / `volatile` / `low-vol` | 按市场环境分组 |

**筛选维度**（WebUI + 周报都支持）：

```
按 setup_tag 筛选：
  "我的 breakout-retest 策略过去 20 笔表现如何？"
  → 胜率 55%、期望值 0.4R、profit factor 1.6（n=20，U 级）

按 stop_type 筛选：
  "ATR 止损 vs 结构止损，哪个让我的 R 倍数更好？"
  → ATR: avg_R = 0.8（n=12）vs Structure: avg_R = 1.2（n=15）

按 market_condition 筛选：
  "我在趋势市 vs 震荡市的表现差异"
  → trending: expectancy 0.6R vs ranging: expectancy -0.2R

交叉筛选：
  "breakout-retest + trending + structure-stop"
  → 这个具体组合的历史表现
```

### 7.3 与现有 σ 行为指标的关系

```
┌─────────────────────────────────────────────────────────────────┐
│                    指标体系全景                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  σ 行为指标（已有 · P0）          α 策略指标（新增 · P1）            │
│  ─────────────────────           ────────────────────            │
│  盘前规则完成率                    胜率（per setup）                │
│  EMA 完成率                       期望值 / Expectancy             │
│  决策链完整率                      Profit Factor                  │
│  止损遵守率                        平均 R 倍数                     │
│                                   最大回撤                       │
│  目的：管住自己                    目的：看懂策略                   │
│  判断：我有没有执行纪律             判断：我的策略有没有 edge         │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │ 交叉分析（最有价值）                                       │    │
│  │                                                         │    │
│  │ "我遵守决策链时 vs 违反时，expectancy 差多少？"              │    │
│  │ "止损遵守率高的那些笔 vs 穿越止损的那些笔，profit factor？" │    │
│  │ "连续亏损后我的 setup 选择质量是否下降？"                   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**最有价值的分析不是"策略指标本身"，而是"行为合规 × 策略表现"的交叉**。这能回答：
- "我的系统有 edge 吗？" → 期望值
- "我有没有在执行这个 edge？" → 合规率 × 策略表现对比
- "我的哪个 setup 值得继续？" → 按 setup 筛选 profit factor
- "我是因为策略问题还是执行问题在亏钱？" → 合规笔 vs 违规笔分别算 expectancy

### 7.4 策略指标 — 实现方案

#### 7.4.1 计算脚本

新增 `scripts/strategy_metrics.py`：

```python
# 核心逻辑：
# 1. 读取 trades/ 所有文件的 frontmatter
# 2. 计算 Layer 1-3 指标（全局 + 按 setup_tag 分组）
# 3. 输出 reviews/weekly/YYYY-WW-metrics.md
# 4. 输出 webui/src/data/strategy_metrics.json

def compute_metrics(trades, group_by=None, min_sample=5):
    """
    计算策略指标。
    group_by: None=全局, "setup_tag", "stop_type", "market_condition"
    min_sample: 低于此数量的分组标注 "U 级 / 样本不足"
    """
    results = {}
    for group_name, group_trades in group_trades_by(trades, group_by):
        n = len(group_trades)
        r_multiples = [t.r_multiple for t in group_trades if t.r_multiple is not None]

        metrics = {
            "n": n,
            "confidence": "U 级" if n < 30 else ("M 级" if n < 100 else "可信"),
            "win_rate": sum(1 for r in r_multiples if r > 0) / len(r_multiples),
            "expectancy": mean(r_multiples),
            "profit_factor": sum(r for r in r_multiples if r > 0) / abs(sum(r for r in r_multiples if r < 0)),
            "avg_r": mean(r_multiples),
            "max_consecutive_loss": max_consecutive(r_multiples, lambda r: r < 0),
            "max_drawdown": compute_drawdown(r_multiples),
        }

        if n >= 50:
            metrics["sharpe"] = mean(r_multiples) / std(r_multiples) * sqrt(252)
            metrics["sortino"] = mean(r_multiples) / downside_std(r_multiples) * sqrt(252)

        results[group_name] = metrics
    return results
```

#### 7.4.2 周报中的策略指标摘要

周报自动生成时，追加策略指标章节：

```markdown
## 策略表现（本周 + 累计）

### 全局（累计 n=45，U 级）

| 指标 | 值 | 备注 |
|------|----|----|
| 胜率 | 53% | n < 50，可能是噪音 |
| 期望值 | 0.35R | 正值，但置信度不足 |
| Profit Factor | 1.4 | 现实区间 |
| 平均 R | 0.35 | |
| 最大回撤 | -8.2% | |
| 最大连续亏损 | 5 笔 | |

### 按 Setup 分组

| Setup | n | 胜率 | 期望值 | PF | 置信度 |
|-------|---|------|--------|-----|--------|
| breakout-retest | 22 | 59% | 0.6R | 1.8 | U 级（n<30）|
| mean-reversion | 15 | 47% | 0.1R | 1.1 | U 级（n<30）|
| trend-follow | 8 | 50% | 0.3R | 1.3 | U 级（n<30）|

⚠ 所有分组 n < 30，上述数字仅供观察趋势，不可作为"策略有效/无效"的结论。
```

#### 7.4.3 WebUI 中的策略视图

在 WebUI 增加 **Strategy** 页面（第 6 页）：

| 功能 | 描述 |
|------|------|
| Setup 选择器 | 下拉选择 setup_tag → 展示该 setup 的所有指标 |
| 筛选面板 | setup_tag × stop_type × market_condition 交叉筛选 |
| R 倍数分布图 | 柱状图展示该 setup 所有交易的 R 分布 |
| Expectancy 趋势 | 滚动 20 笔 expectancy 折线图（看是否在改善） |
| 行为 × 策略交叉 | "合规笔 vs 违规笔"的 expectancy 对比 |
| 样本量警告 | n < 30 时大字标注"样本不足，仅供参考" |

#### 7.4.4 TEMPLATE.md 修改

在 trades/TEMPLATE.md frontmatter 中新增字段：

```yaml
setup_tag:           # 策略标签（如 breakout-retest / mean-reversion）
stop_type:           # 止损类型（structure / atr / percent / time）
target_type:         # 止盈类型（fixed-rr / trailing / structure / time）
target_rr:           # 目标盈亏比
market_condition:    # 市场状态（trending / ranging / volatile / low-vol）
```

### 7.5 策略指标 — 诚实约束（必须严格执行）

| 约束 | 内容 | 来源 |
|------|------|------|
| 样本量标注 | n < 30 标 "U 级"；n < 100 标"初步参考" | foundation §三.5 |
| 不做统计结论 | "这个 setup 的胜率是 60%（n=12）" ≠ "这个 setup 有效" | ai-roles.md §5 |
| Regime 警告 | 如果所有数据来自单一市场环境，必须标注"单 regime 数据" | 学术文献共识 |
| 过拟合警告 | Profit Factor > 3.0 或 Sharpe > 3.0 → 标"可能过拟合" | CrossTrade + 行业共识 |
| 处置效应校正 | 胜率统计时标注"含处置效应风险"——真实胜率可能低 2-5 个百分点 | SSRN 4636623 (2024) |

### 7.6 策略指标 — 何时启动

| 阶段 | 触发 | 内容 |
|------|------|------|
| **立即** | v0 TEMPLATE.md 更新 | frontmatter 增加 setup_tag 等字段（开始积累数据） |
| **Phase 3b** | 4 周 P0 达标 | strategy_metrics.py 上线 + 周报追加策略章节 |
| **Phase 3c** | 8 周 + 累计 ≥ 30 笔 | WebUI Strategy 页面 + 筛选功能 |
| **长期** | 累计 ≥ 100 笔 | 正式评估 setup edge 有效性；低于阈值的 setup 建议淘汰 |

---

## 八、修订记录

| 日期 | 版本 | 变更 |
|------|------|------|
| 2026-05-06 | v0 | 初版：消息系统 + WebUI 详细设计 |
| 2026-05-06 | v0.1 | (1) 消息系统改为全自动定时推送——`sigma_scheduler.py` 统一调度，用户不再需要手动 `make`；(2) 新增 §七 策略/Setup 指标体系（调研 + 设计）——支持按 setup_tag / stop_type / market_condition 筛选 |

---

*设计版本：v0.1 | 来源：design_proposal_2026.md v0.1 §三.2.4 + §三.2.5 + §零 Phase 拆分总表*
