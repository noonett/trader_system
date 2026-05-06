# trades/ — σ 系统交易记录

## 目录结构

```
trades/
├── README.md          ← 本文件
├── TEMPLATE.md        ← v0 交易记录模板（复制到 YYYY/MM/ 下使用）
├── SCREENSHOTS.md     ← 截图命名约定与工作流
└── YYYY/MM/
    ├── YYYY-MM-DD-<symbol>-<dir>.md  ← 每笔交易一文聚合
    └── screenshots/                   ← 交易截图（入场/出场/过程）
        ├── YYYY-MM-DD-<symbol>-<dir>-entry-1.png
        ├── YYYY-MM-DD-<symbol>-<dir>-exit-1.png
        └── YYYY-MM-DD-<symbol>-<dir>-context-1.png  (可选)
```

## 使用方法

1. 每次开仓前，复制 `TEMPLATE.md` 到 `YYYY/MM/YYYY-MM-DD-<symbol>-<dir>.md`
2. 填写 frontmatter（日期 / 标的 / 方向 / **product_class** / 市场 / 价格 / 仓位 / 止损）
3. 填写 §二 决策链 5 项 if-then
4. **截图当时的 K 线画面**（入场位/止损位可见）
5. `git add + commit "open <symbol>"`
6. 实际下单
7. 平仓后 30 分钟内填写 §四 盘后 EMA
8. **截图平仓时的 K 线画面**
9. `git add + commit "close <symbol>"`
10. **把截图贴给 AI**（对话中发图 + 说一句"这是 XX 的入场/出场"）→ AI 处理命名、归档、更新 §五

## product_class 枚举（产品分级，foundation §三.10）


| 值                     | 含义                                                 | 约束                                            |
| --------------------- | -------------------------------------------------- | --------------------------------------------- |
| `green-passive-etf`   | 低成本被动 ETF                                          | 默认允许（仍受决策链 + 仓位规则约束）                          |
| `green-cash-stock`    | 低杠杆现金股票 / 长期价值标的                                   | 默认允许                                          |
| `yellow-small-future` | 低杠杆 + 明确合约规格 + 可计算最大损失的小型期货合约（如 MGC、MES、CN50 mini） | 叠加额外门禁（决策链 5 问 + 单笔风险预算 + 每周交易次数硬上限）          |
| `red`                 | 0DTE 期权 / 超高杠杆永续合约 / 无法定义最大损失的产品 / 无可靠止损机制的产品      | **pre-commit hook 拒绝 commit**——如果绕过，后台违规扫描会抓到 |


## 关于旧交易记录

[trades/2026/05/2026-05-04-mgc-202606-long.md](2026/05/2026-05-04-mgc-202606-long.md) 是用户在旧 Stage 0 下记录的真实交易——保留在原位。格式与 v0 新模板不完全一致——v0 KPI 计算从 v0 启动日开始，不回溯。