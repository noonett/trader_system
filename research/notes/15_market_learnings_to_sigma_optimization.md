# 市场学习 → σ 系统设计优化方案

> 调研日期：2026-05-07
> 输入文档：notes/14（半自动交易 AI 助手产品形态与设计模式调研）+ design_proposal_2026.md v0.1 + 现有实现代码审查
> 证据等级：S/M/W/U 沿用项目标准
> 上下文：将 notes/14 的 6 个跨产品设计模式落地为 σ 系统的具体设计优化方案。每个优化标注优先级（P0/P1/P2/P3）、影响的 Phase、工程复杂度、证据支持、与 foundation 的兼容性。
>
> **本笔记的范围声明**（karpathy §1 + σ 元规则）：
> - **改的**：把 notes/14 市场学习转化为具体设计优化方案
> - **不改**：不改动现有模板/脚本/代码（方案确定后由单独 PR 实施）
> - **不做**：不重复 notes/14 的产品调研本身

---

## 摘要

从 notes/14 的 6 个跨产品设计模式中，筛选出 **5 个可转化为 σ 系统设计优化的方向**，按优先级排列：

| # | 优化方向 | 来源产品模式 | 优先级 | Phase | 核心变更 |
|---|---------|-----------|--------|-------|---------|
| OPT-1 | 行为模式统计引擎 | Zella Insights "你周一胜率 32%" | **P1** | 3b | 新增 `scripts/pattern_analysis.py` |
| OPT-2 | 纪律-绩效关联可视化 | Edgewonk Tiltmeter | **P2** | 3c | WebUI 仪表盘组件 |
| OPT-3 | 交易模板情绪标记简化 | Edgewonk 正/负/中 + Plancana 情绪标签 | **P1** | 3b | 扩展 TEMPLATE.md + violations_scan |
| OPT-4 | 违规扫描从 config.yaml 读取阈值 | Zella 多账户 + σ 多交易员设计 | **P0** | 3a hotfix | 修改 violations_scan.py |
| OPT-5 | 周报增加"牛方/熊方"对比分析结构 | TradingAgents 辩论式框架 | **P1** | 3b | 修改 weekly_report.sh prompt |

**额外分析**：OPT-6 — ATAS 平台级 binding pre-commitment（详见 §OPT-6）

**不转化的 1 个模式**（notes/14 模式 5 "自动券商同步"）：
- 工程复杂度极高（券商 API 接入 + 数据格式适配）
- 认知卸载风险未验证（notes/09 §2.1.2 研究空白）
- 当前手动录入是 σ 的"有意摩擦"设计（foundation §三.3 "好摩擦"）
- 暂列 P3，Phase 3d 可选项

---

## OPT-1：行为模式统计引擎

### 问题

当前 `violations_scan.py` 只做**二元判定**（违规/不违规），不分析行为模式的**统计趋势**。交易者无法看到：
- "你在周一的胜率是 32%，而周四是 68%"
- "你在连亏 2 笔后的下一笔倾向加大仓位 1.8x"
- "你的 `breakout-retest` 策略盈亏比 3.2，但 `mean-reversion` 只有 0.7"
- "你在 `volatile` 市场状态下的胜率是 25%，而 `trending` 是 62%"

TradeZella 的 Zella Insights 和 50+ 报告维度正是解决这个问题。

### 方案

**新增 `scripts/pattern_analysis.py`**，从 `traders/{id}/trades/` 中的结构化字段提取统计：

```python
# 输出结构（写入 traders/{id}/reviews/patterns/YYYY-MM.md）
{
    "period": "2026-05",
    "total_trades": 15,
    "win_rate": 0.53,

    # 按维度切片的胜率/盈亏比/平均仓位
    "by_weekday": {"Mon": {"trades": 3, "win_rate": 0.33, "avg_rr": 0.8}, ...},
    "by_setup_tag": {"breakout-retest": {...}, "mean-reversion": {...}},
    "by_market_condition": {"trending": {...}, "volatile": {...}},
    "by_direction": {"long": {...}, "short": {...}},
    "by_product_class": {"green-cash-stock": {...}, "yellow-small-future": {...}},

    # 序列模式
    "post_loss_behavior": {
        "avg_position_change_pct": +18.5,  # 亏损后下一笔仓位变化
        "win_rate_after_2_consecutive_losses": 0.25,
    },

    # 情绪关联（如果 OPT-3 落地）
    "by_emotion_pre": {"neutral": {...}, "anxious": {...}, "confident": {...}},

    # 止损纪律
    "stop_adherence_rate": 0.87,
    "avg_stop_breach_pct": 3.2,  # 穿越止损后平均多走了多少%
}
```

