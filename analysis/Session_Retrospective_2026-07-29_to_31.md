# Session 回顧：2026-07-29 至 2026-07-31（四日求職 sprint）

**用途：** 呢部機（雲端 remote container）嘅工作要收尾，用戶轉去 MacBook Pro 繼續。本文件記錄做過乜、學到乜教訓、流程點樣改進，俾下一個 session（人或 AI）接手時唔使由零開始。

**Repo：** `Ansonhouston/daily-ai-news-radar`，branch `claude/cv-four-versions-owx7c2`
**Model 沿革：** 呢個 session 中途換過三次 model（Fable 5 → Opus 5 → Sonnet 5），內容連貫性由 git commit 同文件本身保持，唔靠對話記憶。

---

## 一、做咗乜（時序總覽）

### Day 1（07-29）— Activate Talent，四版 Creative Strategist CV

- 用戶 DM 截圖顯示 Activate Talent recruiter Danny (Daniel) Mejia 主動接觸，職位係 Creative Strategist（Remote, HK），客戶匿名
- 用 `cv-optimizer` skill 起步，跑咗公司背景分析、JD 拆解
- 產出四版 CV（A JD-mirror / B AI-Native / C Performance / D Storyteller），各 4 頁 PDF，用自建 `generate_cv_pdf.py`（reportlab + 嵌入 WenQuanYi Zen Hei 字型畀繁體中文渲染）
- 用戶要求兩次調整（email 改 outlook、加/減 expected salary），每次都改 md 源文件 → 重生 PDF → commit → push → SendUserFile
- 做咗一個 30 分鐘 screening call 嘅一頁 cheat sheet（雙欄 A4，`generate_screening_cheatsheet.py`）
- 幫手 draft 咗俾 Danny 嘅 LinkedIn reply（問公司背景、marketing 架構、時區、僱傭形式、budget，唔報自己價）

### Day 2（07-30）— OneDegree，四版 Senior Growth Manager CV + Cover Letter

- 用戶貼 JobsDB 截圖（OneDegree Hong Kong，Senior Growth Manager）
- 因為 `hk.jobsdb.com` 被 session 嘅 egress policy 封鎖（403），改用用戶截圖做輸入
- 做咗深度公司審視：財務（HK$330M 收入、首次全年盈利）、Glassdoor 文化評分、薪酬 benchmark
- 用戶要求「用 budget forecasting 專家真人角度分析呢個 role 要做乜、有咩前瞻策略」→ 首次動用 **CBCV (Customer-Based Corporate Valuation)** 方法論（Dan McCarthy / Peter Fader）去推導 unit economics —— 但呢個模型後來被證實有嚴重瑕疵（見第三節教訓）
- 產出四版 Senior Growth Manager CV（A/B/C/D，同 Creative Strategist 一樣嘅四角度框架）+ 一份 pain-letter 風格 cover letter（Liz Ryan 方法論）
- 建咗獨立嘅 `generate_cover_letter_pdf.py`（信件版面，唔同於 CV 版面）
- Expected salary 反覆改咗兩次（HK$55,000 → 48,000 → 55,000），每次都完整重生 PDF 鏈

### Day 3（07-30 尾聲）— 深度單位經濟分析（v1，有缺陷）

- 寫咗一份 658 行嘅整合分析文件 `Anson_job_search_analysis_2026-07-30.md`，涵蓋四個職位（Activate Talent / OneDegree / Checkout.com / Deloitte）
- 呢份文件本身已經有「證據分級」意識（【公開】【基準】【推導】【評分】），但執行唔夠嚴謹 —— 見第三節
- 用戶主動提出質疑：「呢間寵物保險公司利潤真係咁低？」→ 觸發修正 0.3% 淨利率嘅誤導性論述

### Day 4（07-31）— 外部審視 + 四 Subagent 事實重建 + Skill 沉澱

- 用戶用 **Codex（另一個 AI）獨立審視** v1 分析文件，Codex 捉到三個實質性錯誤（見第三節）
- 用戶明確要求：「設立一個總指揮，然後分 4 個現實真人 subagent 去改造，一定要根據事實」
- 執行：總指揮（本 session）派 4 個並行 subagent，各自用唔同真人方法論做獨立 web research：
  1. Unit Economics 重建（Dan McCarthy / Peter Fader CBCV + 精算 survival analysis）
  2. 行業營運模式驗證（Darryl Rawlings / Trupanion 公開財報）
  3. 薪酬 + 市場數據核實（機構級來源優先）
  4. 策略合成（Alison Green hiring-manager 視角）
