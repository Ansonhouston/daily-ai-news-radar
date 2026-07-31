# Anson Chan — 求職分析 v2（事實重建版）

**日期：** 2026-07-31
**製作方式：** 總指揮（Claude）+ 4 個真人方法論 subagent 並行重建，全部數字附 URL 或標 UNVERIFIED
**取代：** `Anson_job_search_analysis_2026-07-30.md`（v1）— v1 嘅推導模型有多處實質錯誤，本版逐條更正
**已吸收：** Codex 獨立審視（2026-07-31）全部修正意見

**四個 subagent 分工：**
① Unit Economics 重建（Dan McCarthy / Peter Fader CBCV + 精算生存分析）
② 寵物保險營運模式（Darryl Rawlings / Trupanion 公開披露）
③ 薪酬 + 市場數據核實（機構級來源優先：Michael Page / Morgan McKinley / 政府統計處）
④ 策略重建（Alison Green hiring-manager 視角 + Codex 修正全採納）

---

# 第 0 節：v1 → v2 錯誤更正表（先讀呢度）

| # | v1 講法 | v2 事實 | 證據 |
|---|---|---|---|
| 1 | 240,000 保單當 in-force，平均保費 = 330M÷240k = **HK$1,375** | **240k 係累計簽發數**。OneDegree 中文稿原文：「**累計簽發**逾20萬張寵物保險保單」；The Standard 原文 "Total policies reached 240,000"（無 in-force 字眼）。在保保單推算約 10–15 萬（ASSUMPTION），中央情境平均保費 ≈ **HK$2,750** | [OneDegree 首錄盈利稿](https://www.onedegree.hk/zh-hk/news/breakeven)、[The Standard](https://www.thestandard.com.hk/tech-and-startup/article/322012/OneDegree-posts-first-full-year-profit-with-revenue-up-nearly-40pc-to-HK330-million) |
| 2 | 90% 續保 → 幾何模型 → **10 年客戶壽命** | 被公司自己嘅披露推翻：**2020 寵物 cohort 至 2024 年底留存 >52%**（平坦 90% 應得 ~62%）。校準曲線（首續 80% 漸升至 93%）+ 10% 折現後 ≈ **4.6–4.8 個折現保單年** — v1 高估壽命價值超過一半 | [OneDegree 五週年稿](https://www.onedegree.hk/en-us/news/ODHK-5anniversary-en)、[Insurance Business Asia](https://www.insurancebusinessmag.com/asia/news/catastrophe/onedegree-marks-five-years-with-profit-and-expansion-push-533135.aspx) |
| 3 | 獸醫通脹「**6.57%/年**」 | **UNVERIFIED — 搵唔到任何來源**。BLS 實數：美國獸醫服務長期（1997–2026）年均 **+4.98%**，2025 年約 +5.3–5.6%。**香港更高：OneDegree 自己公佈 +18%**，精算顧問估 10–20%/年 | [BLS via in2013dollars](https://www.in2013dollars.com/Veterinarian-services/price-inflation)、[OneDegree 通脹調查](https://www.onedegree.hk/en-us/news/HongKong-pet-medical-inflation-increases)、[EB Actuary](https://www.ebactuary.com/post/hong-kong-pet-insurance-market-analysis) |
| 4 | 「加價會摧毀續保率」→ 寵物保險「near unsolvable」 | **被實證推翻**：Trupanion 加州獲批加價 2023 年 12%、2024 年 **29%**，之後 2025 年月留存率**連升四季**至 98.34%。正確結論：係 pricing discipline 複合題，唔係結構死局 | [StockTitan rate filing](https://www.stocktitan.net/news/TRUP/trupanion-comments-on-rate-filing-approval-in-ymjlewdg1jl9.html)、[Motley Fool Q4 2025 transcript](https://www.fool.com/earnings/call-transcripts/2026/02/12/trupanion-trup-q4-2025-earnings-call-transcript/) |
| 5 | 「淨利 HK$1M → 冇本錢做 3 年 payback」推得太盡 | 淨利 ≠ 現金緩衝 ≠ marketing 預算。保險增長仲受監管資本、再保容量、承保紀律約束。**框架保留，但降級做面試提問，唔係結論** | Codex 修正 + agent ① |
| 6 | 香港寵物險市場「USD 8.5M」 | **棄用** — 聚合商模板數。OneDegree 一間公司 FY2025 收入已 ≈ USD 42M（寵物佔收入 78%）。冇官方口徑：保監局唔拆寵物險分項 | agent ③ 溯源 |
| 7 | 「8–10% 滲透率」當行業事實 | 實為 **OneDegree 高管受訪自述**，唔係保監局或統計機構數據；分母（40 萬定 60 萬隻）冇交代。引用須註明「公司高管聲稱」 | [The Star / SCMP 系](https://www.thestar.com.my/aseanplus/aseanplus-news/2025/07/05/fur-loves-sake-in-hong-kong) |
| 8 | 施政報告「24 萬戶 / 40 萬隻」當 2025 年新數 | 措辭同 2018 年統計處主題性住戶統計調查第 66 號（241,900 戶 / 405,200 隻）幾乎完全吻合 — **施政報告引用緊七年前嘅調查** | [統計處 2019 公報](https://www.info.gov.hk/gia/general/201906/21/P2019062100361.htm)、[施政報告 §245](https://www.policyaddress.gov.hk/2025/en/p245.html) |
| 9 | 薪酬全靠 aggregator（PayScale / Glassdoor / Indeed / ERI） | 改用機構級：**Michael Page** DMM 平均 HK$550K/年、Senior MM **HK$800K/年**；**Morgan McKinley 2026** DMM / MM 平均 **HK$55K/月**、Director HK$80K/月。（ERI 個數啱啱好貼近機構中位 — 但屬模型外推，唔引用到個位數） | [MP Senior MM](https://www.michaelpage.com.hk/salary-comparison-tool/senior-marketing-manager-salaries)、[MM HK](https://www.morganmckinley.com/hk/salary-guide/data/marketing-manager/hong-kong-sar) |
| 10 | 排序將「行動優先」同「職業質量」混埋一齊 | 拆開兩條軸（見第 5 節） | Codex 修正 + agent ④ |

---

# 第 1 節：OneDegree 已核實事實（v2 修訂）

## 1.1 財務與業務（全部附來源）

| 項目 | 數據 | 來源 |
|---|---|---|
| FY2025 收入 | **HK$3.3 億**（+38% YoY）⚠️ 口徑未定義（GWP？已賺？含寵物百貨非保險收入？） | [The Standard](https://www.thestandard.com.hk/tech-and-startup/article/322012/OneDegree-posts-first-full-year-profit-with-revenue-up-nearly-40pc-to-HK330-million) |
| FY2025 淨利 | 七位數（>HK$1M）；2024 年蝕約 HK$4,000 萬；香港首間轉盈利虛擬保險公司 | 同上 + [hk01](https://www.hk01.com/財經快訊/60314167/onedegree去年錄全年盈利-為全港首家扭虧虛擬金融機構) |
| 保單 | 「Total policies reached 240,000」＝**累計簽發口徑**（中文稿：寵物保單「累計簽發逾20萬張」） | [breakeven 稿](https://www.onedegree.hk/zh-hk/news/breakeven) |
| 續保率 | 整體平均 90%；寵物 91% | 同上 |
| **寵物險佔比** | 中文稿：「佔**總收入** 78%」（英文轉載出現過「78–85% of total **policies**」— 基數分歧，未能對頁核實） | [breakeven 稿](https://www.onedegree.hk/zh-hk/news/breakeven) vs [Fintech News HK](https://fintechnews.hk/37058/insurtech/onedegree-achieves-profitability-2025/) |
| 2020 寵物 cohort 留存 | **>52% 至 2024-12-31 仍為保單持有人**（約 4.5 年） | [五週年稿](https://www.onedegree.hk/en-us/news/ODHK-5anniversary-en) |
| 寵物險賠付率 | 只披露「較 2020 年**改善約 30%**」（相對值，絕對水平未披露） | 同上 |
| 2023 GWP | 超過 HK$1.8 億（+59%），連續兩年四虛保之首 | [四週年稿](https://www.onedegree.hk/en-us/news/odhk-anniversary2024) |
| 其他產品線 | 數碼資產保險：3 年收入 +7 倍，**香港市佔 70%**；火險 +6 倍（vs 2021）；家居 +5 倍（vs 2022） | [breakeven 稿](https://www.onedegree.hk/zh-hk/news/breakeven) |
| 員工 | 5 年收入增 38 倍，員工維持約 **100 人** | 同上 |
| 保監局官方數據 | IA 有刊個別公司統計，**本 session 網絡被封未能取得** — 最優先補做嘅核證 | [IA 統計頁](https://www.ia.org.hk/en/infocenter/statistics/annual_general_business_statistics.html) |

## 1.2 產品槓桿（同 growth 職位直接相關）

| 槓桿 | 內容 | 來源 |
|---|---|---|
| 網絡導流 | 網絡獸醫報銷 **90%** vs 非網絡 **70%**（20 個百分點差 = 強力 steering）；幼寵（13週–11個月）最高 50% | [OneDegree Pet Insurance](https://www.onedegree.hk/en-us/pet-insurance)、[FAQ](https://www.onedegree.hk/en-us/faq/article/can-i-bring-my-pet-to-any-vet-in-hong-kong-under-your-plan) |
| 自有獸醫網絡 | 官方網絡名單（Pet CEO Plan） | [網絡 PDF](https://odhk.blob.core.windows.net/pet/OneDegreeVetClinicNetwork-en.pdf) |
| 產品分層 | Pet CEO Plan 四檔，年度上限至 HK$100,000 | [官方稿](https://www.onedegree.hk/en-us/news/onedegree-pawfect-care-The-one-and-only-Pet-CEO-Plan-in-Hong-Kong) |
| 續保定價權 | FAQ：續保保費按**寵物年齡**計算、公司保留最終決定權；終身續保無年齡上限 | [FAQ](https://www.onedegree.hk/en-us/faq/article/will-my-premium-increase-when-i-renew-my-pets-policy) |
| 通脹數據 | 自己出調查：香港寵物醫療通脹 +18%、每次睇獸醫 >HK$2,000 —— 識量度先識定價，正面訊號 | [官方稿](https://www.onedegree.hk/en-us/news/HongKong-pet-medical-inflation-increases) |

---

# 第 2 節：重建 Unit Economics（agent ①）

## 2.1 留存曲線（同時滿足兩個官方披露；ASSUMPTION）

平坦 90% 幾何模型畀 0.9^4.5 ≈ 62%，但官方 cohort 數係 >52% → 早年續保必然低過 90%：

| 續保年度 | 年續保率（假設） | 累計留存 |
|---|---|---|
| 第 1 次續保 | 80% | 80.0% |
| 第 2 次 | 86% | 68.8% |
| 第 3 次 | 90% | 61.9% |
| 第 4 次 | 92% | 57.0% |
| 第 5 次起 | 93%/年 | 53.0%（第5年）… |

4.5 年位置 ≈ 54–55%（符合「>52%」）；加權帳面續保率 ≈ 90% ✓
**10% 折現後預期保單壽命 ≈ 4.6–4.8 個折現保單年**（v1：10 年不折現）

## 2.2 平均保費 sensitivity（分母改為在保假設）

| 在保保單假設 | 平均保費/年 | 評註 |
|---|---|---|
| 240,000（v1 做法） | HK$1,375 | 幾乎肯定錯 — 當累計數係在保數 |
| 180,000 | HK$1,833 | 仍偏樂觀 |
| **120,000（中央）** | **HK$2,750** | 同香港寵物險市價區間最吻合 |
| 80,000 | HK$4,125 | 偏高端 book |

## 2.3 貢獻 LTV（折現）同可容許 CAC

中央情境（在保 120k、年保費 $2,750、貢獻邊際 25%、折現壽命 4.6 年）：
- 貢獻 LTV ≈ **HK$3,160**
- **可容許 CAC = min(LTV÷3, 回本期上限) ≈ HK$690–1,050**（12 個月回本 ≈ $690；24 個月 ≈ $1,190）

**澄清（Codex 修正採納）**：淨利 HK$1M ≠ 現金緩衝 ≠ marketing 預算；就算 LTV>CAC 都受監管資本（新業務 strain）、再保容量、承保紀律約束。**呢個模型嘅正確用途係面試偵察雷達，唔係當事實陳述。**

---

# 第 3 節：寵物保險 — 「可管理嘅定價紀律生意」（agent ② 修正 v1「near unsolvable」）

## 3.1 v1 三個錯

1. **將成本通脹當敵人** — 通脹推高 claims 同時推高保費基數同投保誘因（港人低估獸醫開支 119%：[The Standard](https://www.thestandard.com.hk/hong-kong-news/article/320817/HK-pet-owners-underestimate-vet-costs-by-119pc-survey)）。真正殺人嘅係**重定價速度慢過成本**——營運問題，唔係結構問題。
2. **「加價必炸留存」被推翻** — Trupanion 加州一年加 29%，留存照升四季至 98.34%。關鍵係**點加**：cohort 定價（品種×投保年齡×地區獸醫成本）、成本傳導式歸因、高頻小步、direct-pay service moat。
3. **問錯問題** — 唔係問「有冇通脹」，係問「有冇槓桿 + 用唔用得快」。

## 3.2 Trupanion 實證（20 年通脹下嘅倖存者數據）

| 指標 | 數據 | 來源 |
|---|---|---|
| 2025 全年 | 收入 >**$1.4B**（+12%）、訂閱收入 $989M（+16%）、淨利 **$19.4M**（首次全年盈利）、訂閱寵物 1,096,173 隻 | [GlobeNewswire 官方業績](https://www.globenewswire.com/news-release/2026/02/12/3237668/0/en/Trupanion-Reports-Fourth-Quarter-Full-Year-2025-Results.html) |
| 目標賠付率 | ~70%（2025 實際 ~71%；2024 法定口徑 72.3%） | [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/4/new-us-pet-insurance-data-shows-doubledigit-growth-since-2017-88287943) |
| 獲客 IRR 閘門 | 內部目標 **30%**（2025 blended 30%、Q4 23% 並公開講明調節投放） | [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/02/12/trupanion-trup-q4-2025-earnings-call-transcript/) |
| 月留存 | **98.34%**（連升四季）→ 隱含平均投保 ~60 個月 | 同上 |
| 每寵獲客成本 | $288（2024：$235） | [StockStory/Yahoo](https://finance.yahoo.com/news/trup-q4-deep-dive-retention-053312761.html) |
| 行業對照 | 美國全行業淨賠付率 2024 = **78.89%**；NAPHIA：美國滲透率僅 4.27%，GWP $5.2B（+20.8%） | [S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/4/new-us-pet-insurance-data-shows-doubledigit-growth-since-2017-88287943)、[NAPHIA SOI 2026](https://naphia.org/wp-content/uploads/2026/06/NAPHIA_SOI2026_Report_HIGHLIGHTS_26-06-24.pdf) |

## 3.3 誠實保留項

香港獸醫通脹 **10–20%/年**（OneDegree 自報 18%）係美國（~5%）嘅 2–3 倍 → OneDegree 要嘅重定價速度同幅度係 Trupanion 嘅兩三倍，而且香港冇費率審批做消費者情緒緩衝。**難度更高，但槓桿種類一樣：執行力問題，非結構死局。** Trupanion 都用咗 20 年先行到 15% margin——「可管理」唔等於「易」。

---

# 第 4 節：薪酬核實（agent ③ — 機構級取代 aggregator）

## 4.1 機構級梯級（香港，底薪）

| 職級 | Michael Page | Morgan McKinley 2026 |
|---|---|---|
| Digital Marketing Manager | 平均 **HK$550K/年** | 平均 **HK$55K/月** |
| Marketing Manager | 平均 HK$600K/年 | 平均 HK$55K/月 |
| **Senior Marketing Manager** | 平均 **HK$800K/年（≈HK$61K/月×13）** | — |
| Marketing / Digital Marketing Director | — | 平均 **HK$80K/月** |

來源：[MP DMM](https://www.michaelpage.com.hk/salary-comparison-tool/digital-marketing-manager-salaries) · [MP Senior MM](https://www.michaelpage.com.hk/salary-comparison-tool/senior-marketing-manager-salaries) · [MM MM-HK](https://www.morganmckinley.com/hk/salary-guide/data/marketing-manager/hong-kong-sar) · [MM Director-HK](https://www.morganmckinley.com/hk/salary-guide/data/marketing-director/hong-kong-sar)

**市場環境**（Robert Walters 2025 調查轉述）：買方市場 — 申請量 +122%，77% 僱主只預備加薪 1–5%（[ICT Frame](https://ictframe.com/robert-walters-digital-salary-survey-2025/)）。

## 4.2 判決

| 問題 | 判決 |
|---|---|
| OneDegree 報 **HK$55,000/月**？ | ✅ **企得住** — 等於 Morgan McKinley DMM 平均，高 MP DMM 平均 ~20%，低 MP Senior MM 平均。屬市場中位偏上、有辯護力、唔離地 |
| Checkout.com 報 HK$65–75K/月？ | ✅ 可辯護；**75K 係天花板**（掂到 Director band 底） |
| v1 用嘅 ERI「647,828／830,932」 | 量級啱（貼機構中位）但係模型外推 — 唔好引用到個位數 |
| Indeed／PayScale／Glassdoor | 互相矛盾（同一職位月薪 50K vs 年薪 563K vs 800K）— 只做旁證 |

---

# 第 5 節：策略重建（agent ④ — 雙軌排序）

## 5.1 行動排序（而家點分配時間）

1. **OneDegree — 主動推進，今日內交申請。** 唯一一份「履歷唔使翻譯」嘅工；職位貼出 10 分鐘就發現，先發優勢每拖一日蒸發一日。缺口（Mixpanel/AppsFlyer、CAC/LTV 詞彙）48 小時內可用詞彙同 transferable 框架補。
2. **Activate Talent — 照去 screening，但只當高選擇權。** 成本 30 分鐘；四個未知（匿名客戶／僱傭形式／時區／薪酬）落地之前唔投入更多。JD 寫 2–5 年 vs 佢用 Leader 框你 → call 入面試探客戶預算級別。
3. **Checkout.com — 只行 Renee Yu warm route，唔 easy apply。** 先問 gate question（B2C 背景收唔收），答案係「收」先值得寫 CV。
4. **Deloitte Gen AI — 放棄；MarTech 線另計。**

## 5.2 職業質量排序（如果全部拎到 offer）

1. **Checkout.com** — 品牌最硬 + B2B fintech 新肌肉，10 年可選範圍擴一級；但命中率最低
2. **OneDegree** — 命中率最高 + 真操盤 + 「受監管行業增長」CV 標籤；盯住薪酬天花板（Glassdoor comp 2.7/5）、扁平架構升遷窄、預算受 CFO 緊盯
3. **Activate Talent** — 日常內容匹配最高，但匿名客戶喺香港履歷上品牌價值近零，contractor 可能冇 MPF 冇保障，downside 冇底
4. **Deloitte Gen AI** — 錯配

## 5.3 薪酬 scripts（照讀）

**OneDegree（申請表填 HK$55,000，唔自己讓步）：**
> "My expectation is around HK$55,000 monthly base. I'm flexible depending on the bonus structure, the actual scope of the role, how much team ownership comes with it, and the overall package."

被壓價時：
> "Before we talk about adjusting the number — what does the bonus look like at target, and is there a review cycle tied to performance in the first year?"

**Activate Talent（先問四件事，唔報價）：**
> "Happy to talk numbers, but I need context first. Four things: What's the client's budget range? Is this full-time employment or an independent contractor arrangement — through which entity? What are the expected working hours in Hong Kong time? And if it's a contract, does the rate account for me covering my own MPF, insurance, and paid leave?"

被迫報數：
> "If we're talking full-time with standard benefits and reasonable overlap hours, I'd anchor at HK$55,000 to HK$65,000 monthly. If it's a contractor arrangement on US hours, that's a different calculation entirely — I'd quote that separately once I know the structure. I won't compare the two one-to-one."

**Checkout.com（先問 band）：**
> "Could you share the budgeted range for this role first? I'd rather anchor to your framework than guess."

被迫報數：
> "I'd be targeting HK$65,000 to HK$75,000 monthly base. I'll be upfront: my background is B2C performance rather than B2B product marketing. What I bring that's hard to hire for is a production-grade AI content engine and native Chinese-market instinct — if those are worth a premium to you, the number reflects that; if not, I'd rather we find that out now."

## 5.4 面試問題庫（合併 agent ②④ + Codex 五條）

**OneDegree — 職權範圍（決定係真操盤定 interview theatre）**
1. "Does this role own the full growth loop — retention, CRM, the pricing page, product bundling — or is the mandate primarily paid acquisition, with retention sitting elsewhere?"
2. "Is this a replacement hire, a new headcount, or part of a restructure? If replacement — what did the last person struggle with?"

**OneDegree — 保險經濟（問得出呢啲先係 senior）**
3. "How is growth measured — policy count, gross written premium, earned premium, or contribution margin after claims? Which one is my number?"
4. "Your 240,000 policies figure — is that cumulative issued, or year-end in-force?"
5. "Over the last 24 months, what's been the average renewal increase on the pet book, versus the 18% pet medical inflation your own survey reported? Is there a repricing gap you're catching up on?"
6. "When cohorts received their largest renewal increases, what did retention look like versus untouched cohorts?"
7. "The 90% vs 70% network reimbursement differential is a strong steering tool — what share of claims dollars flows through network vets today, and do network clinics give negotiated rates or just data?"
8. "Does OneDegree budget growth spend against a cohort LTV or IRR framework — and what payback period do you underwrite to?"
9. "Walk me through how a new landing page or ad angle gets compliance sign-off — typical turnaround, fastest, slowest?"

**Activate Talent（30 分鐘內要攞到）**
時區（"The slots offered ran to 3:30am HK — is that representative?"）→ 僱傭實體 → MPF/假期等值 → 行業/階段/團隊規模 → 點解個位開（backfill？幾耐？）→ 年資錯配試探（"JD says 2-5 years; I'm at 8. Is the client open to senior, or is the budget set mid-level?"）

**Checkout.com gate question（俾 Renee Yu，問完先決定投唔投）**
> "Before I put together an application, one honest question: my 8 years are in B2C performance and growth, not B2B product marketing. Is the hiring manager open to a B2C growth background who'd bring an AI content engine and native Chinese-market fluency, or is prior B2B fintech/SaaS experience a hard requirement? I'd rather ask than waste your time with a mismatched application."

## 5.5 Pipeline 加闊（8 個 archetype）

1. 香港電商品牌 in-house Growth/Ecommerce Lead（Casetify、Zalora、大型 D2C 母嬰/美妝/寵物）— Baby Central 履歷直接複製
2. 虛擬銀行/虛擬保險（ZA Bank、Mox、Bowtie、Blue、WeLab）— OneDegree pitch 可重用四五次
3. 零售集團 digital transformation（屈臣氏、DFI/yuu、莎莎、周大福數碼）— 呢級請 mid-40s 資深人係 fit 唔係折扣
4. 中國品牌出海 HK hub（SHEIN/Temu 生態、Anker 類）— 三語 + 投放 + AI 內容量產精確命中
5. AI marketing tool vendor GTM/客戶增長（APAC）— 「用家轉 vendor」完美案例
6. 中小 agency Head of Performance / AI 轉型顧問 — @aieasyjob 受眾係獨有 inbound 渠道
7. 教育/培訓機構 growth — B2C 漏斗 + lifecycle 同母嬰電商同構
8. Fractional CMO retainer（並行收入）— 目的係令所有全職談判有 BATNA

渠道優先：LinkedIn（job alert + 每日 15 分鐘 recruiter outreach）> 目標公司直投 > 傳統獵頭（MP/RW digital desk — 呢個年資層獵頭有用）> JobsDB 保底。**@aieasyjob 每份申請都當 portfolio 連結放入去。**

## 5.6 十條「唔好做」

1. OneDegree 唔好填低過 HK$55K
2. Activate Talent 未知結構前唔講任何 HK$40–55K 區間
3. Contractor 報價唔同全職月薪 1:1 比
4. 唔扮識 Mixpanel/AppsFlyer —— 講 "I've run attribution on GA4 and Meta's ecosystem; app-side tools follow the same logic and I'll be fluent within weeks"
5. **唔好將本文件嘅 unit economics 模型當事實喺面試講 —— 全部轉做問題**（「我估你哋 CAC 係 X」= 扮嘢；「你哋點計 CAC payback」= senior）
6. 唔 easy-apply Checkout.com
7. 唔申請 Deloitte Gen AI
8. 唔為顯得後生而隱藏年資 — mid-40s + 8 年係 Senior Manager/Head 級定位
9. 未有書面工時承諾前唔答應任何深夜時段安排
10. 唔俾四條線嘅忙碌感掩蓋 pipeline 危機 — 真正可打得 1.5 條，本週按 5.5 開至少 5 個新申請

---

# 第 6 節：香港寵物市場數據（調解版）

| 數字 | 來源歸屬 | 用法 |
|---|---|---|
| 241,900 戶 / 405,200 隻（狗 221K + 貓 184K） | **政府統計處 THS 第 66 號（2018 調查）** — 施政報告 2025 引嘅就係呢組七年前數據 | 講「政府數據」時用，註明 2018 |
| 狗 304K / 貓 280K（2023） | 立法會研究簡報 ISSH32/2025 引市場估算（Euromonitor 系） | 講中期水平 |
| 狗 273K（–16% vs 2021）/ 貓 340K（+18%） | USDA FAS《HK Pet Food Market Report 2026》引 Euromonitor 2025 | 講**趨勢**（狗跌貓升、貓已多過狗） |
| 狗 430K / 貓 500K | Flanders 貿易推廣文件，無方法學，離群值 | **棄用** |
| 滲透率 8–10% | OneDegree 高管自述 | 引用須註明身份 |
| 市場規模 USD 8.5M | 聚合商模板數，同 OneDegree 自己收入矛盾 | **棄用** |

來源：[統計處公報](https://www.info.gov.hk/gia/general/201906/21/P2019062100361.htm) · [施政報告 §245](https://www.policyaddress.gov.hk/2025/en/p245.html) · [USDA FAS 報告](https://www.atohongkong.com.hk/wps/wp-content/uploads/HK2026-0009-Hong-Kong-Pet-Food-Market-Report-2026.pdf) · [立法會簡報](https://app7.legco.gov.hk/rpdb/en/file.aspx?id=cd5962402706404a81bdbcc41ad26516&type=pdf&lang1=en&lang2=en)

---

# 第 7 節：仍然無法核實（誠實清單）

1. **保監局 IA 個別公司數據**（OneDegree 官方 GWP／在保保單）— ia.org.hk 被本 session 網絡政策封鎖。**最高優先補做**：香港任何人可直接開 [IA 統計頁](https://www.ia.org.hk/en/infocenter/statistics/annual_general_business_statistics.html) 查
2. HK$3.3 億「收入」會計口徑（GWP／已賺／扣分保／含 Pet Mart？）
3. 現時在保保單數（10–15 萬係推算）
4. OneDegree 賠付率絕對水平（只披露「較 2020 改善 30%」）
5. 實際 CAC、佣金率、分保結構
6. 「78% of revenue」vs「78–85% of policies」措辭分歧
7. Robert Walters / Hays 香港 marketing 具體 band（gated download）
8. 英國/瑞典「30–40% 滲透率」一手出處
9. OneDegree 續保定價因素中「claims／通脹」逐字字眼（可能喺保單條款 PDF 內）
10. Trupanion 10-K 原文逐字（sec.gov 被封；數字經業績稿 + transcript + S&P 法定數據三角核實）
11. 所有「引句」均來自搜尋索引摘錄，原頁多數被 egress policy 封鎖 — 已盡量交叉核實但未能逐字對照

---

**文件結束。** v1 嘅方向性結論（OneDegree 值得投、係保險增長經濟學職位而非普通 ROAS 職位）保留；v1 嘅具體數字模型多數已被本版取代。使用規則：**模型做問題，唔做答案。**
