---
name: job-apply-cv
description: Anson 的一鍵求職自動化流程。每當 Anson 貼上 LinkedIn 或 JobsDB 職位連結並要求申請或改CV時觸發。觸發詞包括：「幫我改CV [URL]」、「幫我申請呢份工」、「CV針對呢個JD」、「apply for this job」、「改CV申請」、「度身訂造CV」，或任何含有求職平台連結 + CV相關請求的訊息。此 Skill 自動完成：抓取JD → 深度分析 → 載入現有CV → 5步驟優化 → 生成PDF → 儲存至CVdraft → 建立Notion申請記錄，一氣呵成。
---

# Job Apply CV — Anson 求職自動化 Pipeline

## 你的任務

幫 Anson 完成整個求職 CV 優化流程，從 JD 連結到交出 PDF，再到 Notion 追蹤記錄。
這個 Skill 建基於 Austin Belcak（Cultivated Culture）的 CV 框架：每個 bullet point 必須通過「So what? Prove it.」測試。

## 硬編碼配置（Anson 專用）

```
CVdraft 資料夾:  /sessions/relaxed-vigilant-johnson/mnt/linkedin/CVdraft/
Notion DB ID:   aa55f724-626b-41dc-be36-216a1c6988d7
Notion DS ID:   ed9b1676-3412-45fc-8c26-75442b7c7352
Notion 父頁面:  33bda87c-6346-8196-a6a5-df705e5a59c4
CV 命名格式:    Anson_Chan_CV_[職位名稱]_[YYYY-MM-DD].pdf
顏色方案:       Teal #1A6B72（與現有CV一致）
```

---

## STEP 0 — 讀取 JD

**從用戶訊息提取 URL。**

平台偵測：
```python
def detect_platform(url):
    if "linkedin.com" in url: return "🔗 LinkedIn"
    elif "jobsdb.com" in url: return "📋 JobsDB"
    else: return "🌐 Other"
```

抓取策略（按優先順序）：
1. 如果 Chrome MCP 已連接：用 `navigate` + `get_page_text` 取全文
2. 否則用 `WebFetch`，prompt：「Extract the complete job description including job title, company name, location, responsibilities, requirements, qualifications, and any other role details.」
3. 如果兩者都失敗：請用戶直接貼上 JD 文字

同時用 WebSearch/WebFetch 搜索公司背景資料。

---

## STEP 1 — JD 深度分析

### 1.1 Must-Have vs Nice-to-Have 表格

| 類別 | 要求 | 重要程度 |
以表格格式列出：5-8 個 Must-Have（⭐⭐⭐⭐⭐），3-5 個 Nice-to-Have。

### 1.2 ATS 關鍵字清單
列出所有高頻關鍵字（工具名稱、技能、行業術語），這些字詞**必須**自然出現在最終 CV 裡。

### 1.3 隱藏訊號
讀懂 JD 字裡行間：文化暗示、隱性優先次序、團隊規模線索、匯報層級、潛在紅旗。

### 1.4 公司背景研究
- 公司類型、行業、規模
- Marketing 團隊架構（如能找到）
- 此職位匯報對象（推斷或確認）

**⚠️ 深度公司審視觸發（v2.0）：** 如果用戶要求「公司審視／deep dive」、分析涉及 unit economics（LTV/CAC/payback/利潤率推導）、或用戶講「唔好吹水／要市場數據」—— 唔好喺主對話 solo 做。必須 Read `~/.claude/skills/cv-optimizer/knowledge/fact-discipline.md` 並照行「總指揮 + 4 現實真人 subagent」模式：每個數字要 URL、搵唔到標 UNVERIFIED、證據四級分級（【公開】【基準】【推導】【評分】）、推導模型只做面試問題唔做事實陳述。薪酬數據以 Michael Page / Morgan McKinley 機構級調查為準，aggregator 只做旁證。

完成後暫停：「✋ Step 1 完成。確認後繼續 Step 2。」

---

## STEP 2 — 載入 CV 並診斷

**載入 CVdraft 最新的 PDF 作為基礎 CV：**

```python
import os, glob
from pypdf import PdfReader

cvdraft = "/sessions/relaxed-vigilant-johnson/mnt/linkedin/CVdraft/"
pdfs = sorted(glob.glob(cvdraft + "*.pdf"), key=os.path.getmtime, reverse=True)
if pdfs:
    reader = PdfReader(pdfs[0])
    base_cv_text = "\n".join(page.extract_text() for page in reader.pages)
    base_cv_filename = os.path.basename(pdfs[0])
```

如果 CVdraft 沒有 PDF，請用戶上傳基礎 CV。

### 三欄診斷表

| ✅ 優勢（保留） | ⚠️ 需要加強 | ❌ 缺失 / 必須處理 |

### Fit Score

| 維度 | 評分 /10 |
| 技能吻合度 | |
| 經驗相關性 | |
| ATS 關鍵字覆蓋 | |
| 表達質量 | |
| **整體** | |

**重要紅旗逐一列出**（例如：舊公司的 90-day plan、期望薪酬、不相關內容）。

完成後暫停確認。

---

## STEP 3 — 優化策略

整合 Step 1 + Step 2，呈現：

**優先級排序：**
- 🚨 高優先（ATS 篩選關口 — 必做）
- 🔶 中優先（影響 interview invitation rate）
- 🟡 低優先（收尾 polish）

**CAR Method 重寫示範（Before → After）：**
為每個需要改進的 bullet 提供量化重寫方向。

**ATS 關鍵字整合計劃：**
哪個關鍵字放進哪個 CV 段落，確保自然不生硬。

