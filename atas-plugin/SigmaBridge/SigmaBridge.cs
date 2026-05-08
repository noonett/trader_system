using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;
using ATAS.Indicators;

namespace SigmaBridge
{
    /// <summary>
    /// σ 系统桥接指标 — 捕获交易事件并推送到 sigma-relay 本地服务。
    /// 安装：编译为 DLL 后放入 Documents/Advanced Time And Sales/Indicators/
    /// 需要挂载到你正在交易的图表上才能接收事件。
    /// </summary>
    [DisplayName("σ SigmaBridge")]
    public class SigmaBridge : ExtendedIndicator
    {
        private static readonly HttpClient Http = new()
        {
            Timeout = TimeSpan.FromSeconds(3)
        };

        private const string DefaultRelayUrl = "http://127.0.0.1:9733";
        private const int DedupeWindowSize = 50;

        [Display(Name = "Relay URL", GroupName = "σ Config")]
        public string RelayUrl { get; set; } = DefaultRelayUrl;

        [Display(Name = "Enable Screenshot Trigger", GroupName = "σ Config")]
        public bool EnableScreenshot { get; set; } = false;

        [Display(Name = "Screenshot Tool Path", GroupName = "σ Config")]
        public string ScreenshotToolPath { get; set; } = "nircmd.exe";

        private readonly LinkedList<string> _recentTradeIds = new();
        private readonly HashSet<string> _recentTradeIdSet = new();

        protected override void OnCalculate(int bar, decimal value)
        {
            // 指标主计算循环 — SigmaBridge 不绘图，仅监听事件
        }

        protected override void OnNewMyTrade(MyTrade trade)
        {
            var tradeId = $"{trade.Time:yyyyMMddHHmmssfff}_{trade.Price}_{trade.Quantity}";
            if (_recentTradeIdSet.Contains(tradeId)) return;

            _recentTradeIdSet.Add(tradeId);
            _recentTradeIds.AddLast(tradeId);
            while (_recentTradeIds.Count > DedupeWindowSize)
            {
                var oldest = _recentTradeIds.First.Value;
                _recentTradeIds.RemoveFirst();
                _recentTradeIdSet.Remove(oldest);
            }

            var payload = new
            {
                event_type = "new_trade",
                timestamp = DateTime.UtcNow.ToString("o"),
                local_time = trade.Time.ToString("o"),
                symbol = TradingInfo?.Security?.Symbol ?? "UNKNOWN",
                price = trade.Price,
                quantity = trade.Quantity,
                side = trade.Direction.ToString(),
                account = TradingInfo?.Portfolio?.AccountId ?? "",
                trade_id = tradeId
            };

            _ = PostAsync("/trade-event", payload);

            if (EnableScreenshot)
            {
                TriggerScreenCapture(TradingInfo?.Security?.Symbol ?? "unknown");
            }
        }

        protected override void OnPositionChanged(Position position)
        {
            if (position.CurrentVolume != 0) return; // 仅关注完全平仓

            var payload = new
            {
                event_type = "position_closed",
                timestamp = DateTime.UtcNow.ToString("o"),
                symbol = TradingInfo?.Security?.Symbol ?? "UNKNOWN",
                realized_pnl = position.RealizedPnL,
                avg_entry_price = position.AveragePrice,
                account = TradingInfo?.Portfolio?.AccountId ?? ""
            };

            _ = PostAsync("/position-closed", payload);
        }

        protected override void OnOrderChanged(Order order)
        {
            if (order.Type == OrderType.Stop || order.Type == OrderType.StopLimit)
            {
                var payload = new
                {
                    event_type = "stop_order_update",
                    timestamp = DateTime.UtcNow.ToString("o"),
                    symbol = TradingInfo?.Security?.Symbol ?? "UNKNOWN",
                    order_state = order.State.ToString(),
                    stop_price = order.StopPrice,
                    order_type = order.Type.ToString(),
                    side = order.Direction.ToString(),
                    account = TradingInfo?.Portfolio?.AccountId ?? ""
                };

                _ = PostAsync("/order-update", payload);
            }
        }

        private async Task PostAsync(string endpoint, object payload)
        {
            try
            {
                var json = JsonSerializer.Serialize(payload);
                var content = new StringContent(json, Encoding.UTF8, "application/json");
                using var response = await Http.PostAsync($"{RelayUrl}{endpoint}", content);
                response.EnsureSuccessStatusCode();
            }
            catch (Exception ex)
            {
                LogError($"SigmaBridge POST {endpoint} failed: {ex.Message}");
            }
        }

        private void TriggerScreenCapture(string symbol)
        {
            try
            {
                var filename = $"sigma_capture_{DateTime.Now:yyyyMMdd_HHmmss}_{symbol}.png";
                var targetDir = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments)
                    + "\\sigma-screenshots";
                System.IO.Directory.CreateDirectory(targetDir);
                var fullPath = $"{targetDir}\\{filename}";

                System.Diagnostics.Process.Start(new System.Diagnostics.ProcessStartInfo
                {
                    FileName = ScreenshotToolPath,
                    Arguments = $"savescreenshot \"{fullPath}\"",
                    CreateNoWindow = true,
                    UseShellExecute = false
                });
            }
            catch (Exception ex)
            {
                LogError($"Screenshot capture failed: {ex.Message}");
            }
        }

        private void LogError(string message)
        {
            // ATAS 内建日志 — 具体 API 需查文档确认
            System.Diagnostics.Debug.WriteLine($"[SigmaBridge] {message}");
        }
    }
}
