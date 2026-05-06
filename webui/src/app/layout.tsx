import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "σ Trading System",
  description: "Agent-assisted trading training workflow",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="zh-CN" className="dark">
      <body className="antialiased">{children}</body>
    </html>
  );
}
