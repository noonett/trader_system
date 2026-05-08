# ATAS 实时下单捕获 → σ 交易记录自动生成 — 技术可行性分析

> **位置**：本文件为 Phase 3 技术调研，对应 design_proposal_2026.md D6 的**升级路径**（原 D6 选择了 "C+D 手动复盘+周批量对账"；本文评估**实时捕获**的可行性与所需能力）。
>
> **当前版本**：v0.1（2026-05-08）
>
> **触发动因**：用户问"能不能实时获取 ATAS 下单记录/截图 → 推送给 agent → 生成初版交易记录"
>
> **诚实标记**：以下 ATAS API 信息来源于 docs.atas.net 官方文档（M 级）+ help.atas.net 帮助文档（M 级）+ GitHub AtasPlatform/Indicators 仓库（M 级）。架构方案部分为逻辑推演（U 级）。

---

## 〇、结论先行

**可以做到。但需要以下 3 个新组件，全部不存在于当前系统中：**

| # | 组件 | 语言/平台 | 复杂度 | 当前状态 |
|---|------|-----------|--------|----------|
| 1 | **ATAS C# 自定义指标（SigmaBridge）** | C# / .NET / ATAS SDK | 中高 | 不存在 |
| 2 | **本地中继服务（sigma-relay）** | Python（或 Node.js） | 中 | 不存在 |
| 3 | **Agent 侧 trade-draft 生成器** | TypeScript（webui 现有栈） | 中低 | 不存在 |

**不需要 OCR。** ATAS 的 C# 指标 API 可直接获取结构化成交数据（价格、方向、数量、时间戳、Playbook ID），比截图 OCR 可靠几个数量级。

**截图仍有价值** — 但作为"视觉证据补充"（盘口/K线环境），不作为数据源。截图捕获可由组件 1 触发系统级屏幕截图，或由用户手动完成。

---

## 一、ATAS 平台能力盘点（M 级，docs.atas.net）

### 1.1 交易事件钩子

ATAS 自定义指标（继承 `ExtendedIndicator`）可 override 以下事件方法：

```csharp
protected override void OnNewMyTrade(MyTrade myTrade)      // 成交回报
protected override void OnOrderChanged(Order order)        // 订单状态变更
protected override void OnPositionChanged(Position position) // 持仓变化
protected override void OnNewOrder(Order order)            // 新订单提交
protected override void OnPortfolioChanged(Portfolio portfolio)
```

`MyTrade` 对象包含：价格、数量、方向、时间戳、合约、账户。
`Position` 对象包含：持仓均价、浮动盈亏、实现盈亏。

**关键点**：`OnNewMyTrade` 在**每次实际成交**时触发（非挂单、非撤单），是最精确的"下单完成"信号。

### 1.2 Webhook 支持

ATAS 内建 Webhook 功能（help.atas.net/72000648977）：
- 指标可向外部 URL 发 HTTP 请求
- 多个指标条件可合并为单一通知
- 通过外部自动化平台（如 n8n / Make / 自建服务）接收

**限制**：
- Webhook listener 功能（外部 → ATAS）仍在 feature request 阶段
- 对外发送（ATAS → 外部）已可用

### 1.3 Playbook API

```csharp
class Playbook {
    long Id;
    string Name;
    string? Description;
    string? Emoji;
    long? Color;
}
```

可通过 `ITradingStatisticsProvider.Playbooks` 过滤特定策略标签下的交易。

### 1.4 Telegram Alert Bot

- `@atas_alerts_bot` 已上线
- 支持 Smart Tape、Cluster Search、Big Trades 等模块的 alert 推送
- **不直接支持自定义指标的任意 payload 推送**（仅预定义格式）

### 1.5 统计导出

- 手动：`Statistics → Export statistics` → `.xlsx`
- 包含 3 个 sheet：统计数据 / 日志 / 交易情况
- **不支持自动触发导出**——必须用户手动点击

---

## 二、架构方案评估

### 方案 A：ATAS C# 指标 → HTTP POST → 本地中继服务（**推荐**）

