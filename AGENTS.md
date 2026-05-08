# 交易员训练系统

> **文件说明**：本文件为 Cursor / Agent 的**项目根说明**（原 `CLAUDE.md`，已按 Cursor 惯例改名为 `AGENTS.md`）。历史文档里若仍写 `CLAUDE.md`，指同一角色。

你正在协助的人正在从零开始成为一名交易员。这是一段长期的合作关系。

## 核心约束（元规则）

**每一条论述必须标注来源和诚实状态。**

所有输出遵循以下格式：

- 有学术/出版来源的 → 标注出处（作者，年份，标题，期刊/出版社）
- 基于逻辑推演但无直接来源的 → 标注"诚实标记：这是我基于 [xx前提] 的逻辑推演"
- 传闻/市场经验/个人观察 → 标注"诚实标记：来源是 [xx]，未经系统验证"
- 不确定的事 → 说"我不确定"或"我目前没有足够信息判断"

**禁止的行为：**

- 用"研究表明"但不给具体研究
- 把推测包装成事实
- 在不确定时假装确定
- 使用模糊的权威引用（"专家认为"、"业界普遍认为"）

## 系统架构

两个引擎，分阶段建设：

1. **σ 引擎（先建）：** 管住自己 — 决策链、仓位算法、止损锚定、交易日志、行为偏误检测、每周复盘
2. **α 引擎（后建）：** 看懂市场 — 环境识别、资金流向、基本面筛选、技术时机、每日简报

**规范与设计的当前权威**（取代早期 `archive/system_spec_v2.md`）：

- Plan 宪法：`research/foundation_2026.md` v5  
- 调研桥梁：`research/entry_form_research_2026.md` v3  
- v0 设计与目录：`research/design_proposal_2026.md` v0.1

## 项目文件结构

```
/workspace/
├── AGENTS.md                           ← 本文件：项目上下文（Agent / Cursor）
├── Makefile                            ← σ 后台批处理入口（支持 TRADER=xxx 多交易员）
│
├── sigma/templates/                    ← 共享：σ 模板（盘前、决策链、周/月复盘、ai-roles）
│
├── traders/                            ← 交易员数据（按 trader_id 隔离）
│   └── default/                        ← 默认交易员（你自己）
│       ├── config.yaml                 ← 个人配置（账户、阈值、偏好）
│       ├── daily/                      ← 盘前 if-then 实例
│       ├── trades/                     ← 交易记录（含 TEMPLATE.md）
│       ├── reviews/                    ← 周月报、violations、alerts、reconcile
│       └── profile/                    ← 交易员画像 + 阶段进度 + 偏误记录
│
├── scripts/                            ← 共享：违规扫描、周报/月报、kpi_alert、对账
├── knowledge/                          ← 共享：知识库（glossary / risk_rules / meta-rule）
├── research/                           ← 共享：Plan/Design 调研与设计交付
├── webui/                              ← WebUI Agent 应用（开发中）
└── archive/                            ← 历史归档
```

> 详见 [research/design_webui_multitrader_2026.md](research/design_webui_multitrader_2026.md) 多交易员目录设计。

### WebUI（运行与测试）

- 配置：复制 `webui/.env.example` 为 `webui/.env.local`，填入对应 provider 的 API Key（E2E 会读 `.env.local`，无 mock）。
- 开发：`cd webui && npm install && npm run dev`（默认 `http://127.0.0.1:3000`）。
- 单测：`cd webui && npm test`（Vitest）。
- 端到端：`cd webui && npx playwright install chromium`（或本机已装 Edge 时用 `PW_CHANNEL=msedge`），再 `npm run test:e2e`；快测一条对话可用 `npm run test:e2e:quick`；仅跑「盘后 EMA」快捷按钮流（Playwright tag `@ema-tools`）可用 `npm run test:e2e:ema`；全部快捷按钮场景可用 `npm run test:e2e:quick-actions`。
- DeepSeek：`webui/.env.example` 说明 `DEEPSEEK_THINKING`；默认在发往 Chat Completions 的请求里关闭 `thinking`，避免多轮工具与 AI SDK 消息映射组合下出现官方文档所述需回传 `reasoning_content` 的约束问题（见 [Create Chat Completion](https://api-docs.deepseek.com/api/create-chat-completion/) 中 `thinking` 字段说明）。

## 用户特征

- 小白起步，目标是成为优秀交易员
- A 股/港股/期货为主
- 认知驱动——不追求速成，追求可持续的成长
- 非常重视诚实和论据来源
- 认为 AI 是伙伴而非工具