- 合成做 `Anson_job_search_analysis_v2_2026-07-31.md`，開頭係 10 條「v1→v2 錯誤更正表」
- 用戶要求將呢套「總指揮 + 4 subagent 事實紀律」模式**沉澱落 skill**，令以後自動用 —— 執行咗 `ssc`（skill creator）流程，寫入 `cv-optimizer/knowledge/fact-discipline.md` + 兩個 SKILL.md 嘅觸發路由

---

## 二、完整交付物清單

Repo `Ansonhouston/daily-ai-news-radar`，branch `claude/cv-four-versions-owx7c2`：

```
cv/
├── Anson_Chan_CV_Creative_Strategist_{A_JD_Mirror,B_AI_Native,C_Performance,D_Storyteller}_2026-07-29.{md,pdf}
├── Anson_Chan_CV_Senior_Growth_Manager_{A_JD_Mirror,B_AI_Automation,C_Performance_Budget,D_Lifecycle_Funnel}_2026-07-30.{md,pdf}
├── Anson_Chan_CoverLetter_OneDegree_Senior_Growth_Manager_2026-07-30.{md,pdf}
├── Anson_Chan_Screening_CheatSheet_ActivateTalent_2026-07-29.pdf
├── generate_cv_pdf.py          — CV 產生器（支援 markdown → 4頁A4，帶 CJK 字型）
├── generate_cover_letter_pdf.py — 信件版面產生器
└── generate_screening_cheatsheet.py — 雙欄 cheat sheet 產生器

analysis/
├── Anson_job_search_analysis_2026-07-30.md      — v1（有缺陷，保留做對照）
├── Anson_job_search_analysis_v2_2026-07-31.md   — v2（事實重建版，以此為準）
└── Session_Retrospective_2026-07-29_to_31.md    — 本文件
```

技能升級（已 commit 入 repo 嘅 `skills/` 資料夾，**需要手動同步返本機 `~/.claude/skills/`**）：
```
skills/cv-optimizer/SKILL.md              — 加咗「多智能體事實紀律模式」觸發節
skills/cv-optimizer/knowledge/fact-discipline.md  — 新模組主體
skills/job-apply-cv/SKILL.md              — Step 1.4 加咗深度審視路由
```

---

## 三、教訓（最重要嘅部分）

### 教訓 1：口述數字要求截圖驗證，唔可以照單全收

用戶第一次講 FB Reel「60,000 views」，之後補截圖先發現係 **76,000**，仲有第二條 11,000 嘅片。差 27% 唔算少。**規則：涉及會寫入 CV／cover letter 嘅具體數字，如果得口述冇截圖，要主動問「有冇 screenshot 可以核對」。**

### 教訓 2：唔好將「JD 匹配度」同「成功機率」混為一談

我一度建議用戶「集中打 Activate Talent，Checkout.com 做 backup」，理由係 Activate Talent JD 匹配 9/10。用戶指出呢個判斷錯 —— Activate Talent 客戶匿名、僅係 agency 初篩、多個未知數（時區/僱傭形式/薪酬）疊加，唔應該因為「文本匹配分高」就當成主線押注。**規則：排序建議要分開兩條軸 —— 「呢份工幾啱我」同「呢份工幾大機會成」，唔可以用同一個分數代表兩件事。**（呢條後尾正式落咗 skill：v2 文件第 5 節嘅「行動排序 vs 職業質量排序」雙軌設計。）

### 教訓 3：精確嘅無來源數字係最危險嘅一種（最大教訓）

v1 分析用咗「獸醫通脹 6.57%/年」呢個數字去支撐「寵物保險係結構性難題」嘅論述 —— 聽落好權威，但**完全查無出處**。真實數字（BLS）係長期均值 4.98%、近年 5.3–5.6%；香港更高達 10–20%（OneDegree 自己公佈 18%）。

仲有更嚴重嘅：v1 用「HK$330M 收入 ÷ 240,000 保單 = 平均保費 $1,375」，但事後查證原文係「**累計簽發**逾 20 萬張」—— 分子分母根本唔同時間口徑，成條算式由第一步已經錯。跟住用「90% 續保率 → 幾何模型 → 10 年客戶壽命」，但公司自己披露「2020 年客戶 cohort 到 2024 年底剩 52%」，同幾何模型推算嘅 62% 明顯唔夾。