```
┌─────────────────────────────────────────────────────────────────┐
│  ATAS (Windows)                                                  │
│                                                                  │
│  ┌──────────────────────────┐                                   │
│  │  SigmaBridge.cs          │                                   │
│  │  (ExtendedIndicator)     │                                   │
│  │                          │                                   │
│  │  OnNewMyTrade() ─────────┼──── HTTP POST ────┐               │
│  │  OnPositionChanged() ────┼──── (localhost)   │               │
│  │  [触发截图] ──────────────┼──── (可选)        │               │
│  └──────────────────────────┘                   │               │
└─────────────────────────────────────────────────┼───────────────┘
                                                  │
                                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  sigma-relay (Python, 本地常驻)                                   │
│                                                                  │
│  ┌──────────────────────────┐    ┌─────────────────────────┐   │
│  │  HTTP Server (FastAPI)   │───▶│  Trade Event Processor  │   │
│  │  POST /trade-event       │    │  - 聚合 partial fills   │   │
│  │  POST /position-closed   │    │  - 等待 position close  │   │
│  │  POST /screenshot        │    │  - 生成 draft markdown  │   │
│  └──────────────────────────┘    └────────────┬────────────┘   │
│                                                │                 │
│  ┌─────────────────────────────────────────────▼───────────────┐│
│  │  Output:                                                     ││
│  │  1. traders/default/trades/YYYY/MM/YYYY-MM-DD-<sym>-<dir>.md ││
│  │     (draft, 标记 [DRAFT - 待确认])                            ││
│  │  2. git add + commit "draft(<sym>): auto-captured"           ││
│  │  3. 推送通知 → WebUI / Telegram / 微信                        ││
│  └─────────────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
                                                  │
                                                  ▼
┌─────────────────────────────────────────────────────────────────┐
│  Agent (WebUI / Cursor / CLI)                                    │
│                                                                  │
│  用户收到通知 → 打开 draft → 补填：                                │
│  - §二 决策链 5 问（为什么做这笔？）                                │
│  - §四 盘后 EMA（情绪 + 学到什么？）                               │
│  - 确认/修正 auto-captured 数据                                   │
│  → Agent 标记 draft → final                                      │
└─────────────────────────────────────────────────────────────────┘
```

**优势**：
- 结构化数据直接从 ATAS 内存获取，零 OCR 误差
- 实时（成交后 < 1 秒触发）
- 自动聚合 partial fills（如你 2026-05-06 的 2 手分批开仓）
- 可自动关联 Playbook → `setup_tag`

**劣势 / 风险**：
- 需要写 C# 代码（ATAS 指标开发）
- 本地服务需要常驻运行
- ATAS 自定义指标的 HTTP 发送能力需验证是否可用 `System.Net.Http`（可能有沙箱限制）

---

### 方案 B：ATAS 统计导出 → 文件监控 → 解析（退化方案）

```
用户手动导出 xlsx → watchdog 监控目标文件夹 → 解析 xlsx → 生成 draft
```

**优势**：零 ATAS 插件开发
**劣势**：
- 不实时（依赖用户手动导出）
- 比 "C+D 手动填+周对账" 只省了"填模板"这一步，ROI 低
- xlsx 解析逻辑已在 `2026-05-06-atas-statistics-note.md` 中手工验证过，可复用

---

### 方案 C：ATAS Telegram Bot → Telegram Bot API → 中继（有限方案）

```
ATAS Alert → @atas_alerts_bot → 你的 Telegram Bot 监听 → 中继
```

**优势**：不需要写 C# 指标
**劣势**：
- ATAS Telegram alert 格式固定，**不包含全部交易字段**（无 entry_price 具体值、无 position_size、无 Playbook）
- 解析文本 alert 消息 ≈ 弱化版 OCR，可靠性不高
- Telegram Bot API 需要额外基础设施（轮询 / webhook server）

---

### 方案 D：截图 + Vision LLM OCR（最弱方案）

```
手动截图 / 热键截图 → Vision API (GPT-4o/Claude) → JSON → 生成 draft
```

**优势**：不需要任何 ATAS 插件
**劣势**：
- OCR 准确率对数字（价格）不够可靠——4722.0 vs 4772.0 差一位就是灾难
- design_proposal D6 §四.6 已明确评估 "OCR 极脆弱"（M 级结论）
- 延迟高（截图 → 上传 → API 调用 → 返回 ≈ 3-10 秒）
- 无法自动触发

---

### 方案 E（推荐）：A + 截图辅助

**主路径 = 方案 A**（结构化数据），**辅助路径 = 截图自动触发**：

```csharp
// SigmaBridge.cs 中
protected override void OnNewMyTrade(MyTrade myTrade) {
    PostToRelay(myTrade);           // 结构化数据
    TriggerScreenCapture();          // 可选：调用系统截图
}
```

截图不用于提取数据，仅存入 `screenshots/` 作为 §五 证据层——与 `SCREENSHOTS.md` 约定完全一致。

---

## 三、所需新建组件详细设计

### 3.1 组件 1：SigmaBridge（ATAS C# 自定义指标）

**文件位置**：`atas-plugin/SigmaBridge/SigmaBridge.cs`（新建）

