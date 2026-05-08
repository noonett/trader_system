# SigmaBridge — ATAS → σ 系统桥接指标

## 用途

捕获 ATAS 中的交易成交事件，实时推送到本地 sigma-relay 服务，自动生成交易记录草稿。

## 前置条件

1. Windows + ATAS 正式版（评估版可能限制自定义指标）
2. .NET 6 SDK 或 Visual Studio 2022+
3. ATAS 安装目录中的 `ATAS.Indicators.dll`

## 编译

```bash
# 将 ATAS.Indicators.dll 复制到 lib/ 目录（或修改 .csproj 中的 HintPath）
mkdir ..\..\lib
copy "C:\Program Files\ATAS Platform\ATAS.Indicators.dll" ..\..\lib\

# 编译
dotnet build -c Release
```

## 安装

```bash
# 将编译产物复制到 ATAS 指标目录
copy bin\Release\net6.0-windows\SigmaBridge.dll ^
  "%USERPROFILE%\Documents\Advanced Time And Sales\Indicators\"
```

重启 ATAS 后，在指标列表中搜索 "σ SigmaBridge"，挂载到你交易的图表上。

## 配置

挂载后可在指标设置面板中配置：

| 参数 | 默认值 | 说明 |
|------|--------|------|
| Relay URL | `http://127.0.0.1:9733` | sigma-relay 服务地址 |
| Enable Screenshot | `false` | 成交时是否自动截图 |
| Screenshot Tool Path | `nircmd.exe` | 截图工具路径（需安装 NirCmd 或替换为其他工具） |

## 数据流

```
OnNewMyTrade → POST /trade-event    (每次成交)
OnPositionChanged → POST /position-closed (完全平仓时)
OnOrderChanged → POST /order-update  (止损单变更时)
```

## 注意事项

- 仅挂载到一个图表上即可（多图表会触发去重逻辑）
- sigma-relay 未启动时静默失败，不影响交易
- 模拟盘中事件是否触发需实测确认