**数据来源**：全部来自 TEMPLATE.md 的现有字段 + frontmatter：

| 统计维度 | 数据来源 | 字段 |
|---------|---------|------|
| 按星期 | frontmatter `date` | 自动计算 |
| 按策略 | frontmatter `setup_tag` | 用户填写 |
| 按市场状态 | frontmatter `market_condition` | 用户填写 |
| 按方向 | frontmatter `direction` | 用户填写 |
| 按产品 | frontmatter `product_class` | 用户填写 |
| 盈亏 | frontmatter `pnl_net` | 用户填写 |
| 止损纪律 | frontmatter `stop_loss_price` + `exit_price` + `direction` | 用户填写 |
| 序列模式 | 按 `date` 排序的连续交易 | 自动计算 |

**输出格式**：markdown 表格 + 文字摘要，写入 `traders/{id}/reviews/patterns/YYYY-MM.md`，由 `make monthly-calibration` 调用。

**Makefile 集成**：

```makefile
pattern-analysis: ## 月末：行为模式统计
	@python3 scripts/pattern_analysis.py --trader $(TRADER)

monthly-calibration: violations-scan pattern-analysis ## 月末：完整月校准
	@SIGMA_TRADER=$(TRADER) bash scripts/monthly_calibration.sh
	@python3 scripts/kpi_alert.py --trader $(TRADER)
```

### 证据支持

| 证据 | 等级 | 与 OPT-1 的关系 |
|------|------|--------------|
| Auer & Griffiths 2014：特异性消息 > 通用消息 | S | **核心支持**——"你周一胜率 32%"是特异性消息 |
| Morewedge 2015：互动 + 个性化反馈 → 偏误降幅 31.94% | S | 行为模式统计是"个性化反馈"的数据基础 |
| Steiss 2024 + IJETHE 2026：反馈质量 ≠ 行为改变 | S | **风险**——即使统计准确，用户也可能不改行为 |
| notes/09 §4.2：后台 AI 异步报告是推荐形态 | U | 月度模式报告 = 后台异步分析的典型实现 |

### 与 foundation 的兼容性

- **§三.2 anchoring 防御**：模式统计是**事后数据**，不在决策瞬间呈现 → 不触发认知卸载 ✅
- **§三.8 AAR 框架**：模式统计提供"事前预设 vs 实际发生"的数据基础 ✅
- **§三.3 binding pre-commitment**：统计本身不是 binding，但可作为 KPI alert 的输入 ✅

### 优先级判定

**P1（Phase 3b）**：
- 不是 v0 启动必需（P0 的 violations_scan 已能检测违规）
- 但对"从违规检测到行为理解"的跨越有实质价值
- 工程量低（~5-8 工时，纯 Python 数据聚合）
- 数据来源全部是现有模板字段，不需要新的用户输入

### 与现有实现的关系

- **不改** `violations_scan.py`（它做二元违规检测，职责不变）
- **新增** `pattern_analysis.py`（做趋势统计，互补关系）
- **不改** TEMPLATE.md（已有足够字段）
- **需改** Makefile（加一行 target）

---

## OPT-2：纪律-绩效关联可视化

### 问题

当前 σ 系统的所有输出都是 markdown 文本——violations 报告、KPI alerts、周/月复盘。用户**看不到**纪律与绩效之间的视觉关联。

Edgewonk 的 Tiltmeter 是当前市场上最有效的"纪律可视化"设计：把遵规/违规的时间带叠加在收益曲线上，让交易者**一眼看到**"遵守规则时赚钱，违反规则时亏钱"。

### 方案

在 WebUI Phase 3c（P2）中增加**两个仪表盘组件**：

#### 组件 A：σ Tiltmeter（纪律-绩效时间线）

```
时间轴 →
┌─────────────────────────────────────────────────┐
│  收益曲线（累计 PnL）                               │
│    /\    /\          /\                           │
│   /  \  /  \    ____/  \____                      │
│  /    \/    \  /              \                    │
│ /            \/                \___                │
│                                                   │
│ ▓▓▓▓░░▓▓▓▓▓▓░░░░▓▓▓▓▓▓▓▓▓░░░░░░                │
│ 绿=遵规  红=违规  （来自 violations_scan 数据）        │
└─────────────────────────────────────────────────┘
```

**数据来源**：
- 收益曲线：`traders/{id}/trades/` 中 `pnl_net` 按日期累加
- 纪律条带：`traders/{id}/reviews/violations/` 中每周违规类型 + 日期
- **不需要用户额外输入**——完全基于现有数据

