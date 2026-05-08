using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading;
using System.Threading.Tasks;
using ATAS.Indicators;

namespace SigmaBridge
{
    /// <summary>
    /// σ 系统桥接指标 — 捕获交易事件并推送到 sigma-relay 本地服务。
    /// 安装：编译为 DLL 后放入 Documents/Advanced Time And Sales/Indicators/
    /// 需要挂载到你正在交易的图表上才能接收事件。
    /// 多图表挂载安全：去重集合为 static，所有实例共享。
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

        // Static: shared across all indicator instances (multi-chart scenario).
        // Lock protects concurrent access from different chart threads.
        private static readonly object DedupeLock = new();
        private static readonly LinkedList<string> RecentTradeIds = new();
        private static readonly HashSet<string> RecentTradeIdSet = new();

        [Display(Name = "Relay URL", GroupName = "σ Config")]
        public string RelayUrl { get; set; } = DefaultRelayUrl;

        [Display(Name = "Enable Screenshot Trigger", GroupName = "σ Config")]
        public bool EnableScreenshot { get; set; } = false;

        [Display(Name = "Screenshot Tool Path", GroupName = "σ Config")]
        public string ScreenshotToolPath { get; set; } = "nircmd.exe";

        protected override void OnCalculate(int bar, decimal value)
        {
        }

        protected override void OnNewMyTrade(MyTrade trade)
        {
            var symbol = TradingInfo?.Security?.Symbol ?? "UNKNOWN";
            var account = TradingInfo?.Portfolio?.AccountId ?? "";
            var timeTicksUtc = trade.Time.ToUniversalTime().Ticks;
            var tradeId = $"{symbol}|{account}|{trade.Direction}|{timeTicksUtc}|{trade.Price}|{trade.Quantity}";

            lock (DedupeLock)
            {
                if (RecentTradeIdSet.Contains(tradeId)) return;

                RecentTradeIdSet.Add(tradeId);
                RecentTradeIds.AddLast(tradeId);
                while (RecentTradeIds.Count > DedupeWindowSize)
                {
                    var oldest = RecentTradeIds.First.Value;
                    RecentTradeIds.RemoveFirst();
                    RecentTradeIdSet.Remove(oldest);
                }
            }

            var payload = new
            {
                event_type = "new_trade",
                timestamp = DateTime.UtcNow.ToString("o"),
                local_time = trade.Time.ToString("o"),
                symbol = symbol,
                price = trade.Price,
                quantity = trade.Quantity,
                side = trade.Direction.ToString(),
                account = account,
                trade_id = tradeId
            };

            FireAndForget(PostAsync("/trade-event", payload));

            if (EnableScreenshot)
            {
                TriggerScreenCapture(TradingInfo?.Security?.Symbol ?? "unknown");
            }
        }

        protected override void OnPositionChanged(Position position)
        {
            if (position.CurrentVolume != 0) return;

            var payload = new
            {
                event_type = "position_closed",
                timestamp = DateTime.UtcNow.ToString("o"),
                symbol = TradingInfo?.Security?.Symbol ?? "UNKNOWN",
                realized_pnl = position.RealizedPnL,
                avg_entry_price = position.AveragePrice,
                account = TradingInfo?.Portfolio?.AccountId ?? ""
            };

            FireAndForget(PostAsync("/position-closed", payload));
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

                FireAndForget(PostAsync("/order-update", payload));
            }
        }

        private async Task PostAsync(string endpoint, object payload)
        {
            var json = JsonSerializer.Serialize(payload);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            using var response = await Http.PostAsync($"{RelayUrl}{endpoint}", content);
            response.EnsureSuccessStatusCode();
        }

        /// <summary>
        /// Safely observes a Task without awaiting it in synchronous event handlers.
        /// Logs any exceptions rather than letting them go unobserved.
        /// </summary>
        private void FireAndForget(Task task)
        {
            task.ContinueWith(t =>
            {
                if (t.IsFaulted && t.Exception != null)
                {
                    foreach (var ex in t.Exception.InnerExceptions)
                    {
                        LogError($"SigmaBridge async error: {ex.Message}");
                    }
                }
            }, TaskContinuationOptions.OnlyOnFaulted);
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
            System.Diagnostics.Debug.WriteLine($"[SigmaBridge] {message}");
        }
    }
}