**結構建議：**
職稱、段落順序、刪除什麼、加入什麼。

完成後暫停確認。

---

## STEP 4 — 撰寫完整優化 CV

按確認的策略撰寫全新 CV，嚴守以下原則：

- **職稱**必須與目標職位完全一致
- **每個 achievement bullet** 必須通過 Austin Belcak 的「So what? Prove it.」測試
- **所有 ATS 關鍵字**自然融入（不能堆砌）
- **刪除**：期望薪酬、HKPR 身份、針對其他公司的 90-day plan
- 最多 **2頁**
- 用戶的真實經驗 — 不捏造任何內容

呈現完整 CV 文字供確認。暫停等待用戶 OK。

---

## STEP 5 — 生成 PDF 並儲存

用 `scripts/generate_cv.py` 腳本生成 PDF。如果腳本不存在，用 reportlab inline 生成。

**設計規格（與現有 CV 一致）：**
```python
TEAL        = colors.HexColor("#1A6B72")
TEAL_LIGHT  = colors.HexColor("#E8F4F5")
DARK        = colors.HexColor("#1C1C1C")
RULE        = colors.HexColor("#C5DDE0")
# 字體：Helvetica, A4 紙張, 頁邊距 18mm
# Bullet 符號：▸ (teal)
# 工作標題：左欄職位+公司，右欄日期+地點（兩欄佈局）
```

**檔案命名：**
```python
import re
from datetime import date

def make_filename(job_title):
    clean = re.sub(r'[^a-zA-Z0-9\s]', '', job_title)
    slug = '_'.join(clean.split())
    return f"Anson_Chan_CV_{slug}_{date.today().strftime('%Y-%m-%d')}.pdf"

output_path = f"/sessions/relaxed-vigilant-johnson/mnt/linkedin/CVdraft/{make_filename(job_title)}"
```

生成後確認頁數和文字內容正確。

---

## STEP 6 — 建立 Notion 申請記錄

用 `notion-create-pages` 在 Job Application Tracker 建立新記錄。

**Properties：**
```json
{
  "Job Title": "[職位名稱]",
  "Company": "[公司名稱]",
  "Platform": "[🔗 LinkedIn / 📋 JobsDB / 🌐 Other]",
  "Job Link": "[URL]",
  "Status": "🔍 Researching",
  "Priority": "⚡ Medium",
  "date:Applied Date:start": "[今日 YYYY-MM-DD]",
  "Match Score": [Fit Score 數字],
  "Remote Type": "[從JD判斷]",
  "Reports To": "[從研究或JD推斷]",
  "CV Version": "[PDF檔案名稱]",
  "Notes": "[一句話總結：強項 + 主要 gap]"
}
```

**頁面內容（點進 record 後看到的）：**

```markdown
## 📋 Job Description
> [職位基本資料 callout]
[JD 要點整理]

## ✅ Requirements Analysis
| 要求 | 我的狀態 | 證據 |
|---|---|---|

## 🏢 Company Background
[公司研究結果]

## 📊 Marketing Department Structure
[匯報架構圖 or 推斷]

## 📄 CV & Application
- CV 檔案：`[filename]`
- CV 位置：`ansonchanmac/Cowork OS/linkedin/CVdraft/`
- 優化日期：[日期]

## 📅 Application Timeline
| 日期 | 動作 | 備註 |
|---|---|---|
| [今日] | CV 優化完成 | |
| — | 📤 提交申請 | |
| — | 📞 跟進 | 申請後 7 日 |

## 💬 Interview Prep Notes
**可能面試問題：**（根據 JD 生成 5 條）

**主要 Gap 回應策略：**（如何回應最弱的要求）
```

---

## STEP 7 — 更新 Notion 父頁面 CV 庫

用 `notion-update-page` 的 `update_content` 指令，在 LinkedIn 求職父頁面的 CV 檔案庫表格加入新一行：

```
| `[新CV檔案名稱]` | [職位] @ [公司] | [日期] |
```

找到現有表格的最後一行，在後面加入新行（`update_content` with `old_str` = 最後一行現有 entry）。

---

## STEP 8 — 完成總結

呈現給用戶：

```
✅ CV 生成完成！
[查看 CV](computer:///sessions/.../CVdraft/[filename].pdf)

✅ Notion 記錄已建立
[查看申請記錄]([notion_url])

📋 提交前 Checklist：
□ 打開 PDF 確認格式（特別係手機版）
□ 確認職稱和公司名稱正確
□ 準備 Cover Letter（需要的話叫 Claude 寫）
□ 申請後更新 Notion 狀態為「📤 Applied」

💡 面試準備提示：
[3 條針對此職位的面試 tips]
```

---

## 錯誤處理

| 情況 | 處理方式 |
|---|---|
| JD 抓取失敗 | 請用戶直接貼上 JD 文字 |
| CVdraft 沒有 PDF | 請用戶上傳基礎 CV |
| Notion 寫入失敗 | 將記錄資料儲存至本機 JSON，通知用戶 |
| PDF 生成失敗 | 以 Markdown 輸出 CV，通知用戶 |
| 公司資料找不到 | 在 Notion 記錄中標記「⚠️ 待研究」 |

---

## 重要原則

**只用真實資料。** 不捏造 Anson 沒有的技能或經歷。如果不確定某個量化數字，用保守但可信的框架表達（如「HK$3M+ cumulative ad spend」而非「數以百萬計」）。

**職稱要精確對應。** CV 頂部的職稱必須和目標職位完全一致，這是 ATS 的第一關。

**每一步都等用戶確認。** Steps 1-4 各自暫停一次，確保用戶對方向認同才繼續。Steps 5-8 可以連續執行。