**实现路径**：
- WebUI 新增 `/dashboard` 路由
- 前端图表库（Recharts / Chart.js）绑定从 `repo.ts` 读取的 trades + violations 数据
- 后端新增 tool `getDashboardData` 聚合 trades + violations

#### 组件 B：维度切片面板（OPT-1 的可视化呈现）

如果 OPT-1 的 `pattern_analysis.py` 已落地，组件 B 把其输出可视化为：
- 按策略的胜率柱状图
- 按星期的盈亏热力图
- 按市场状态的表现对比
- 连亏后行为趋势图

### 证据支持

| 证据 | 等级 | 与 OPT-2 的关系 |
|------|------|--------------|
| Morewedge 2015：互动 + 个性化视觉反馈 → 偏误降幅 31.94% | S | Tiltmeter 是"个性化视觉反馈"的直接实现 |
| Edgewonk Tiltmeter：纪律叠加收益曲线 | W | 产品设计参考，无独立效果评估 |
| notes/09 对比矩阵：后台 AI 4/6 维度最优 | U | 仪表盘是"被动呈现"，用户主动查阅 → 后台范式 |

### 与 foundation 的兼容性

- **§三.2 不主动归因**：仪表盘只呈现数据，不说"你应该…" ✅
- **§三.8 AAR 三段式**：可视化提供"事前 vs 实际 vs 偏差"的直觉入口 ✅
- **设计 D1 P2**：WebUI read-only 渲染层正是 Phase 3c 的定位 ✅

### 优先级判定

**P2（Phase 3c）**：
- 依赖 WebUI 框架已搭建（当前 WebUI 是 chat-only）
- 依赖足够的交易数据积累（≥20-30 笔才有统计意义）
- 工程量中等（~10-15 工时，需前端图表 + 后端数据聚合）
- **触发条件**：v0.1 启动 8 周 KPI 持续达标 + 用户主动需求（design_proposal §0.2）

### 与现有实现的关系

- **不改**现有 WebUI chat 功能
- **新增** `/dashboard` 路由 + 组件
- **新增** `tools.ts` 中 `getDashboardData` tool
- **依赖** OPT-1 的 `pattern_analysis.py` 输出（组件 B）

---

## OPT-3：交易模板情绪标记简化

### 问题

当前 TEMPLATE.md 的情绪记录分布在两处，格式不一致：
- **If 4**（开仓前）：自由文本 `当前情绪状态：` + `强度：[1-5]`
- **四、盘后 EMA**：自由文本 `平仓时情绪：` + `强度 [1-5]`

问题：
1. **自由文本难以聚合**——"紧张"、"有点紧张"、"anxiety"、"焦虑"是同一情绪但无法自动归并
2. **无法与绩效做关联统计**——OPT-1 的 `by_emotion_pre` 切片需要标准化标签
3. **高反刍风险**（Sbarra 2013 S 级）——自由文本情绪描述可能诱发反刍式叙事

Edgewonk 的解决方案是**正面/负面/中性三级评分 + 自定义标签**，Plancana 是预设情绪标签列表。两者都避免了自由文本。

### 方案

**扩展 TEMPLATE.md frontmatter**，新增两个枚举字段：

```yaml
# 在现有 frontmatter 中增加
emotion_pre: # 开仓前情绪：neutral / confident / anxious / frustrated / excited / revenge / fomo
emotion_post: # 平仓后情绪：neutral / relieved / regretful / satisfied / angry / numb
```

**设计原则**：
- **枚举而非自由文本**——可聚合、可统计、减少反刍风险
- **标签基于交易场景高频情绪**（不用心理学术语，用交易者语言）
- **保留 If 4 的自由文本部分作为可选补充**——强度 [1-5] 保留，但核心统计基于枚举字段
- **7 个开仓前标签 + 6 个平仓后标签**——覆盖 decision-chain 检查清单里的情绪门禁（`{兴奋, 愤怒, 报复, 翻本, 恐惧}`）+ 中性 + 正向

**violations_scan 扩展**：

当 `emotion_pre` 为 `revenge` 或 `fomo` 时，自动标记为**第 6 类违规**（"情绪违规——已声明处于高风险情绪状态但仍开仓"）。这是从"事后发现"到"自我声明"的升级——用户在 If 4 填了 `revenge` 但仍然开了仓，violations_scan 应该捕捉到这个矛盾。

### 证据支持

