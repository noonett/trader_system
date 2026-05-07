# σ 触发型邮件 Alert — cron 配置参考

> 对应 design_proposal_2026.md §三.2.4。
> 当 KPI alert / 违规扫描产生新文件时，通过邮件通知用户。
> 推送延迟 5-30 分钟可接受（离线批处理，不是实时触发）。

## 前置条件

- 本地或服务器上可发邮件（`sendmail` / `msmtp` / `postfix` / SMTP relay 任选）
- cron 或 launchd 可用

## 方案 A：cron + msmtp（推荐，最简）

### 1. 安装 msmtp

```bash
# macOS
brew install msmtp

# Ubuntu/Debian
sudo apt-get install msmtp msmtp-mta
```

### 2. 配置 ~/.msmtprc

```
account default
host smtp.gmail.com
port 587
from your-email@gmail.com
auth on
user your-email@gmail.com
password your-app-password
tls on
tls_starttls on
logfile ~/.msmtp.log
```

> 使用 Gmail 时需生成 App Password（不是账户密码）。
> 也可用其他 SMTP 服务（QQ邮箱、163、SendGrid 等）。

### 3. 配置 cron

```bash
crontab -e
```

添加以下两行：

```cron
# 每周日 21:00 检查本周是否有新 alert
0 21 * * 0 /workspace/scripts/check_and_email_alert.sh

# 每月最后一天 21:30 检查月度 KPI alert
30 21 28-31 * * [ "$(date -d tomorrow +\%d)" = "01" ] && /workspace/scripts/check_and_email_alert.sh
```

### 4. alert 检查脚本（参考）

创建 `scripts/check_and_email_alert.sh`：

```bash
#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"
ALERTS_DIR="$WORKSPACE/reviews/alerts"
RECIPIENT="your-email@example.com"

# 查找最近 7 天内创建的 alert 文件
recent=$(find "$ALERTS_DIR" -name "*-alert.md" -mtime -7 2>/dev/null | head -5)

if [ -z "$recent" ]; then
    exit 0
fi

# 拼接邮件正文
body="σ 系统检测到以下 KPI alert 需要 acknowledge:\n\n"
for f in $recent; do
    # 只取 acknowledge 状态行
    acked=$(grep -c '\[x\]' "$f" 2>/dev/null || echo "0")
    total=$(grep -c '\[ \]' "$f" 2>/dev/null || echo "0")
    body+="- $(basename "$f"): $acked/$((acked + total)) 已 acknowledge\n"
done
body+="\n请在 Cursor 中打开 reviews/alerts/ 处理。"

echo -e "$body" | mail -s "⚠ σ KPI Alert 待处理" "$RECIPIENT"
```

```bash
chmod +x scripts/check_and_email_alert.sh
```

## 方案 B：macOS launchd（无 cron 时）

创建 `~/Library/LaunchAgents/com.sigma.alert-check.plist`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.sigma.alert-check</string>
    <key>ProgramArguments</key>
    <array>
        <string>/workspace/scripts/check_and_email_alert.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Weekday</key>
        <integer>0</integer>
        <key>Hour</key>
        <integer>21</integer>
        <key>Minute</key>
        <integer>0</integer>
    </dict>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.sigma.alert-check.plist
```

---

## 不采纳的方案（design §二 D4）

| 方案 | 原因 |
|---|---|
| Telegram bot | Phase 3d 评估；当前无强需求 + 引入外部依赖 |
| 微信公众号推送 | 合规模糊 + §收敛信号 6 "微信群是冲动种子源"反激励 |
| 实时 JITAI 推送 | σ 无传感器/无实时数据流；离线批处理是次优近似 |

*版本：v0.1 | 来源：design_proposal §三.2.4 + §二 D4*