**規則：**
- 任何「%/年」「$X per unit」呢類精確數字，出街前必須有 URL。搵唔到就寫「約 5%（BLS 估算）」，唔好寫一個假裝精確嘅數。
- 分母口徑（累計 vs 在保、cumulative vs active、GWP vs net revenue）要喺計算前先確認，唔可以假設分子分母自動對齊。
- 幾何/簡化模型如果同公司自己嘅披露數字矛盾，模型錯，唔係披露錯。

### 教訓 4：結構性斷言（「X 必然導致 Y」）出街前要搵反例試炸

v1 寫「加保費會摧毀續保率，所以寵物保險係近乎無解嘅難題」。Subagent 查到 Trupanion 喺加州獲批加價 29%，之後**留存率反而連升四季**。呢個直接推翻咗斷言嘅必然性 —— 真相係「點加價」（cohort 定價、透明歸因、高頻小步）先係關鍵，唔係「加唔加」。

**規則：寫任何形式嘅「A 必然導致 B」之前，主動搵「有冇人做過 A 但冇發生 B」嘅反例。搵到就要修正結論，唔可以因為反例難搵就假設佢唔存在。**

### 教訓 5：薪酬數據要分級，aggregator 之間可以自相矛盾到失控

同一個職位，PayScale 話年薪 HK$563K，Indeed 話月薪 HK$50K（年化都係 600K 但講法唔一致），Glassdoor 甚至出現「HK$55,250/**年**」呢類明顯手民之誤嘅數字。呢啲嘢混埋一齊用會令建議睇落有依據，實質係雜訊疊加。

**規則：機構級薪酬調查（Michael Page、Morgan McKinley、Robert Walters、政府統計處）優先；aggregator（PayScale/Glassdoor/Indeed/ERI）只做旁證，唔可以係唯一支撐。呢條已寫入 skill。**

### 教訓 6：市場規模數字要用龍頭玩家收入做 sanity check

v1 引用「香港寵物保險市場規模 USD 8.5M」，但 subagent 一計：OneDegree 一間公司嘅收入已經 ≈USD 42M，仲未計其他競爭者。呢個市場規模數字明顯係聚合商模板文字，冇任何方法學交代。**規則：市場規模類數字，如果有已知單一玩家嘅收入，用嚟做上限檢查——市場唔可能細過龍頭。**

### 教訓 7：政府/官方文件引用嘅數字，要查番原始調查年份

施政報告 2025 年講「24 萬戶養 40 萬隻貓狗」，subagent 查到呢組數字**同 2018 年統計處住戶調查幾乎一模一樣**——即係 2025 年份文件引緊七年前嘅舊調查，唔係新統計。**規則：政府文件入面嘅統計數字，如果冇註明調查年份，預設佢有可能係舊數，要另外搵原始調查嚟源核實。**

### 教訓 8：交俾第二個 AI 做審視嘅文件，要主動帶「證據分級 + 指定攻擊點」

第一次交俾 ChatGPT／Codex 審視時，我哋喺文件度已經加咗證據分級，但仲加咗一組「指定要挑戰嘅問題清單」（例如「攻擊第 4.1 節嘅五項假設，邊項最可能錯」）。事後證明呢個做法有效 —— Codex 真係逐點拆解咗個 unit economics 模型，冇淪為覆述總結。**規則：叫第二個 AI 做獨立審視，唔好淨係話「幫我睇睇」，要話「呢幾點我唔肯定，你specifically 挑戰呢啲」。開放式請求通常換返一份客套總結。**

### 教訓 9：唔好將自己嘅推導模型喺真實情境（面試）當事實講

即使 v2 已經修正咗大部分數字問題，我哋都刻意喺文件加咗一句規則：**呢啲單位經濟模型嘅正確用法係「面試偵察雷達」——即係轉化成問題去問對方，唔係當成已證實嘅結論講出嚟。** 用戶如果喺 OneDegree 面試度講「我推算你哋嘅 CAC 大概係 $900」，聽落好似專家，但其實係攞一個未經驗證嘅模型冒充事實，一旦對方追問假設就會穿煲。反而問「你哋點計 CAC payback period」先顯得資深。

### 教訓 10：Egress policy 封鎖要即時識別，唔好重試繞路

`hk.jobsdb.com` 被 session 政策擋咗（403 policy denial），我確認咗係政策封鎖之後就冇再嘗試繞過（例如換 UA、換代理），直接請用戶用截圖代替。**規則：403/407 屬組織政策拒絕，唔係網站技術故障，一律唔重試唔繞路，改用替代輸入方式。**

---

## 四、流程改進（已經落實）

1. **PDF 產生器分工細化** —— CV 用一個 generator（`generate_cv_pdf.py`），Cover Letter 因為版面完全唔同（信件抬頭 vs CV 分節）獨立開咗 `generate_cover_letter_pdf.py`，Cheat sheet 因為要雙欄又開咗第三個。教訓：唔好一個 generator 塞哂晒所有版面邏輯，分開先易維護。

2. **繁體中文渲染** —— reportlab 預設 Helvetica 冇 CJK 字集，中文變黑方塊。解法：搜到系統已裝 `wqy-zenhei.ttc`（文泉驛正黑），用 regex 偵測 CJK 字符範圍、動態包 `<font name="CJK">` tag。**呢個 fix 已經寫死入三個 generator，下次唔使再搜。**

3. **PDF 驗證自動化** —— 每次改完內容，唔淨係「睇落無錯」就算，用 `pypdf.PdfReader` 直接抽取文字驗證關鍵字段有冇改到位（例如 email、salary 數字），先算完成。中途裝 `cryptography` package 撞版本 bug（rust binding panic），改用 `pip install --force-reinstall` 解決。

4. **多智能體事實紀律 skill 化** —— 呢個係最大嘅流程資產。以後任何公司深度審視／unit economics 分析，唔使再由頭諗一次「點樣先叫做有紀律咁做研究」——已經寫成可重用嘅 `knowledge/fact-discipline.md`，觸發條件、四級證據分級、Locked Lessons 全部固化，兩個 job skill 都會自動路由過去。

5. **v1→v2 更正表做標準做法** —— 任何重建分析文件，開頭必須列返「邊啲數字變咗、點解變」，唔淨係靜靜噉換走舊結論。呢個透明度規則已寫入 skill 嘅合成規則。

---

## 五、未完成 / 待接手事項

| 項目 | 狀態 | 下一步 |
|---|---|---|
| Activate Talent screening call | 已準備 cheat sheet + reply draft | 需要用戶確認實際 call 咗未、有咩結果 |
| OneDegree 申請 | CV + cover letter 已就緒（HK$55,000） | 需要用戶確認實際遞交咗未 |
| Checkout.com | Gate question 已寫好（俾 recruiter Renee Yu） | 未發送，待用戶決定 |
| Deloitte | 建議放棄（唔啱 profile） | 唔使跟進 |
| Skill 同步 | 已 commit 入 repo `skills/` 資料夾 | **用戶需要手動 `cp -r skills/cv-optimizer skills/job-apply-cv` 去本機 `~/.claude/skills/`** |
| OneDegree 保監局官方數據 | 因 session 網絡政策封鎖 `ia.org.hk`，未能核實 | 本機無呢個限制，可以直接查 |
| v1 分析文件 | 保留做對照，未刪除 | 可以擺喺度，v2 已經係權威版本 |

---

## 六、轉去 MacBook Pro 點樣開始

呢個 session 跑喺雲端 remote container，同你 MacBook 嘅 Claude Code CLI 唔係同一個執行環境，但**所有實質工作成果已經 push 上 GitHub**，唔喺對話記憶度，喺 repo 度。

MacBook 開啟 Claude Code 之後，貼呢句：

```
呢個 repo 有個未合併嘅 branch claude/cv-four-versions-owx7c2，
喺 Ansonhouston/daily-ai-news-radar。入面有我四日嘅求職資料：
四版 Creative Strategist CV、四版 Senior Growth Manager CV、
OneDegree cover letter、Activate Talent cheat sheet，
同埋 analysis/ 資料夾入面嘅 v2 事實重建分析文件同呢份 retrospective。
先 checkout 呢個 branch，讀 analysis/Session_Retrospective_2026-07-29_to_31.md
同 analysis/Anson_job_search_analysis_v2_2026-07-31.md，
了解返成件事嘅來龍去脈先。另外我要將 skills/cv-optimizer 同
skills/job-apply-cv 呢兩個升級版 sync 落我本機 ~/.claude/skills/，幫我做埋。
```

如果想快啲直接指令：

```bash
git clone https://github.com/Ansonhouston/daily-ai-news-radar.git
cd daily-ai-news-radar
git checkout claude/cv-four-versions-owx7c2
cp -r skills/cv-optimizer skills/job-apply-cv ~/.claude/skills/
```

---

**文件完。** 呢份記錄本身都應該 commit 入 repo，成為呢個 branch 嘅一部分。