| 证据 | 等级 | 与 OPT-3 的关系 |
|------|------|--------------|
| Sbarra 2013：高反刍者自由文本情绪描述 9 月后变差 | S | **核心风险** → 枚举标签而非自由叙事 |
| Edgewonk 正/负/中 + 自定义标签 | W | 产品设计参考 |
| Plancana 情绪标记 | W | 产品设计参考 |
| notes/09 §2.5：What 提问 > Why 提问 | S | 枚举是 What（"你现在的状态是什么"），不是 Why（"你为什么焦虑"）|
| Bisra 2018：开放式自我解释 g=0.55 | S | **保留 If 4 自由文本作为可选**——不放弃开放式反思的价值 |

### 与 foundation 的兼容性

- **§三.2 不主动归因**：枚举标签是用户自选，不是 AI 判定 ✅
- **§三.8 AAR What 主导**：枚举是描述性的（What），不是归因性的（Why）✅
- **§三.11 临床安全**：`revenge`/`fomo` 标签本身是自我觉察工具，不是诊断 ✅

### 优先级判定

**P1（Phase 3b）**：
- 对 OPT-1 的情绪切片统计是前置条件
- 模板变更工程量极低（~1-2 工时）
- violations_scan 扩展工程量低（~2-3 工时）
- 不影响现有已录入的交易记录（新字段为可选，空值不触发）

### 与现有实现的关系

- **改** `traders/default/trades/TEMPLATE.md`：frontmatter 增加 2 字段
- **改** `scripts/violations_scan.py`：增加第 6 类违规检测
- **改** `sigma/templates/decision-chain.md`：If 4 增加枚举引用
- **不改** 现有已填写的交易记录（向后兼容，空值跳过）

---

## OPT-4：违规扫描从 config.yaml 读取阈值

### 问题

当前 `violations_scan.py` 硬编码 `MAX_SINGLE_POSITION_PCT = 20`（第 89 行），而 `traders/default/config.yaml` 已经定义了 `overrides.max_single_position_pct: 20`。这意味着：

1. 如果用户修改 config.yaml 的阈值，violations_scan **不会感知**
2. 多交易员场景下，每个交易员的阈值不同但脚本只用一个硬编码值
3. `max_daily_loss_pct: 3` 和 `yellow_weekly_limit: 3` 在 config.yaml 中定义了但**没有任何脚本检测**

这不是 notes/14 某个产品的"学习"，而是在审查现有实现时发现的**设计-实现不一致**——σ 元规则的"看见就改"范围。

### 方案

```python
# violations_scan.py 修改

def load_trader_config(trader_id):
    """Load trader config.yaml and return overrides."""
    config_path = WORKSPACE / "traders" / (trader_id or "default") / "config.yaml"
    if config_path.exists():
        import yaml
        with open(config_path) as f:
            config = yaml.safe_load(f)
        return config.get("overrides", {})
    return {}

# 替换硬编码
overrides = load_trader_config(trader_id)
MAX_SINGLE_POSITION_PCT = overrides.get("max_single_position_pct", 20)
MAX_DAILY_LOSS_PCT = overrides.get("max_daily_loss_pct", 3)
YELLOW_WEEKLY_LIMIT = overrides.get("yellow_weekly_limit", 3)
```

**新增第 6 类违规**（日损超限）：

```python
# 当日所有交易的 pnl_net 累加 < -MAX_DAILY_LOSS_PCT% × 账户总额
# 数据来源：同一日期的所有 trade files 的 pnl_net 字段
```

**新增第 7 类违规**（黄色产品周上限）：

```python
# 本周 product_class: yellow-* 的交易笔数 > YELLOW_WEEKLY_LIMIT
```

### 证据支持

| 证据 | 等级 | 与 OPT-4 的关系 |
|------|------|--------------|
| Fischbacher 2017：binding pre-commitment > reminders | S | config.yaml 的阈值必须被**执行**，不只是**记录** |
| design_proposal §三.2.3 A 类：自动违规扫描 | — | 扫描范围应覆盖 config.yaml 定义的所有阈值 |

### 优先级判定

**P0（Phase 3a hotfix）**：
- 这是 σ 元规则"看见就改"范围的编码错误（硬编码 vs config.yaml 不一致）
- 工程量极低（~2-3 工时）
- 修复后立即生效

### 与现有实现的关系

- **改** `scripts/violations_scan.py`：读 config.yaml + 新增 2 类违规
- **不改** `traders/default/config.yaml`（已有正确的阈值定义）
- **需新增** PyYAML 依赖（或用简单文本解析避免依赖）

---

## OPT-5：周报增加"牛方/熊方"对比分析结构

### 问题

当前 `weekly_report.sh` 生成的 AI prompt 是线性叙事——"这周发生了什么"。用户读完后得到一份总结，但**没有被强制看到两面**。

TradingAgents 的辩论式框架提供了一个有价值的结构：**强制从正反两面审视同一组数据**。

### 方案

