# reviews/ — σ 系统复盘 + 后台强制风控输出

## 目录结构

```
reviews/
├── README.md           ← 本文件
├── weekly/             ← 周复盘
│   ├── YYYY-WW.md      ← 用户手写人工 review
│   └── YYYY-WW-auto.md ← AI 后台批处理自动生成（scripts/weekly_report.sh）
├── monthly/            ← 月校准
│   ├── YYYY-MM.md      ← 用户手写月校准
│   └── YYYY-MM-auto.md ← AI 后台批处理自动生成（scripts/monthly_calibration.sh）
├── violations/         ← 后台违规扫描结果（A 类，scripts/violations_scan.py）
│   └── YYYY-WW.md      ← 5 类违规检测：
│                          1. 未写规则有交易
│                          2. 决策链跳过
│                          3. 仓位超阈值
│                          4. 止损穿越未平仓（处置效应）
│                          5. 红区产品出现
├── alerts/             ← KPI 退化 alert（B 类，scripts/kpi_alert.py）
│   └── YYYY-MM-DD-alert.md  ← 含 acknowledge 字段；
│                               未 acknowledge 时 sigma/daily/ 顶部 emit banner
└── reconcile/          ← 训练资金对账（D 类，Phase 3b scripts/reconcile_funds.py）
    └── YYYY-WW.md
```

## 工作流

**每周末**：
1. 跑 `make weekly-report` → AI 生成 reviews/weekly/YYYY-WW-auto.md
2. 跑 `make violations-scan` → 生成 reviews/violations/YYYY-WW.md
3. 读两份自动报告
4. 复制 sigma/weekly-review.md → reviews/weekly/YYYY-WW.md 填写人工 review
5. git add + commit

**每月末**：
1. 跑 `make monthly-calibration` → AI 生成 reviews/monthly/YYYY-MM-auto.md + KPI alert 检测
2. 复制 sigma/monthly-calibration.md → reviews/monthly/YYYY-MM.md 填写月校准
3. git add + commit

**KPI alert 触发时**（自动）：
- scripts/kpi_alert.py 检测到退化条件 → 生成 reviews/alerts/YYYY-MM-DD-alert.md
- 用户必须去 alerts/ 文件里填 acknowledge 字段
- 未 acknowledge = 下次写盘前规则时顶部有 banner 提醒