**依赖**：
- ATAS.Indicators.dll（ATAS 安装目录）
- .NET Framework 或 .NET 6+（取决于 ATAS 版本）
- System.Net.Http / System.Text.Json

**核心逻辑**：

```csharp
using ATAS.Indicators;
using System.Net.Http;
using System.Text.Json;

public class SigmaBridge : ExtendedIndicator
{
    private static readonly HttpClient _http = new();
    private const string RelayUrl = "http://127.0.0.1:9733";

    protected override void OnNewMyTrade(MyTrade trade)
    {
        var payload = new {
            event_type = "new_trade",
            timestamp = DateTime.UtcNow.ToString("o"),
            symbol = TradingInfo.Security?.Symbol,
            price = trade.Price,
            quantity = trade.Quantity,
            side = trade.Direction.ToString(),
            account = TradingInfo.Portfolio?.AccountId,
            // playbook = GetPlaybookName(trade), // 如果可获取
        };
        _ = _http.PostAsync($"{RelayUrl}/trade-event",
            new StringContent(JsonSerializer.Serialize(payload),
                System.Text.Encoding.UTF8, "application/json"));
    }

    protected override void OnPositionChanged(Position position)
    {
        if (position.CurrentVolume == 0) // 完全平仓
        {
            var payload = new {
                event_type = "position_closed",
                timestamp = DateTime.UtcNow.ToString("o"),
                symbol = TradingInfo.Security?.Symbol,
                realized_pnl = position.RealizedPnL,
                avg_entry = position.AveragePrice,
                account = TradingInfo.Portfolio?.AccountId,
            };
            _ = _http.PostAsync($"{RelayUrl}/position-closed",
                new StringContent(JsonSerializer.Serialize(payload),
                    System.Text.Encoding.UTF8, "application/json"));
        }
    }
}
```

**安装**：编译为 DLL → 放入 `Documents/Advanced Time And Sales/Indicators/`

**未验证风险**：
1. ATAS 指标沙箱是否允许 `System.Net.Http`？（文档未明确禁止，Webhook 功能暗示可以）
2. `OnNewMyTrade` 在模拟盘/回放是否触发？（需测试）
3. 多图表挂载时是否重复触发？（需通过 trade ID 去重）

---

### 3.2 组件 2：sigma-relay（Python 本地常驻服务）

**文件位置**：`tools/sigma-relay/` （新建）

**依赖**：
- Python 3.10+
- FastAPI + uvicorn（HTTP 服务）
- openpyxl（可选，xlsx 解析备用路径）
- pyyaml（生成 frontmatter）
- watchdog（可选，文件监控备用）

**核心功能**：

```python
# tools/sigma-relay/server.py

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from pathlib import Path
import yaml

app = FastAPI()

# 状态：聚合 partial fills 直到 position_closed
open_positions: dict = {}  # key = (symbol, account)

class TradeEvent(BaseModel):
    event_type: str
    timestamp: str
    symbol: str
    price: float
    quantity: float
    side: str
    account: str | None = None

class PositionClosed(BaseModel):
    event_type: str
    timestamp: str
    symbol: str
    realized_pnl: float
    avg_entry: float
    account: str | None = None

@app.post("/trade-event")
async def handle_trade(event: TradeEvent):
    key = (event.symbol, event.account)
    if key not in open_positions:
        open_positions[key] = {
            "symbol": event.symbol,
            "direction": "long" if event.side == "Buy" else "short",
            "fills": [],
            "first_fill_time": event.timestamp,
            "account": event.account,
        }
    open_positions[key]["fills"].append({
        "price": event.price,
        "qty": event.quantity,
        "time": event.timestamp,
    })
    return {"status": "aggregating", "fills": len(open_positions[key]["fills"])}

@app.post("/position-closed")
async def handle_close(event: PositionClosed):
    key = (event.symbol, event.account)
    pos = open_positions.pop(key, None)
    if pos is None:
        # 没有对应的开仓记录——可能 relay 重启后丢失，容错处理
        pos = {"symbol": event.symbol, "direction": "unknown", "fills": []}

    draft = generate_trade_draft(pos, event)
    path = write_draft(draft)
    notify_user(path)
    return {"status": "draft_created", "path": str(path)}

def generate_trade_draft(pos, close_event):
    fills = pos.get("fills", [])
    total_qty = sum(f["qty"] for f in fills)
    avg_entry = sum(f["price"] * f["qty"] for f in fills) / total_qty if total_qty else 0

    return {
        "frontmatter": {
            "date": datetime.fromisoformat(close_event.timestamp).strftime("%Y-%m-%d"),
            "symbol": pos["symbol"],
            "direction": pos["direction"],
            "product_class": infer_product_class(pos["symbol"]),
            "market": infer_market(pos["symbol"]),
            "account": close_event.account or "",
            "entry_price": round(avg_entry, 2),
            "exit_price": None,  # position_closed 不直接给 exit_price，需从最后一笔 fill 推断
            "position_size": int(total_qty),
            "stop_loss_price": None,  # 需用户填写
            "pnl_gross": close_event.realized_pnl,
            "pnl_net": None,  # 需扣费
            "fees": None,     # 需用户确认
        },
        "fills": fills,
        "direction": pos["direction"],
    }
```

