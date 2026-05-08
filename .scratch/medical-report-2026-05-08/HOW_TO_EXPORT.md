# 如何把这 6 份报告导入飞书 —— 两条路径

> 当前状态：6 份 markdown 文档已生成在 `/tmp/medical-report/`，但**Cloud Agent 这边没有浏览器，无法完成飞书 OAuth 授权**。所以最后一步需要你在自己电脑或手机上完成。

---

## 🚀 路径 A（推荐 · 5 分钟搞定 · 适合今晚）：直接复制粘贴

**飞书原生支持 markdown 粘贴**——粘贴后会自动渲染表格、标题、列表、代码块等格式。

### 操作步骤

1. **在飞书新建一个文件夹**：
   - 打开飞书 → 文档 → 新建文件夹 → 命名 "钟钊灵病情家属备查"

2. **创建 6 个文档**，依次复制粘贴每份内容：

   | 序号 | 文档标题（建议） | 内容来源 |
   |---|---|---|
   | 1 | 00 索引 - 钟钊灵病情家属备查 | `README_索引.md` |
   | 2 | 00 必读 · 今晚行动 | `00_必读_今晚行动.md` |
   | 3 | 01 病情整合分析 | `01_病情整合分析.md` |
   | 4 | 02 问医生清单 + 红线症状 | `02_问医生清单_红线症状.md` |
   | 5 | 03 家庭行动方案 | `03_家庭行动方案.md` |
   | 6 | 04 医生评估 + 二诊路径 | `04_医生评估_二诊路径.md` |

3. **每份文档的操作**：
   - 在飞书新建文档
   - 直接 Ctrl+V / Cmd+V 粘贴 markdown 内容
   - 飞书会自动识别 `#` 标题、`|` 表格、`-` 列表、` ``` ` 代码块
   - 偶尔表格边框对齐有问题，手动微调即可

### 怎么拿到 markdown 内容？

Cloud Agent 这一侧文件在 `/tmp/medical-report/`。三种方式获取：

#### 方式 1：直接从对话里复制

往上翻这个对话，每份文档的内容我已经写在了对话里（前面 5 个 Write 工具调用的内容）。直接选中复制即可。

#### 方式 2：让我把文件内容回显到对话

直接告诉我："把 X 文档内容贴到对话里"——我会用文本输出整个文件。

#### 方式 3：commit 到一个临时分支再拉到本地

```bash
# 在 cloud agent 这边执行
cd /workspace
git checkout -b cursor/medical-report-temp-82f4
mkdir -p .scratch/medical
cp /tmp/medical-report/*.md /tmp/medical-report/*.sh .scratch/medical/
git add .scratch/medical
git commit -m "temp: medical report files for export"
git push -u origin cursor/medical-report-temp-82f4

# 然后在你本机
git fetch origin
git checkout cursor/medical-report-temp-82f4
ls .scratch/medical/   # 6 个文档 + 1 个上传脚本
```

⚠️ 这种方式会留临时分支在 sigma 仓库里，导出完成后建议删除。

---

## 🤖 路径 B（一次设置 · 长期可用）：lark-cli 一键上传

适合：你以后还会经常用飞书做笔记导出。

### 一次性设置（在你**本机** macOS / Windows / Linux 上）

#### Step 1：安装 lark-cli

```bash
npm install -g @larksuite/cli
```

#### Step 2：创建飞书自建应用 + 绑定 CLI

```bash
lark-cli config init --new
```

这条命令会：
- 给出一个**浏览器 URL**
- 你在浏览器里登录飞书 → 创建一个自建应用 → 给它加权限（docs / drive / wiki）→ 把应用 id/secret 自动同步回 CLI
- 整个过程约 3 分钟

#### Step 3：完成 OAuth 设备授权

```bash
lark-cli auth login --domain docs,drive,wiki
```

CLI 会输出一个 device URL，你在浏览器打开授权即可。

#### Step 4：拿到 6 份文档（从 cloud agent）

把 `/tmp/medical-report/*.md` + `upload-to-feishu.sh` 拷贝到本机。可以用上面的"方式 3"git 拉取，或者让我把内容输出到对话再保存。

#### Step 5：上传

```bash
cd /path/to/medical-report
chmod +x upload-to-feishu.sh
bash upload-to-feishu.sh
```

如果想上传到指定文件夹，先在飞书创建文件夹，URL 中拿到 folder_token：

```
https://xxx.feishu.cn/drive/folder/[FOLDER_TOKEN]
                                    ^^^^^^^^^^^^^^
```

然后：

```bash
bash upload-to-feishu.sh FOLDER_TOKEN
```

---

## 💡 我的建议

**今晚**：用**路径 A**（复制粘贴）。5 分钟搞定，不用学新工具。

**等下次想批量做笔记导出**：再投资学路径 B。

---

## 文件清单（在 /tmp/medical-report/）

```
/tmp/medical-report/
├── README_索引.md            ← 总览 + 一段话总结
├── 00_必读_今晚行动.md        ← 1 页纸紧急行动
├── 01_病情整合分析.md          ← 完整临床分析
├── 02_问医生清单_红线症状.md   ← 13 问 + 急诊触发 + 监测节奏
├── 03_家庭行动方案.md          ← 饮食 + 分工 + 日记 + 时间线
├── 04_医生评估_二诊路径.md     ← 医生评估 + 上级医院推荐
├── HOW_TO_EXPORT.md          ← 本文档
└── upload-to-feishu.sh       ← 一键上传脚本
```