修改 `weekly_report.sh` 中的 AI prompt 结构，要求 AI 按以下格式输出周报：

```markdown
## 本周 σ 审计报告

### 🟢 本周做对的（"牛方视角"）
> 从 trades/ 和 daily/ 中提取本周**遵守规则、执行良好**的证据

1. [具体交易 + 遵规证据]
2. [具体行为改进]

### 🔴 本周做错的（"熊方视角"）
> 从 violations/ 和 trades/ 中提取本周**违规、偏差、纪律松懈**的证据

1. [具体违规 + 影响]
2. [具体行为倒退]

### ⚖️ 风控审计
> violations_scan 的正式输出 + 未被扫描器捕捉但值得注意的模式

### 📊 关键数据
> 本周胜率、盈亏比、平均仓位、止损遵守率、情绪分布

### 🪞 镜子问题（不回答，留给你周复盘时自答）
> 1-3 个基于本周数据的 What 问题（禁 Why）
```

**关键设计约束**：
- **"镜子问题"必须是 What 不是 Why**——避免触发反刍（Watkins & Teasdale 2004 S 级）
- **AI 不判断好坏**——只陈述事实 + 引用具体交易文件 + 让用户自己在周复盘中判断
- **牛方/熊方是数据驱动的**，不是 AI 的主观评价——"你在 2026-05-05 的 breakout-retest 交易中止损执行准确"是事实陈述，不是"你做得好"

### 证据支持

| 证据 | 等级 | 与 OPT-5 的关系 |
|------|------|--------------|
| TradingAgents 辩论式框架（arXiv 2412.20138） | M | 结构参考——强制正反两面 |
| Keiser & Arthur 2021：AAR 复盘 d=0.79 | S | "事前 vs 实际 vs 偏差"三段式 → 牛方/熊方是偏差的两个方向 |
| notes/09 §四.2：后台 AI 异步报告 | U | 周报 = 后台 AI 的核心交付物 |
| Watkins & Teasdale 2004：Why 提问触发反刍 | S | "镜子问题"必须是 What |

### 与 foundation 的兼容性

- **§三.2 AI 是镜子不是裁判**：牛方/熊方都只陈述事实 ✅
- **§三.8 AAR 三段式**：牛方 ≈ "按计划执行的"，熊方 ≈ "偏差" ✅
- **§三.2 不主动归因**：镜子问题是 What 不是 Why ✅

### 优先级判定

**P1（Phase 3b）**：
- 只改 shell 脚本中的 prompt 文本，工程量极低（~1-2 工时）
- 不影响现有 AI 后端（prompt 结构变更，输出格式变更）
- 但需要 `weekly_report.sh` 的路径问题先修复（已知 gap：脚本仍引用旧路径 `trades/`、`sigma/daily/`、`sigma/ai-roles.md`）

### 与现有实现的关系

- **改** `scripts/weekly_report.sh`：修复路径 + 改 prompt 结构
- **不改** `sigma/templates/weekly-review.md`（用户填写的周复盘模板不变）
- **前置修复**：`weekly_report.sh` 中的路径必须先对齐到 `traders/{id}/` 多交易员布局

---

## OPT-6：ATAS 平台级 binding pre-commitment

### 问题：当前 binding 层的执行力不足

σ 系统当前的 binding pre-commitment 实现在**文件系统层**：
- **C 类**：git pre-commit hook 拦截 `product_class: red` → 只防"记录红区产品"，不防"交易红区产品"
- **A 类**：violations_scan 事后检测 → 只能"发现"违规，不能"阻止"违规
- **B 类**：KPI alert → 只能"告警"退化，不能"锁屏"

**核心缺口**：所有 binding 都发生在**交易之后**（post-trade），不在**交易之前**（pre-trade）。用户完全可以在 ATAS 中自由下单，违反所有规则，然后事后在 violations 报告中"acknowledge"。

Fischbacher 2017（S 级）的核心发现是：**reminders 无效，actual ex-ante commitment 才有效**。当前的 σ binding 层更接近 "sophisticated reminders" 而非 "actual pre-trade enforcement"。

### 用户问题：能否通过 ATAS 拦截实现？

用户使用 ATAS（Advanced Time And Sales）作为主交易平台，连接 Interactive Brokers (CME training)。ATAS 提供 C# Strategy API，理论上可以在下单前介入。

### ATAS 能力评估