**关键设计决策**：
- **聚合 partial fills**：多笔成交合成一笔交易记录（与 2026-05-06 的 2 手分批场景匹配）
- **position_closed 作为"生成 draft"的触发器**：只有完全平仓才写 draft，持仓中的 fills 仅缓存
- **draft 标记**：生成的 markdown 文件顶部加 `<!-- DRAFT: auto-captured, pending user confirmation -->`
- **推送通知**：可选通道——WebUI 弹窗 / Telegram / 微信企业号 / 系统通知

---

### 3.3 组件 3：Agent 侧 trade-draft 接收与完善

**改动位置**：`webui/src/lib/tools.ts`（扩展现有 tool）

**新增能力**：
- `list_drafts` tool：列出所有标记为 DRAFT 的交易记录
- `finalize_draft` tool：将 draft 升级为 final，补填决策链 + EMA
- 通知渲染：WebUI 中显示 "新交易 draft 已生成，待补填决策链"

**或者**更简单的路径：sigma-relay 生成 draft 后直接 `git commit`，用户下次打开 WebUI/Cursor 时 Agent 主动识别 draft 文件并引导用户补填。

---

## 四、截图自动捕获（辅助路径）

### 4.1 方案 A：由 SigmaBridge 触发系统截图

```csharp
// 在 OnNewMyTrade 中
private void TriggerScreenCapture()
{
    // 方法 1：调用外部工具
    Process.Start("nircmd", "savescreenshot screenshots\\latest.png");
    // 方法 2：调用 Windows API
    // 方法 3：发 HTTP 给 sigma-relay，让 relay 调用截图
}
```

**风险**：ATAS 沙箱可能限制 `Process.Start`。备选：sigma-relay 收到 trade-event 后自行调 Windows 截图 API。

### 4.2 方案 B：AHK / PowerShell 热键截图

用户按热键（如 Ctrl+Shift+S）→ 截图保存到约定目录 → watchdog 检测新文件 → 关联到最近的 draft。

### 4.3 截图用途

截图**不用于 OCR 提取数据**。用途仅为：
1. 满足 `SCREENSHOTS.md` 约定的 "§五 截图证据"
2. 周复盘时 AI 可以"回到当时画面"做对照分析
3. 捕获 footprint / 热力图等无法从成交数据重建的视觉信息

---

## 五、你缺少什么（坦诚清单）

### 5.1 你需要学/做的 Skills

| # | 技能 | 当前水平 | 所需投入 | 为什么不能绕开 |
|---|------|----------|----------|----------------|
| 1 | **C# 基础 + ATAS Indicator SDK** | 零（假设） | 需阅读 ATAS 文档 + 写约 150 行 C# | ATAS 只支持 C# 指标，没有 Python/JS 选项 |
| 2 | **Visual Studio 构建 .NET 类库** | 可能有（如有 C# 经验则跳过） | 创建 Class Library → 引用 ATAS DLL → 编译 | 无法跳过——产出是 .dll 文件 |
| 3 | **本地 HTTP 服务运维** | 假设你用过 Python/Node | FastAPI 上手极快 | 需要 relay 常驻 |
| 4 | **Windows 任务计划 / 系统服务** | 基本了解 | 让 sigma-relay 开机自启 | 否则每次交易前要手动启动 |

### 5.2 你需要新建的 Plugins / 工具

| # | 名称 | 类型 | 位置 | 行数估计 |
|---|------|------|------|---------|
| 1 | **SigmaBridge** | ATAS C# DLL | `atas-plugin/SigmaBridge/` | ~200 行 |
| 2 | **sigma-relay** | Python 常驻服务 | `tools/sigma-relay/` | ~400 行 |
| 3 | **draft-template** 渲染器 | Python/Jinja2 | `tools/sigma-relay/templates/` | ~100 行 |
| 4 | **通知推送模块** | Python | `tools/sigma-relay/notify.py` | ~80 行 |
| 5 | **WebUI draft indicator**（可选） | TypeScript | `webui/src/` | ~50 行 |

### 5.3 基础设施需求

