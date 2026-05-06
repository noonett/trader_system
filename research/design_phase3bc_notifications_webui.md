# Phase 3b/3c 详细设计 — 消息系统 + WebUI 渲染层

> **位置**：本文件是 `design_proposal_2026.md` v0.1 §三.2.4（提醒层）+ §三.2.5（呈现层）的**工程级详细设计**。
>
> **输入**：design_proposal v0.1 §零（Phase 拆分总表）+ §二 D1/D4（入口形态 + 端策略）+ §三.2.3-2.5（后台强制 + 提醒 + 呈现）+ Phase 3a 已落地的 `scripts/` 基础设施。
>
> **当前版本**：v0（2026-05-06）
>
> **触发条件**：Phase 3b = v0 启动 4 周 P0 KPI 达标后；Phase 3c = v0.1 启动 8 周 KPI 持续达标后。**本设计先行产出，待触发条件满足后按此施工。**

---

## 一、消息系统（Phase 3b — 提醒 + 触发型通知）

### 1.1 设计目标

把 σ 系统的两类通知需求用**最低工程复杂度**实现：

| 类型 | 含义 | 时机 | 示例 |
|------|------|------|------|
| **固定时刻提醒** | 每天/每周/每月的周期性 nudge | 可预测 | "盘前规则书写时间到" |
| **触发型 alert** | 系统检测到异常后主动通知 | 不可预测 | "KPI 退化到 L4-warning" / "本周有 3 条违规" |

### 1.2 架构总览

```
┌─────────────────────────────────────────────────────┐
│                   消息系统架构                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌───────────────────┐     ┌──────────────────────┐ │
│  │ 固定时刻提醒          │     │ 触发型 Alert          │ │
│  │ (Calendar / cron)  │     │ (Event-driven)       │ │
│  └────────┬──────────┘     └──────────┬───────────┘ │
│           │                           │             │
│           ▼                           ▼             │
│  ┌───────────────────┐     ┌──────────────────────┐ │
│  │ 通道层               │     │ 通道层                │ │
│  │ • macOS/iOS 日历    │     │ • 邮件 (SMTP)         │ │
│  │ • 系统通知 (cron)    │     │ • 系统通知 (notify)    │ │
│  │                    │     │ • 文件 banner         │ │
│  └───────────────────┘     └──────────────────────┘ │
│                                                     │
│  ┌─────────────────────────────────────────────────┐ │
│  │ 持久化层：reviews/alerts/ + sigma/daily/ banner   │ │
│  └─────────────────────────────────────────────────┘ │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### 1.3 固定时刻提醒 — 详细规格

#### 1.3.1 五条日历事件

| # | 时间 | 标题 | 重复规则 | 提醒提前量 |
|---|------|------|----------|-----------|
| 1 | 工作日 08:30 | σ 盘前规则书写 | Mon-Fri | 准时 |
| 2 | 工作日 09:15 | σ 9:20 集合竞价将至 | Mon-Fri | 准时 |
| 3 | 工作日 15:15 | σ 盘后 EMA 截止提醒 | Mon-Fri | 准时（A 股 15:00 收盘后 15 分钟） |
| 4 | 周日 20:00 | σ 周复盘 | 每周日 | 准时 |
| 5 | 每月最后工作日 20:00 | σ 月校准 | 每月 | 准时 |

#### 1.3.2 实现方式

**方案 A（推荐，零工程量）：macOS / iOS Calendar 手动创建**

用户在系统日历 App 中创建 5 条重复事件。优势：
- 跨 iPhone / Mac / iPad 自动同步（iCloud）
- 原生通知，不额外安装任何东西
- 与用户现有日历共存，一目了然

提供 `.ics` 导入文件（一键导入所有 5 条）：

```
sigma/reminders/sigma-calendar.ics
```

**方案 B（补充）：本地 cron + 系统通知**

适用于不用 iCloud 或需要更灵活逻辑的场景：

```bash
# crontab 示例（macOS / Linux）
30 8  * * 1-5  /path/to/scripts/notify.sh "σ 盘前规则书写时间到"
15 9  * * 1-5  /path/to/scripts/notify.sh "σ 9:20 集合竞价将至——打开盘前规则复述"
15 15 * * 1-5  /path/to/scripts/notify.sh "σ 盘后 EMA 截止——平仓后 30 分钟内填写"
0  20 * * 0    /path/to/scripts/notify.sh "σ 周复盘时间到——make weekly-report"
```

`scripts/notify.sh` 跨平台通知：

```bash
#!/usr/bin/env bash
MSG="$1"
if command -v osascript &>/dev/null; then
    osascript -e "display notification \"$MSG\" with title \"σ 系统\""
elif command -v notify-send &>/dev/null; then
    notify-send "σ 系统" "$MSG"
fi
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
| `sigma-calendar.ics` 生成 | 0.5h | 无 |
| `sigma/reminders/README.md` | 0.5h | 无 |
| `scripts/notify.sh` | 0.5h | 无 |
| `scripts/send_alert_email.py` | 2h | SMTP 配置 |
| `scripts/inject_banner.py` | 2h | 无 |
| `cron-examples.md` | 0.5h | 无 |
| Makefile 集成 + 测试 | 1h | 上述全部 |
| **总计** | **~7h** | |

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
│   trades/*.md + sigma/daily/*.md + reviews/*                        │
│      │                                                              │
│      ├──→ make weekly-report ──→ violations_scan.py ──┐             │
│      │                          kpi_alert.py ──────────┤             │
│      │                                                 │             │
│      │                                                 ▼             │
│      │                              ┌─────────────────────────────┐ │
│      │                              │ 消息系统                      │ │
│      │                              │ • inject_banner.py → daily/ │ │
│      │                              │ • send_alert_email.py → 邮件 │ │
│      │                              │ • notify.sh → 桌面通知        │ │
│      │                              └─────────────────────────────┘ │
│      │                                                              │
│      └──→ make build-webui-data ──→ build_data.py                   │
│                                         │                           │
│                                         ▼                           │
│                              ┌─────────────────────────────┐        │
│                              │ WebUI                        │        │
│                              │ • Dashboard (KPI + 趋势)     │        │
│                              │ • Trades (列表 + 截图)        │        │
│                              │ • Weekly (AI 报告可视化)      │        │
│                              │ • Screenshots (对照画廊)      │        │
│                              └─────────────────────────────┘        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### 关键原则

1. **消息系统是"推"**（主动通知你该做什么）—— Phase 3b
2. **WebUI 是"拉"**（你主动来看数据）—— Phase 3c
3. **两者都不写数据**——写入路径唯一性在 Cursor + git
4. **两者都可关掉**——消息系统关 = 回到纯自律；WebUI 关 = 回到读 markdown

---

## 四、实施时间线

| 阶段 | 触发条件 | 交付 |
|------|----------|------|
| **Phase 3b-1** | v0 运行 4 周 P0 达标 | 消息系统：ICS 文件 + notify.sh + send_alert_email.py + inject_banner.py |
| **Phase 3b-2** | Phase 3b-1 后 1 周 | 训练资金对账：reconcile_funds.py + 集成到消息系统 |
| **Phase 3c-1** | v0.1 运行 8 周 KPI 达标 | WebUI 骨架：Vite + Vue 3 + build_data.py + Dashboard 页 |
| **Phase 3c-2** | Phase 3c-1 后 2 周 | WebUI 完整：Trades + Weekly + Screenshots + KPI 四页 |
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

*设计版本：v0 | 来源：design_proposal_2026.md v0.1 §三.2.4 + §三.2.5 + §零 Phase 拆分总表*