| 能力 | 当前状态 | 来源 |
|------|---------|------|
| **C# Strategy API** | ✅ 可用：继承 `ChartStrategy`，重写 `OnCalculate`/`OnStopping` 等方法 | docs.atas.net【W 级，官方文档】 |
| **订单管理** | ✅ 可用：`OpenOrder`/`ModifyOrder`/`CancelOrder` + 状态回调 | docs.atas.net【W 级】 |
| **当前持仓** | ✅ 可用：`CurrentPosition`、`AveragePrice` 属性 | docs.atas.net【W 级】 |
| **交易事件** | ✅ 可用：`OnNewMyTrade(MyTrade)` 回调 | docs.atas.net【W 级】 |
| **强制平仓** | ✅ 可用：`CloseCurrentPosition()` 方法 | docs.atas.net【W 级】 |
| **SL/TP 自动化** | ✅ 内置：简单模式/多级模式/追踪止损/保本移动 | help.atas.net【W 级】 |
| **风险模块（日损上限/仓位上限/锁屏）** | ❌ **尚未发布**：作为 feature request "In Progress" | feedback.atas.net【W 级】 |
| **基于 PnL 阻止下单** | ❓ **无官方文档**：需自定义 Strategy 实现 | 未找到示例【U 级推论】 |

### 可行的 ATAS binding 方案（三层架构）

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: ATAS 内置 SL/TP（已可用，零开发）               │
│  → 每笔交易自动设止损/止盈                                │
│  → 实现 foundation §三.3 "止损在执行层" 的 binding        │
├─────────────────────────────────────────────────────┤
│  Layer 2: ATAS C# Strategy "σ-Guardian"（需开发）       │
│  → 监控日内累计 PnL → 触发日损上限锁定                      │
│  → 监控持仓大小 → 拒绝超限订单                             │
│  → 监控交易频率 → 超过 yellow 周上限时告警                   │
├─────────────────────────────────────────────────────┤
│  Layer 3: σ 文件系统层（现有，事后审计）                     │
│  → violations_scan.py 事后复核                          │
│  → git pre-commit hook 红区拒绝                         │
│  → KPI alert 退化检测                                   │
└─────────────────────────────────────────────────────┘
```

### Layer 1：ATAS 内置 SL/TP（零开发，立即可用）

**做什么**：在 ATAS 中启用 Automatic Exit Strategy，每笔交易自动附带 SL/TP。

**配置**：
- Stop Loss：从 If 2 的 `P_stop` 推导 → 在 ATAS 中设为默认 SL 距离
- Take Profit：从 `target_rr` × SL 距离推导
- Breakeven：设定"盈利 N ticks 后移动止损到保本"
- Trailing Stop：根据 `stop_type` 选择是否启用追踪

**binding 强度**：**高**——一旦设定，SL/TP 在 ATAS 侧自动执行，用户不需要手动平仓。
**局限**：ATAS 必须保持运行和连接；如果断网/关闭 ATAS，SL/TP 不会执行（除非 broker 侧也设了）。

**与 σ 系统的集成**：
- 盘前 if-then 中明确"今日 SL/TP 策略设置"
- 交易记录 TEMPLATE.md 中 `stop_type` 字段与 ATAS SL 配置对应
- violations_scan 可对比 `stop_loss_price` vs 实际 `exit_price` 验证 SL 是否被执行

### Layer 2：ATAS C# Strategy "σ-Guardian"（需开发）

**做什么**：开发一个 ATAS 自定义 Strategy，作为"σ 守门人"在交易执行层拦截违规。

**核心逻辑**（C# 伪代码）：

```csharp
public class SigmaGuardian : ChartStrategy
{
    // 从 config 读取（对应 config.yaml overrides）
    [Display(Name = "日损上限%")]
    public decimal MaxDailyLossPct { get; set; } = 3m;

    [Display(Name = "单笔最大仓位%")]
    public decimal MaxPositionPct { get; set; } = 20m;

    [Display(Name = "黄色产品日内上限")]
    public int YellowDailyLimit { get; set; } = 3;

    private decimal _dailyPnL = 0;
    private decimal _accountSize;
    private int _todayTradeCount = 0;
    private bool _tradingLocked = false;

    protected override void OnNewMyTrade(MyTrade trade)
    {
        _dailyPnL += trade.PnL;
        _todayTradeCount++;

        // 日损超限 → 强制平仓 + 锁定
        if (_dailyPnL < 0 &&
            Math.Abs(_dailyPnL) / _accountSize * 100 > MaxDailyLossPct)
        {
            CloseCurrentPosition();
            _tradingLocked = true;
            // 弹窗告警
            AddAlert("σ 日损上限触发",
                $"当日亏损 {_dailyPnL:F1} = {Math.Abs(_dailyPnL)/_accountSize*100:F1}%，"
                + $"超过 {MaxDailyLossPct}%，已锁定交易");
        }
    }

