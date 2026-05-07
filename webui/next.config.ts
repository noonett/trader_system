import type { NextConfig } from "next";

// Next 16: explicit empty turbopack block when not using custom webpack (avoids build warning).
const nextConfig: NextConfig = {
  turbopack: {},
  // Playwright / 多 Host 访问 dev 时避免 HMR 跨源被拦（控制台刷屏且可能影响热更新）
  allowedDevOrigins: ["127.0.0.1", "localhost"],
};

export default nextConfig;