| 需求 | 说明 |
|------|------|
| Windows 本地运行 | ATAS 只运行在 Windows；sigma-relay 也跑在同机（localhost 通信） |
| Python 3.10+ | sigma-relay 依赖 |
| .NET SDK（或 Visual Studio） | 编译 SigmaBridge.dll |
| 端口 9733（本地） | sigma-relay 监听地址，仅 127.0.0.1 |

---

## 六、实施路径（按依赖关系排序）

### Phase 1：验证 ATAS C# HTTP 发送可行性（最高风险，先做）

1. 创建最小 C# 指标：`OnNewMyTrade` → `Console.WriteLine` / 写本地文件
2. 确认事件在实盘/模拟盘中触发
3. 尝试 `HttpClient.PostAsync` 到 localhost——如果沙箱阻止，需找替代方案（写文件 → watchdog）

**如果此步失败**：退化到方案 B（文件监控 + 手动导出），ROI 大幅降低但仍可做。

### Phase 2：sigma-relay 本地服务

1. FastAPI 服务 + trade event / position closed 两个端点
2. Partial fill 聚合逻辑
3. Draft markdown 模板生成（复用 TEMPLATE.md 格式）
4. `git add + commit` 自动化

### Phase 3：端到端测试

1. ATAS 模拟盘下单 → SigmaBridge 捕获 → relay 接收 → draft 生成
2. 验证 partial fills 聚合（模拟 2 手分批场景）
3. 验证 draft 文件格式与现有 trades/ 记录兼容

### Phase 4：截图辅助 + 通知

1. 接入系统级截图（AHK 热键或 SigmaBridge 触发）
2. 通知推送通道选择与实现
3. WebUI 中 draft 标记展示

---

## 七、与现有 D6 设计决策的关系

原 D6 选择了"C+D"：
> **推荐 = C（手动复盘）+ D（周批量对账）混合**——A 股零售无 broker API（§四.6），不投入 OCR / API 工程预算。

**本方案与 D6 的关系**：
- **不是替代 D6，是 D6 的增强层**。周批量对账（reconcile_funds.py）仍然保留作为最终校验
- 原 D6 的核心论据是"A 股零售券商无 broker API"——**但你目前交易的是 CME 期货、用的是 ATAS**，这个约束不适用
- 本方案专注于 ATAS → σ 的实时通道；A 股部分（如果未来涉及）仍走 D6 原路径
- reconcile_funds.py 从"唯一校验"升级为"二次确认"——如果 relay 漏捕了某笔（如 relay 宕机），周对账仍能兜底

---

## 八、替代方案快速否决记录

| 方案 | 否决理由 |
|------|----------|
| OCR 截图 → 提取价格 | D6 §四.6 已评估"OCR 极脆弱"；4722.0 vs 4772.0 一位之差是灾难 |
| 只用 Telegram Alert | ATAS alert 格式固定，不含完整交易数据（无 entry_price / size） |
| 手动导出 xlsx + watchdog | 不实时；比现有"手填"只省 30 秒/笔，ROI 不值 |
| Broker API（IB/CQG） | 可行但绕过了 ATAS（你的主分析工具），且需要单独的 API 认证流程 |

---

## 九、开放问题（需要你确认）

1. **ATAS 版本**：你用的是 ATAS 正式版还是评估版？评估版可能限制自定义指标（xlsx 导出中有 "Evaluation Warning" sheet）
2. **C# 开发环境**：你的 Windows 机器上是否已装 Visual Studio 或 .NET SDK？
3. **数据馈送源（datafeed）**：你通过哪个 connector 连 CME（CQG / Rithmic / 其他）？这影响 `MyTrade` 对象的字段完整度
4. **热力图/Footprint 截图需求**：你是否需要在成交时自动截图？还是手动截就够？
5. **通知偏好**：draft 生成后你希望怎么知道？Telegram / 微信 / 系统弹窗 / WebUI badge？

---

## 十、下一步

如果你确认要走这条路（方案 A/E），我的建议是：

1. **立刻做**：Phase 1 验证（最小 C# 指标 + HTTP POST）—— 这是整条链的最大未知数
2. **同步做**：我可以先把 sigma-relay 的 Python 代码骨架写出来（不依赖 Phase 1 结果）
3. **决策点**：Phase 1 如果发现 ATAS 沙箱阻止 HTTP，则退化到"写文件 + watchdog"路径（仍可实时，只是多一层间接）

---

*文档版本：v0.1 | 生成日期：2026-05-08 | 诚实标记：ATAS API 信息为 M 级（官方文档）；架构方案为 U 级（逻辑推演，未经实测验证）*