    protected override void OnCalculate(int bar, decimal value)
    {
        // 如果已锁定，取消所有挂单
        if (_tradingLocked && Orders.Any())
        {
            foreach (var order in Orders.ToList())
                CancelOrder(order);
        }
    }
}
```

**能实现的 binding**：

| 约束 | 实现方式 | binding 强度 |
|------|---------|-------------|
| 日损上限 | `OnNewMyTrade` 监控累计 PnL → 超限时 `CloseCurrentPosition()` + 锁定 | **强**：平仓是自动的 |
| 单笔仓位上限 | 拦截 `OpenOrder` 前检查仓位大小 | **中**：可以取消自己的订单，但无法阻止用户手动在 DOM 下单 |
| 交易频率 | 计数 `OnNewMyTrade` 触发次数 | **弱**：只能告警，无法真正阻止 |

**不能实现的 binding**：

| 约束 | 原因 |
|------|------|
| 红区产品拒绝 | ATAS Strategy 无法区分产品类型（需要 σ 系统的 product_class 分类） |
| 盘前 if-then 门禁 | ATAS 无法知道用户是否完成了 markdown 盘前文件 |
| 决策链 5 问完成 | ATAS 无法知道用户是否填完了 If 1-5 |

### Layer 3 不变（事后审计）

现有的 `violations_scan.py` + `kpi_alert.py` + git hooks 作为**最后一道防线**：即使 Layer 1/2 被绕过（ATAS 关闭、断网、手动覆盖），事后审计仍能发现问题。

### 三层之间的关系

```
时间轴 →

