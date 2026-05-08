# SigmaBridge — ATAS → σ 系统桥接指标

## 用途

捕获 ATAS 中的交易成交事件，实时推送到本地 sigma-relay 服务，自动生成交易记录草稿。

## 前置条件

| 需求 | 说明 |
|------|------|
| Windows 10/11 | ATAS 只运行在 Windows |
| ATAS 正式版 | 评估版可能限制自定义指标 |
| .NET 8 SDK | 仅 CLI 工具，不需要 Visual Studio（~200MB） |
| dxfeed 连接 | 你当前的 CME datafeed |

## 安装 .NET SDK（轻量方案，无需 Visual Studio）

```powershell
# 方法 1：winget（推荐，一行搞定）
winget install Microsoft.DotNet.SDK.8

# 方法 2：手动下载
# 访问 https://dotnet.microsoft.com/download/dotnet/8.0
# 选 "SDK" → Windows x64 → Installer
# 安装后重启终端

# 验证安装
dotnet --version
# 应输出 8.x.xxx
```

**为什么不需要 Visual Studio**：`dotnet build` CLI 是独立的编译器。VS 是 IDE + 调试器 + 设计器的全家桶（~40GB），写一个 150 行的 DLL 完全用不上。你用 VS Code、Notepad++ 甚至记事本编辑 .cs 文件，然后命令行 `dotnet build` 即可。

## 编译

```powershell
# 1. 找到 ATAS 安装目录中的 ATAS.Indicators.dll
#    典型路径（检查你的实际安装位置）：
#      C:\Program Files\ATAS Platform\
#      %LOCALAPPDATA%\ATAS Platform\

# 2. 创建 lib 目录并复制 DLL
cd atas-plugin\SigmaBridge
mkdir ..\..\lib 2>$null
copy "C:\Program Files\ATAS Platform\ATAS.Indicators.dll" ..\..\lib\

# 3. 编译
dotnet build -c Release

# 产出位置：bin\Release\net8.0-windows\SigmaBridge.dll
```

如果 ATAS 使用的 .NET 版本与 net8.0 不匹配（编译报错），编辑 `SigmaBridge.csproj` 中的 `<TargetFramework>` 改为对应版本（如 `net6.0-windows`）。

## 安装到 ATAS

```powershell
# 复制编译产物到 ATAS 指标目录
copy bin\Release\net8.0-windows\SigmaBridge.dll ^
  "%USERPROFILE%\Documents\Advanced Time And Sales\Indicators\"

# 重启 ATAS
```

重启 ATAS 后：
1. 打开你正在交易的图表（dxfeed 连接的）
2. 添加指标 → 搜索 "σ SigmaBridge"
3. 在设置面板中确认 Relay URL 为 `http://127.0.0.1:9733`
4. 如需自动截图，开启 "Enable Screenshot Trigger"

## 配置参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| Relay URL | `http://127.0.0.1:9733` | sigma-relay 服务地址 |
| Enable Screenshot | `false` | 成交时是否由 ATAS 侧触发截图（备选方案；推荐使用 sigma-relay 侧的 `mss` 截图） |
| Screenshot Tool Path | `nircmd.exe` | ATAS 侧截图工具路径（仅在 Enable Screenshot = true 时生效） |

## 数据流

```
OnNewMyTrade ─────────────> POST /trade-event    (每次成交)
OnPositionChanged (vol=0) → POST /position-closed (完全平仓)
OnOrderChanged (stop) ────> POST /order-update    (止损单变更)
```

## dxfeed 注意事项

- dxfeed 提供的 `MyTrade.Time` 通常为 **exchange time**（CME = US/Central）
- sigma-relay 中的时间戳以 UTC 存储，显示时按 `config.yaml` 中的 `preferences.timezone` 转换
- dxfeed 的 Symbol 格式可能包含合约月份后缀（如 `MGCM2026`），draft_generator 会自动清理

## 故障排查

| 现象 | 原因 | 解决 |
|------|------|------|
| 编译报错 "ATAS.Indicators not found" | DLL 路径错误 | 确认 `lib\ATAS.Indicators.dll` 存在 |
| 挂载后无事件触发 | 未在活跃图表上挂载 | 确保挂载到 dxfeed 连接的、有交易活动的图表 |
| 模拟盘不触发 | 部分 connector 模拟盘不走 OnNewMyTrade | 用最小实盘单验证（1 手 MGC） |
| HTTP POST 超时 | sigma-relay 未启动 | 先启动 `python server.py`，确认 9733 端口监听 |
| HTTP 被沙箱阻止 | ATAS 安全策略 | 退化方案：改为写本地文件，sigma-relay 用 watchdog 监控 |

## 退化方案（如果 HTTP 被阻止）

如果 ATAS 沙箱限制 `System.Net.Http`，改为文件输出模式：

```csharp
// 替换 PostAsync 为：
var json = JsonSerializer.Serialize(payload);
File.AppendAllText(@"C:\sigma-events\events.jsonl", json + "\n");
```

sigma-relay 侧用 Python `watchdog` 监控 `C:\sigma-events\events.jsonl` 的变化。