盘前                 下单瞬间              盘中                  盘后
├─────────────────┼─────────────────┼──────────────────┼──────────────────┤
│ Layer 3: git    │ Layer 2: ATAS   │ Layer 1: ATAS    │ Layer 3: scan   │
│ 盘前文件必须存在 │ σ-Guardian 检查  │ SL/TP 自动执行    │ violations 检测  │
│ (pre-commit)    │ 仓位/日损/频率    │ 止损/止盈/追踪      │ 7 类违规扫描      │
│                 │ 拦截或告警         │                   │ KPI alert        │
```

**核心设计原则：defense in depth（纵深防御）**
- Layer 1 解决"止损不执行"问题 → 最高优先（零开发）
- Layer 2 解决"日损超限不停手"问题 → 中等优先（需 C# 开发）
- Layer 3 解决"所有被绕过的违规"问题 → 已实现

### 实施建议

| 阶段 | 内容 | 优先级 | 工程量 |
|------|------|--------|--------|
| **立即** | 在 ATAS 中启用 SL/TP Automatic Exit Strategy（Layer 1） | **P0** | 0（配置操作） |
| **Phase 3b** | 开发 σ-Guardian C# Strategy（Layer 2 日损上限） | **P1** | ~15-25 工时（含 C# 学习曲线 + ATAS API 调试）|
| **Phase 3b** | σ-Guardian 增加仓位检查 | **P1** | ~5-10 工时（增量）|
| **观望** | 等待 ATAS 官方 Risk Management Module 发布 | — | 0（如果 ATAS 官方做了，不需要自己写） |

### 与 foundation 的兼容性

- **§三.3 binding pre-commitment**：Layer 1+2 把 binding 从"事后审计"升级到"事前/事中拦截" ✅
- **§三.3 "reminders 无效，actual commitment 才有效"**（Fischbacher 2017 S 级）：ATAS SL/TP 和日损锁定都是 actual enforcement ✅
- **§三.10 产品分级**：红区拒绝仍依赖 Layer 3（ATAS 层无法判断 product_class）⚠️
- **§三.2 "好摩擦"**：ATAS Layer 1 SL/TP 不增加操作摩擦（自动执行）；Layer 2 日损锁定是"强制摩擦"而非"提醒摩擦" ✅

### 风险与局限

1. **ATAS 必须保持运行**：Layer 1+2 在 ATAS 关闭/断网时失效。这对期货（CME 夜盘）是实际风险——如果用户睡着了、ATAS 断了，SL 不会执行。**缓解**：在 IB 侧同时设 bracket order。
2. **自定义 Strategy 的稳定性**：C# Strategy 如果有 bug 可能反而导致误操作（错误平仓、错误锁定）。**缓解**：先在模拟盘测试 ≥2 周。
3. **无法替代 σ 的认知层 binding**：ATAS 只能在"执行层"拦截，无法替代"是否完成盘前规则"、"是否填完决策链"等认知层约束——这些仍需 Layer 3。
4. **C# 开发学习曲线**：如果用户不熟悉 C# + Visual Studio + ATAS SDK，开发 σ-Guardian 的实际工时可能是估计的 2-3x。

> **诚实标记**：Layer 2（σ-Guardian）的可行性是基于 ATAS 官方文档的 U 级推论——`OnNewMyTrade` + `CloseCurrentPosition()` 组合能否可靠实现"日损超限 → 自动平仓 + 锁定"，需要在 ATAS 模拟盘上实际测试验证。文档中没有这样的完整示例。ATAS 官方的 Risk Management Module 作为 feature request 标记为 "In Progress"，如果 ATAS 官方发布了，自定义开发可能不需要。

---

## 实施路线图

### Phase 3a hotfix（立即可做）

| 项目 | 变更文件 | 工程量 |
|------|---------|--------|
| **OPT-4** config.yaml 阈值读取 + 2 类新违规 | `scripts/violations_scan.py` | ✅ 已完成 |
| **路径对齐修复**（已知 gap） | `scripts/weekly_report.sh`, `scripts/monthly_calibration.sh`, `scripts/install_hooks.sh` | ✅ 已完成 |
| **OPT-6 Layer 1** ATAS 启用 SL/TP Automatic Exit Strategy | ATAS 平台配置（非代码） | 0（配置操作） |

### Phase 3b（v0 启动 4 周 P0 KPI 达标后）

| 项目 | 变更文件 | 工程量 | 前置条件 |
|------|---------|--------|---------|
| **OPT-3** 情绪枚举标签 | TEMPLATE.md, decision-chain.md, violations_scan.py | ~3-5 工时 | 无 |
| **OPT-1** 行为模式统计引擎 | 新增 pattern_analysis.py, Makefile | ~5-8 工时 | OPT-3（情绪字段） |
| **OPT-5** 周报牛方/熊方结构 | weekly_report.sh | ~1-2 工时 | 路径对齐修复 ✅ |
| **OPT-6 Layer 2** σ-Guardian ATAS C# Strategy | ATAS SDK 外部项目（非本仓库） | ~15-25 工时 | ATAS 模拟盘可用 |

### Phase 3c（v0.1 启动 8 周 KPI 持续达标后）

| 项目 | 变更文件 | 工程量 | 前置条件 |
|------|---------|--------|---------|
| **OPT-2** σ Tiltmeter 仪表盘 | WebUI 新增 /dashboard + getDashboardData | ~10-15 工时 | OPT-1, WebUI 框架 |

---

## 设计约束汇总（必须遵守）

以下约束来自 foundation v5 + design_proposal v0.1 + notes/03/09/14 的交叉验证，**所有 OPT 方案必须满足**：

1. **数据归交易者**：所有新增输出写入 `traders/{id}/` 目录树，不写仓库根
2. **markdown + git 是唯一事实源**：可视化层（WebUI）只读 markdown，不建独立数据库
3. **后台异步**：模式统计和可视化都是事后呈现，不在交易决策瞬间介入
4. **不主动归因**：AI 生成的报告只陈述数据事实，不说"你应该…"
5. **What 不是 Why**：所有反思提示用 What 框架，禁用 Why 类提问
6. **枚举优先于自由文本**：新增字段用枚举标签，减少反刍风险
7. **向后兼容**：所有新字段为可选，旧交易记录不受影响
8. **退化路径不受影响**：这些优化是 Phase 3b/3c 增量，不改变 L4→L0 退化逻辑

---

## 本笔记的局限

1. **所有 OPT 方案的"效果"都是 U 级**——没有任何方案在交易场景有直接的 RCT 验证。它们的合理性来自邻近领域证据（debiasing S 级、AAR S 级、特异性消息 S 级）到交易场景的逻辑外推。

2. **工程量估计是粗略的**——"~5-8 工时"是基于代码审查的主观判断，实际可能因边界情况（数据缺失、字段不一致、frontmatter 解析异常）而增加。

3. **OPT-2 的可视化设计只是文字描述**——实际 UI 设计需要原型验证，文字描述的可视化不一定是最佳呈现方式。

4. **未覆盖中国市场产品的设计模式**——A 股/港股场景的交易助手（同花顺、东方财富）可能有不同的设计范式，本方案未参考。

5. **OPT-1 的"序列模式"分析需要足够样本量**——"连亏 2 笔后下一笔行为"需要至少 10-15 个这样的序列才有统计意义。Phase 3b 启动时可能数据不足。

> **诚实标记**：以上 5 个 OPT 方案是"把市场产品的成功设计模式 + 学术证据，转化为 σ 系统具体改进"的 U 级逻辑推演。它们的优先级排列基于与 foundation 兼容性 + 工程复杂度 + 证据强度的综合判断，不是精确计算。
