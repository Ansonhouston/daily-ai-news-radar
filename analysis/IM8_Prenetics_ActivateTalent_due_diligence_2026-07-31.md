# IM8 Health / Prenetics × Activate Talent — 盡職調查

**日期：** 2026-07-31（深夜）
**觸發事件：** Activate Talent recruiter Danny Mejia 於 2026-07-31 23:30 進行 10 分鐘 Google Meet，披露匿名客戶為 **IM8 Health / Prenetics (NASDAQ: PRE)**，並於 23:39 email 附上一份 12 頁 take-home test，要求「用週末」完成。
**製作方式：** 3 個並行研究 subagent（企業財務／中介商業模式／take-home 業界規範）+ 主線直接核實 GitHub 原始 brief 同 email header。
**結論：** **已退出 Activate Talent 流程。轉為直投 Prenetics 香港資深職位。**

> **使用規則：模型做問題，唔做答案。** 本文件所有 unit economics 推論只用於面試偵察，唔可以當事實陳述講出口。
> **來源限制：** 本 session egress policy 封鎖大部分主站直讀（SEC.gov、ir.prenetics.com、careers.prenetics.com、Glassdoor、Reddit、Trustpilot 等全部 403）。除 GitHub raw 外，數據來自搜尋層摘錄而非親自讀原頁。載重數字須自行覆核。

---

# 第 0 節：決策摘要

| 項目 | 判斷 |
|---|---|
| IM8/Prenetics 係唔係好機會 | ✅ **係** — 真公司、香港總部、增長真實、剛獲 10 億美元營銷融資 |
| Creative Strategist 呢個位適合 Anson 嗎 | ❌ **唔適合** — 2–5 年、有 Junior 版、中層 IC。Anson 8 年 = 降級 |
| 應否經 Activate Talent | ❌ **唔應該** — 離岸成本套利中介、香港零足跡、閘門公開所以中介零 gatekeeping 價值 |
| 應否做嗰份 6–8 小時 test | ❌ **唔做** — 次序倒轉（未見 hiring manager）、超業界規範 2–4 倍、要交 prompt library |
| 最終行動 | **清乾淨退出 → 直投 careers.prenetics.com 嘅 Head of Social — IM8 / Head of Performance Marketing — IM8** |

---

# 第 1 節：最重要嘅單一發現 — Brief 係公開嘅，而 Anson 收到嘅係閹版

份 test **公開喺 GitHub：`github.com/Prenetics/beat-claude`**

以下係**官方原版有、但 Danny 那份 PDF 完全冇提**嘅規格：

| 官方規格 | Danny 版本 |
|---|---|
| **PDF 或 Google Slides，最多 4 頁** | ✗ 冇提 |
| **必須附 Loom 影片講解思路** | ✗ 冇提 |
| **收到 brief 起 5 個日曆日** | ✗ 冇提 |
| 交去 careers portal **或 `recruitment@prenetics.com`**，subject「Beat Claude — Creative Strategist — [Your Name]」 | ✗ 冇提 |
| 必須提供**現時薪金 + 期望薪金** | ✗ 冇提 |

**兩個實質後果：**

1. **4 頁上限徹底改變工作性質** — 唔係窮盡式審計，而係殘酷綜合。主線初期基於閹版 brief 估算「25–40 小時」**係錯的，已更正**。有 4 頁上限，6–8 小時屬 plausible。
2. **按閹版去做會死** — 交一份 20 頁詳盡 deck 即違反指示，而 Presentation & Communication 佔 10%，rubric 明問「Can someone skim it and get the key points?」大多數收到同一份閹版嘅候選人會喺呢度輸。

**Prenetics 全公司共 8 個 beat-claude 挑戰：**

| 挑戰 | 難度 |
|---|---|
| Creative Strategist — IM8 | Hard |
| Influencer Marketing Manager — IM8 | Hard |
| CRO Manager — IM8 | Hard |
| Customer Experience Manager — IM8 | Hard |
| Supply Chain Manager — IM8 **Hong Kong** | Hard |
| Social Media Manager — IM8 | Medium |
| Retention & Lifecycle Manager — IM8 | Medium |
| Marketing Intern — IM8 | Medium |

⚠️ **Head of Social 同 Head of Performance Marketing 唔喺呢個名單上** → 大機會走正常流程、直接見人。**呢個就係直投目標。**

---

# 第 2 節：IM8 / Prenetics 已核實事實

## 2.1 公司結構

| 項目 | 數據 | 來源 |
|---|---|---|
| IM8 定位 | Prenetics Global Limited (NASDAQ: PRE) 旗下品牌，**非獨立上市公司** | [ir.prenetics.com](https://ir.prenetics.com/news-releases/news-release-details/multimedia-update-nasdaq-listed-prenetics-and-david-beckham) |
| 正式推出 | **2024-11-18**，兩款產品，發貨 31 個國家 | [PRNewswire](https://www.prnewswire.com/apac/news-releases/nasdaq-listed-prenetics-and-david-beckham-officially-launch-im8-health-302308583.html) |
| Beckham 角色 | **「co-founding partner」兼 IM8 股權持有人**（自成立起），另為 Prenetics 策略投資者 — 實質超越純代言 | [Prenetics](https://prenetics.gcs-web.com/news-releases/news-release-details/prenetics-unveils-im8-us-consumers-co-founding-partner-david) |
| 僱主實體 | **Prenetics**，非獨立 IM8 實體；所有 IM8 職位貼喺 `careers.prenetics.com` | [careers.prenetics.com](https://careers.prenetics.com/) |
| Prenetics 總部 | **香港**。2014 年由 Danny Yeung + Lawrence Tzang 創立 | [prenetics.com](https://www.prenetics.com/about-us) |
| 上市方式 | 經鄭志剛 Artisan Acquisition Corp SPAC 合併（2021 宣佈、2022 完成） | [IR](https://ir.prenetics.com/news-releases/news-release-details/prenetics-global-leader-genomic-and-diagnostic-testing-become) |

**UNVERIFIED：** Beckham 股權喺 IM8 子公司定 Prenetics 母公司、持股比例（未披露，應在 20-F 關聯方章節）。

## 2.2 母公司財務 — 疫後崩塌係真實且嚴重

| 年度 | 收入 |
|---|---|
| FY2020 | US$65M |
| FY2021 | US$205M |
| FY2022 | **US$275.8M** |
| FY2023 | **US$21.7M**（持續經營） |
| FY2024 | US$30.6M |
| FY2025 | **US$92.4M** |

SPAC 時期指引「2025 年 >US$600M」→ 實際 US$92.4M，**差約 85%**。

| 風險項 | 事實 |
|---|---|
| COVID 業務 | 檢測業務 **2023 Q2 全面停止**；EMEA DNA 檢測 2023 Q4 停止；US$2.4M 重組費用 |
| 反向分割 | **2023-11-13 生效 1 兌 15**，明確為符合 NASDAQ US$1 最低股價、避免除牌 |
| 持續經營虧損 | FY2024 US$(38.4)M → FY2025 **US$(55.0)M**（擴大） |
| 比特幣 | 2025-06 起買入，現持 ~**510 BTC（~US$45M）**，已停止增持；**Q1 2026 淨虧損內含 US$9.8M 未實現數字資產虧損** |
| 資產出售 | ACT Genomics 多數股權售 Delta Electronics US$72M（2025-10-01 完成）；Insighta 35% 股權售 US$70M 現金（2026-02 完成） |
| 市值 | ~**US$0.3B**（2026-07-29, Macrotrends）vs 2026 收入指引 US$210–220M → **股市冇 buy 佢新聞稿嘅增長故事** |

⚠️ **新聞稿放大傾向：** FY2025 稿標題寫「Revenue Surges 480% YoY」。$92.4M vs $30.6M 實為 **+202%**。「480%」最可能描述 IM8 而非總收入。**讀 Prenetics 任何數字都要自己核。**

**Q1 2026（截至 2026-03-31）：**
- 總收入 US$36.0M；**IM8 US$33.8M**（Q1 2025: $5.7M；Q4 2025: $27.4M，+23.1% QoQ）
- 毛利 US$23.3M，**65% 毛利率**
- **淨虧損 US$(23.1)M**（含 $9.8M 數字資產 + $8.0M warrant 公允值虧損 → 剔除非現金約 $(5.3)M）
- 營銷開支 ~US$22M vs IM8 收入 $33.8M = **65%**
- 現金 US$56.0M（3月底）→ ~US$83.4M（5月底）— **靠資產出售同增發，非營運現金流**

**UNVERIFIED：** FY2025 20-F 有冇 going-concern 或 material weakness 語句（未能讀取核數師報告）。**唯一搵到「substantial doubt」語句係關於 Insighta（權益法投資對象），非 Prenetics 本身。** 未搵到 2023 反向分割後任何除牌警告。

## 2.3 IM8 商業牽引力

**公司口徑（未經獨立審計）：** 0 → >US$100M ARR / 11 個月；US$120M ARR（2025-12）；FY2025 IM8 收入「超過 US$60M」；2026-05 單月收入 ~US$16.7M（+19.3% MoM）；43 個國家；>60% 收入來自美國以外；>800,000 客戶；FY2026 IM8 指引 US$190–210M。

**第三方可驗證子集：只有 Q1 2026 IM8 收入 US$33.8M 屬正式報告數字。**「ARR」「annualized run-rate」「$200M」全部係**單月年化**，屬公司呈述選擇而非報告結果。

## 2.4 🔑 已披露 unit economics — 呢個係求職者嘅武器

| 指標 | 數據 |
|---|---|
| FY2025 AOV | **~US$110** |
| FY2025 CAC | **~US$130** |
| 24 個月 LTV | ~US$480 |
| 2026 初 AOV | 升至 ~US$233 |
| 訂閱者 | **~82,000**（Q1 2026） |
| 累計客戶 | >800,000（公司口徑） |
| S&M 佔收入 | FY2025 38.5% → **2026 指引 45–50%** |
| 公司聲稱 | 「every \$1 in customer acquisition returned \$1.44 in gross profit, **blended across all mature cohorts**」← 注意限定詞排除近期未回本 cohort |

**推論（ASSUMPTION，只做面試問題）：**
- **CAC $130 > AOV $110 → 每張首單蝕住賣，全部回本壓喺留存**
- **82,000 ÷ 800,000 ≈ 10% 訂閱附著率** — 對自稱 subscription-model 嘅品牌屬軟弱
- → 真正創意問題**唔係「廣告數量不足」**，而係**首單訂閱附著 + 留存創意缺失**

## 2.5 General Catalyst 10 億美元融資（2026-07-14，即事發前兩週）

**結構（要睇清，新聞標題全部誤導）：**
- **唔係股權。** General Catalyst 嘅 **Customer Value Fund (CVF)** 按月出資支付 IM8 **最多 70% 月度營銷開支**，以 cohort 為單位，換取 cohort 層收入嘅上限分成，直至還足固定倍數
- 非攤薄、無股權無認股權證、無固定到期日、無契約條款、除被融資 cohort 外無追索
- 帳列**金融負債**，回報記作**利息支出**

⚠️ **標題衛生：** 媒體寫成「IM8 secures \$1 billion」/「raises \$1B without selling a single share」。實為**承諾額度嘅營銷融資 facility，隨開支動用** — 唔係 10 億現金入帳，唔係 10 億估值事件。當作 CAC 融資循環額度嘅上限。

**對求職者意義（INFERENCE）：** IM8 嘅投放預算已被設計成硬性擴張，創意產出量預期會極高（「thousands of ad variations per month」有咗財務基礎）。同時創意產出直接決定被融資 cohort 還唔還得起錢 → 責任壓力真實。

## 2.6 🔴 CMO 已離職，無繼任人

- **Kate Paulley**（由 launch 起架構 IM8 品牌同增長策略嘅 CMO）LinkedIn headline 用**過去式**：「Global CMO & Growth Operator | **Led** IM8…」
- SignalHire（2026-05-07 更新）列現職為 **Kind Marketing 創辦人 & Growth Strategist**；ZoomInfo 相同
- **未搵到任何繼任 CMO、VP Growth 或 Head of Creative 公告**

同時同步招聘：Creative Strategist、Junior Creative Strategist、Head of Social、Social Media Manager、CRO Manager、Retention & Lifecycle Manager、Junior Designer、Influencer Marketing Manager、Video Editor。

**INFERENCE（非事實）：呢個唔係「擴張招聘」，係一個營銷組織喺可能冇 sitting CMO 嘅情況下被重建。**

→ **面試第一問：「Who does this role report to, and is that person currently in seat?」**

## 2.7 已知營銷組織架構

| 角色 | 狀態 |
|---|---|
| CMO | **疑似空缺**（Kate Paulley 已離） |
| VP of Growth | 存在（Influencer MM 直接匯報） |
| Head of Paid Media | 存在 |
| **Head of Social — IM8** | 招聘中，**香港島 hybrid**，6+ 年 social + 2+ 年帶 DTC/consumer/**creator-focused** 公司 |
| **Head of Performance Marketing — IM8** | 招聘中，**香港島** |
| Creative Strategist | 招聘中，2–5 年，中層 IC |
| Junior Creative Strategist | 招聘中，Remote |
| Social Media Manager — IM8 | 招聘中，香港 hybrid，全市場 US/UK/HK/APAC |
| CRO Manager — IM8 | 招聘中（與 Head of Paid Media + Creative Strategist 平行） |
| Retention & Lifecycle Manager — IM8 | 招聘中，HK 優先，開放 US/UK 但需定期來港 |
| Influencer Marketing Manager | 招聘中，向 VP Growth 匯報，**八位數預算** |
| Junior Designer — IM8 | 招聘中 |

**外部夥伴：** Jack Taylor = 全球 PR AOR（2024-12 起合作）；Paracosm Creative（AI agency）製作 Sabalenka 時代廣場廣告。**未搵到 paid-media AOR** — 公司框架為內部「AI-native acquisition engine」。

## 2.8 僱主評價

Glassdoor（Prenetics，E1789930）：**3.6/5，299 條評價，57% 推薦**；薪酬福利 3.4、work-life 3.6、文化 3.6、職涯機會 3.5。標題由「Great place」到「**Run for your life, save your breathe**」。

**INFERENCE：** 299 條評價基數幾乎肯定偏向 2021–23 COVID 檢測人力高峰期，描述嘅係**另一間公司**。應輕度加權。

**UNVERIFIED：** 集團同 IM8 人數；levels.fyi 完全無 Prenetics/IM8 薪酬數據。

---

# 第 3 節：Activate Talent

| 項目 | 事實 | 來源 |
|---|---|---|
| 性質 | 洛杉磯總部離岸／近岸人才配置公司，提供招聘 + **EOR** + payroll + onboarding + compliance | [LinkedIn](https://www.linkedin.com/company/activate-talent) · [NextInHR](https://nextinhr.com/agency/activate-talent) |
| 規模 | **21–50 人**，估計年收入 **~US$4.28M**，**從未融資** | [Prospeo](https://prospeo.io/c/activate-talent-revenue) · [Crunchbase](https://www.crunchbase.com/organization/activate-talent) |
| 領導層 | CEO/共同創辦人 **Jared Orkin**（定位：「proving the best teams aren't always local」）；COO Jara Soriano；Head of Sales Alexandra Burgess | [theorg](https://theorg.com/org/activate-talent) |
| 招聘地域 | **菲律賓、哥倫比亞、墨西哥、巴西、多明尼加、肯尼亞、南非、加拿大、美國**。辦公室：LA、宿霧、Quezon City | [Remote4Africa](https://remote4africa.com/companies/activate-talent) |
| **香港** | **完全唔喺其地域足跡或辦公室名單內。未搵到任何香港存在、香港職位或香港配置。** | 同上 |
| 成本套利定位 | Indexed copy：「Hiring in the Philippines or India isn't just cost-effective… **Save up to 60%** while getting top-notch talent」（**逐字未核實，主題已核實**） | [activatetalent.com](https://www.activatetalent.com/) |
| Rate card | **不存在。所有職位貼出嚟都冇薪酬。** | Remotive / Jobgether / Jobstreet PH / ZipRecruiter 全部 |
| 僱傭形式 | 明確提供 **EOR**（即 Activate Talent 或其 EOR 夥伴為法定僱主）；亦有明確 **independent contractor** 職位 | [NextInHR](https://nextinhr.com/agency/activate-talent) · [ZipRecruiter](https://www.ziprecruiter.com/co/Activate-Talent/Jobs) |

**離岸同業對照價（用於推算報價區間）：**
- 離岸媒體投放員 ~US$15/hr ≈ **US$2,400/月**（vs 美國 freelancer $45–70/hr）
- 熟練離岸媒體投放員 **US$1,000–4,000/月**（vs 本地 $6,000–10,000/月）
- 資深 PPC：美國 $70–90K/年 vs **拉美 $28–36K/年**
- 菲律賓遠端：**US$700–4,500/月**；拉美遠端：**US$1,000–6,500/月**
- 同業 Paired / Somewhere 宣傳「減少最多 80% 薪資成本」

**評價：** Glassdoor **4.8/5（95–97 條）、94% 推薦**，但**雙峰分佈** — 有 1 星「Worst experience I've had」（前資深招聘員）、「Dissapointng, worst management from CEO I've ever experienced」。Trustpilot **4 星但只有 9 條**，搜尋摘錄顯示有 ghosting 投訴（面試後停止回覆）。有一條記錄：候選人完成數小時 assessment 後兩星期無回覆（覆核跟進亦無果）。**Reddit 完全零討論**（該平台本 session 亦被封，屬「無證據」非「證據為無」）。Scamadviser 評為合法。

**INFERENCE：** 一間 21–50 人配置公司有 4.8/95 條 Glassdoor 且正評集中於「recruiters 主動」，符合內部／邀約式評價特徵。應重視 1 星離群值同薄弱 Trustpilot 多於總平均。

**「Danny Mejia」身份 — 已由 email header 解決（見第 5 節）。**

**INFERENCE（高信心）：香港對 Activate Talent 屬異常，對客戶屬原生。** Activate Talent 係代 Prenetics 尋才，香港元素來自客戶而非中介。Prenetics 嘅 Creative Strategist 職位標示 remote/global → **一個香港候選人仍可能收到本地市場費率報價，而呢個正係套利模式咬落嚟嘅位置。**

---

# 第 4 節：Take-home 業界規範 — 呢份 test 超標

## 4.1 硬數據

| 指標 | 數據 | 來源 |
|---|---|---|
| 約 200 個公開 take-home 中位時數 | **3 小時** | [careerfair.io](https://www.careerfair.io/takehome-assessments) |
| 其中講明會補償嘅比例 | **~10%** | 同上 |
| ~700 人調查：應 ≤4 小時 | **>80%** | [interviewing.io](https://interviewing.io/blog/why-engineers-dont-like-take-homes-and-how-companies-can-fix-them) |
| 理想時數眾數 | **2 小時** | 同上 |
| 建議上限 | **2 小時**；超過應付錢；>1–2h 屬**公平性**問題非禮儀問題 | [RecruitingDaily](https://recruitingdaily.com/navigating-take-home-assignments-for-effective-and-equitable-hiring/) |
| 正常派發階段 | **見完 hiring manager 之後**，final round 前後 | [InterviewQuery](https://www.interviewquery.com/interview-guides/workday-growth-marketing-analyst) |

**「非常早期派 take-home」= 明確列為 immediate red flag**，標準建議係**相反次序**（先傾完確認雙向匹配再投入時間）。此模式有專門討論串（Blind「take home assignment after recruiter screening」等），屬公認投訴而非個別經驗。

## 4.2 AIGA 正式立場 + 規定替代方案

AIGA 維持反對 spec work 立場（[AIGA Position on Spec Work](https://www.aiga.org/resources/aiga-position-on-spec-work)），理由：品質（排除研究同原型測試）、剝削（「Some clients may see this as a way to get free work」）、法律／IP 風險、應獲公平補償並協商權利歸屬。

**AIGA 規定嘅道德替代方案（載重句）：** 要求候選人提交**過往作品範例 + 一份書面「我會如何 approach 你個項目」陳述**。

## 4.3 Spec work 診斷標記（呢份 test 全中）

| 標記 | 呢份 test |
|---|---|
| 交付物可直接用於真實在營問題 | ✅ 佢自己寫「This challenge mirrors a real first project at IM8」 |
| 用公司真實現行具名問題非消毒／歷史案例 | ✅ 真實品牌、真實 Meta Ad Library、真實競品 |
| 極早期派發 | ✅ 10 分鐘 recruiter screen 之後 |
| 範圍超出讀取訊號所需 | ✅ 6–8h 官方估算 = 業界建議上限 2–4 倍 |
| 無補償且無主動提及補償 | ✅ 全文零提及 |
| 交付物為**可即執行格式**（deck/calendar/plan）而非推理格式（memo/approach） | ✅ 4 頁 deck + 30 日 calendar + 10 個 concept |
| 披露不對稱 | ✅ 候選人交策略 + 現時薪金 + 期望薪金 + prompt library；公司零披露薪酬／團隊／匯報線 |

## 4.4 🔑 IP 歸屬 — 法律結論

| 認知 | 法律實際 |
|---|---|
| 我交出去，版權仍係我 | ✅ **無書面協議下候選人擁有文件版權**（work-made-for-hire 需僱傭關係或簽署書面協議，候選人兩者皆非） |
| 佢用我方法我可以追 | ❌ **版權只保護表達，唔保護思想／方法。** 公司可合法執行你提議嘅策略而從不複製你嘅文件 |
| 執法可行嗎 | ⚠️ 「could be very expensive for the interviewee and may not result in much by way of damages」— 現實救濟係槓桿同聲譽壓力，非訴訟 |
| 另有 FLSA 角度 | 若公司將作品用於**評估以外**用途而不付酬，多數情況可能違反 FLSA（含等額懲罰性賠償） |

**已記錄（新聞／第一人稱，非判決）商業使用案例：** 30 小時作業；為公司活動做籌備；候選人所寫文章後來未具名出現在公司網站 — **上述三人全部未被錄用**。另有「無人被錄用但候選人幾乎所有想法都被執行」案例。**誠實限制：未搵到任何具名、經審判嘅案例。**

**建議做法：** 提交前 email 聲明「all ideas will be shared solely for interview purposes / 我保留所有權」 — 未被反駁嘅 email 即係證據，成本零。
**負面發現：** 未搵到任何招聘業界建議為 take-home 加水印。屬一般版權實務嘅合理外推，**不可當業界規範引用**。

## 4.5 🔴 「Beat the AI」format — 業界零紀錄，且前提已被推翻

**多種查詢方式搜尋結果：零案例、零評論、零法律分析。** 唯一同類實作為 Single Grain / Eric Siu（`ericosiu/beat-claude`，措辭不同、明確拒絕公佈 rubric），該 repo 明確 credit **Anthropic 原始 performance take-home** 而非 Prenetics。

**→ 呢個唔係業界做法。係個別僱主嘅獨創做法。任何將其呈述為標準實務嘅公司都係在誤述行業狀態。**

**而業界真實走向係相反方向：**

Anthropic（Claude 製造商）2026-01-22 發表《Designing AI-resistant technical evaluations》：
- **Claude Opus 4 已勝過大多數人類申請者**（相同時限下）；**Claude Opus 4.5 已追平最強候選人**
- 逐字：**「Humans can still outperform models when given unlimited time, but under the constraints of the take-home test, there is no longer a way to distinguish between the output of top candidates and the most capable model.」**

**→ Prenetics 整個閘門建立喺一個「你要贏 AI」嘅區分上，而模型製造商已公開證明喺 take-home 時間預算下嗰個區分唔存在。**

IBM 方向：轉為評估候選人**監督同修正機器產出**嘅能力，而非與之競爭。

**適用批評（非針對此 format 但直接轉移）：**
1. **冇工作工具嘅測試 = 測試一個唔存在嘅環境。** 營銷人真實工作包含 AI 工具，所以「赤手空拳贏 AI」量度唔到任何職務相關能力
2. **雙重標準** — 公司用 AI 寫 JD、用 AI 篩人，然後因申請者疑似用 AI 而拒絕
3. **有效性缺陷** — 一個**未經驗證、未公佈、單一實例**嘅 AI 產出作為評分閾值，係一個**無已證實職務相關性嘅選拔標準**。此為任何選拔工具嘅經典弱點，與是否涉及 AI 無關
4. **AI 參與僱傭決定** → 即使無 AI 專門法規，僱主仍須負公平性、透明度、結果責任（可能觸發 NYC LL144 式偏見審計、Illinois、Colorado、EU AI Act 高風險僱傭分類義務）

## 4.6 🔴 Prompt library — 最高風險項

| 認知 | 法律實際 |
|---|---|
| Playbook 可以係 trade secret | ✅ 可以 — **但 trade secret 地位以實際保密為存續條件** |
| 交出去之後仲有保護 | ❌ **無 NDA 下自願披露 = trade secret 地位即時消滅，且不可逆。** 冇回頭路 |
| 版權可補位 | ❌ 版權保護文件表達，**唔保護方法**。而 prompt library 嘅價值**就係方法** |

**最有力嘅一點：** 僱主方法律最佳實務（Seyfarth Shaw / Trading Secrets）係**主動避免**候選人披露機密資料，「focus the candidate on general skills and knowledge」— 因為收到會污染自己。

**→ 一個有律師指導嘅僱主根本唔想要你嘅 prompt library。主動索取嘅僱主，唔係指導不足，就係為咗嗰樣嘢本身而索取。**

**防線：** 展示能力，保留可重用資產。
- **保留：** prompt 原文、system prompt、chained workflow、具名 playbook/SOP/決策樹、可重用模板同計算器、工具棧配置同自動化邏輯
- **可交：** 經編輯嘅產出同結果、**原則層級**嘅方法描述、**live demo**（最關鍵 — 將資產轉移變成一次演出，零可重用檔案流出）、自己完全擁有嘅過往作品

**腳本：**
> "Happy to walk you through my process live and you can push on any part of it. What I don't share outside a signed agreement is the prompt library and playbooks themselves — those are the assets I've built and they're the same ones I'd be bringing to the role. Hope that reads as protecting my work rather than withholding from you."

---

# 第 5 節：Email header 鑑證（2026-07-31 23:39）

| 欄位 | 值 |
|---|---|
| 寄件者 | `Danny Mejia <danny@activatetalent.com>` |
| 日期 | **2026-07-31 23:39**（Google Meet 為 23:30） |
| 主旨 | `IM8 Creative Strategist **Tets**`（串錯「Test」） |
| DKIM 簽署網域 | **`activatetalent-com.20251104.gappssmtp.com`** |
| 安全性 | 標準 TLS |
| 附件 | `IM8 Creative strategist Test.pdf`（**閹版**，見第 1 節） |

## 5.1 判定

✅ **Email 真實，未被冒充。** `gappssmtp.com` 係 Google 自身基礎設施域名；格式 `<域名點換橫線>.<YYYYMMDD>.gappssmtp.com` 係 Google Workspace **預設 DKIM 簽章**。`activatetalent-com` = `activatetalent.com` → 郵件確由該 Workspace 租戶發出。

**→ 先前「Danny Mejia 搵唔到 LinkedIn」嘅黃旗降級為小疑問，非風險訊號。**

⚠️ **但佢哋從未設定自訂 DKIM。** 簽章域名本應為 `activatetalent.com` 本身（發佈自有 DKIM key 後即如此）。技術後果：預設 gappssmtp 簽章**唔會同 From 域名 align**，故其 DMARC 保護完全依賴 SPF alignment。對一間**大量發候選人 email、處理個人資料**嘅招聘公司屬低於標準嘅郵件衛生。**成熟度訊號**，符合 21–50 人／~US$4M 規模。

（`20251104` = Google 為該域名生成預設 DKIM key 之日期，通常為加入 Workspace 或更換金鑰之時。Activate Talent 於 2025-11 前已存在，故最可能為遷移日期 — **不由此推論公司年齡**。）

## 5.2 時間戳揭示嘅更重要事實

**Google Meet 23:30 → Email 23:39。** 郵件喺通話開始後 9 分鐘、即一收線就發出。

**→ 份 PDF 係預先準備好嘅，與 Anson 喺 call 中表現完全無關。**

配合：主旨串錯字、內文極簡、附件檔名大小寫不一致 → **低投入、高數量嘅群發行為。**

**結論：呢個唔係「佢覺得你好所以派功課」。呢個係一個預載附件 + 一個 10 分鐘形式化通話。個 call 冇篩選功能。**

**→ 唔可以將「佢派 test 俾我」讀成任何形式嘅認可。**

## 5.3 真實期限

官方 repo：「5 calendar days from when you receive the brief」。收到 = 2026-07-31 23:39 → **真實期限約 2026-08-05（星期三）**，非 Danny 口述嘅「呢個週末」。

**→ Danny 壓縮咗 3 日。可能係佢自己交客戶嘅內部 deadline，可能係製造緊迫感。** 而既然期限由「收到 brief」起算而 brief 公開喺 GitHub，該時鐘嘅歸屬本身模糊。

---

# 第 6 節：最終決策同行動

## 6.1 決策：退出 Activate Talent 流程

**理由排序：**
1. **職級錯** — Creative Strategist 為 2–5 年、有 Junior 版、夾喺 Head of Paid Media 同 CRO Manager 之間嘅中層 IC。Anson 8 年、mid-40s、目標 HK$55K → 降級投
2. **通道差** — Activate Talent 香港零足跡、零公開薪酬、EOR/contractor 模式、成本套利為核心產品
3. **中介零 gatekeeping 價值** — brief 公開喺 GitHub，官方交件地址為 `recruitment@prenetics.com` 或 careers portal。中介唔守住任何入口，只抽成
4. **流程次序倒轉** — 業界標準係見完 hiring manager 才派 take-home；此處為 10 分鐘、附件預製、匯報線未答之 recruiter screen 之後
5. **超業界規範 2–4 倍** — 6–8h vs 建議上限 2h / 中位 3h；且僅 ~10% take-home 會補償
6. **前提已破** — 「贏 AI」建立喺 Anthropic 自己已推翻嘅區分上
7. **不對稱極端** — 交 6–8h + 現時薪金 + 期望薪金 + prompt library；收到零薪酬範圍、零團隊資訊、零匯報線

## 6.2 退出信（已交付，不燒橋、不披露後續動向）

> Hi Danny,
>
> Thanks for the call and for sending the brief over.
>
> After reviewing it, I'm going to withdraw from this process. The assignment is a 6–8 hour build, and at this stage I haven't had a conversation with the hiring manager, don't have the reporting line, and don't have a budgeted range for the role. I'm not comfortable committing that much work before any of those are established — that's a scoping issue on my side, not a reflection on you or the client.
>
> If a role comes up where there's a hiring-manager conversation earlier in the process, I'd be glad to hear about it.
>
> Best,
> Anson

**不提直投計劃。** 退出理由句句真實；但披露會令中介有動機**搶先 submit CV 以 claim attribution**，之後直投即撞入 fee 爭議。Anson 未簽任何獨家協議，職位公開招聘，brief 公開可得 → 清乾淨退出後自行直投完全正當。

## 6.3 直投目標（`careers.prenetics.com`）

| 優先 | 職位 | 匹配理由 | 缺口 |
|---|---|---|---|
| **1** | **Head of Social — IM8**（香港島 hybrid） | 6+ 年 social ✓（8 年）；「**creator-focused** company」← Anson 本身就係 creator；76K organic Reel（77 followers 起，~990x）；200+ KOL；84K YouTube views / 57 條片。**不在 beat-claude 8 個挑戰名單** → 大機會正常流程直接見人 | ⚠️ **要求「2+ years leading a social function」— Anson 係 solo 營運，未帶過團隊。真實缺口，須正面處理（「一個人做出團隊產出量 + 我建嘅 pipeline 就係我嘅團隊」），不可假裝不存在** |
| **2** | **Head of Performance Marketing — IM8**（香港島） | HK$3M+ 累計投放 @ 3–10x ROAS；峰值 HK$500K+/月 @ 3–7x；ROAS 0.3x→3x 救亡；+200% CVR。**亦不在挑戰名單** | 職級要求未核實 |
| 3 | Influencer Marketing Manager | 向 VP Growth 匯報、八位數預算；200+ KOL programme 直接對口 | 有 Hard beat-claude 挑戰 → 放後 |

## 6.4 面試必問（若進入流程）

1. **「Who does this role report to, and is that person currently in seat?」** ← 最高優先（CMO 疑似空缺）
2. "How is growth measured — new customers, subscription starts, GWP-equivalent, or contribution margin after CAC? Which one is my number?"
3. "Your disclosed FY2025 numbers showed AOV around \$110 against CAC around \$130. How does the team think about first-order economics versus subscription attach?"
4. "With the General Catalyst CVF facility financing cohort-level marketing spend, how does that change the reporting cadence and the payback discipline on creative?"
5. "82,000 subscribers against 800,000-plus customers — is lifting subscription attach a creative mandate or a CRO/lifecycle mandate?"
6. "Is this a new headcount, a replacement, or part of the marketing rebuild? If replacement — what did the last person struggle with?"

⚠️ **全部轉做問題，唔好當事實陳述。**「我估你哋 CAC 係 X」= 扮嘢；「你哋點計 CAC payback」= senior。

## 6.5 紅線（任何情況適用）

1. **絕對唔交真實 prompt library**（trade secret 一次性且不可逆消滅）
2. **「現時薪金」欄位** — freelance 身份，報**年化等值**，唔好報低月薪（錨點陷阱）
3. **期望薪金** — Creative Strategist 級不低於 **HK$55,000/月**（= Morgan McKinley DMM 平均）；Head 級須更高
4. 任何提交前先 email 聲明「shared solely for the purpose of evaluating my candidacy, ownership retained」
5. 若再遇 take-home：**4 頁就 4 頁**（跟指示係 10% 分數）、**6 小時封頂**、優先反提議 **60–90 分鐘 live working session**（結構上無法被再用作交付物 — 拒絕 live session 而堅持要文件嘅公司，已用該拒絕告訴你文件本身就係目的）

---

# 第 7 節：仍未核實（誠實清單）

1. **FY2025 20-F 有冇 going-concern／material weakness 語句** — 未能讀核數師報告（SEC.gov 被封）
2. IM8 Creative Strategist 直接 req 嘅薪酬、地點、職級（`careers.prenetics.com` 403）
3. Head of Performance Marketing 嘅具體年資要求同匯報線
4. Prenetics 集團同 IM8 人數
5. Beckham 股權層級同比例
6. Activate Talent rate card、此個案嘅法定僱主實體、被配置營銷人員有冇福利
7. IM8 現任營銷最高負責人（如有）
8. Prenetics 營運現金流實數（僅有 Adj. EBITDA 同現金餘額）
9. 「480% YoY」新聞稿口徑對帳
10. Activate Talent 候選人投訴嘅 Reddit 規模模式（平台本 session 被封 → 無證據 ≠ 證據為無）

---

**文件結束。**

**一句話結論：** IM8/Prenetics 係一個真實、增長中、剛獲 10 億美元營銷融資、營銷組織正在重建（可能無 CMO）嘅香港總部 NASDAQ 公司 — **值得投**；但 Activate Talent 嘅 Creative Strategist 通道係一個職級錯配、成本套利、流程次序倒轉、要求交出護城河嘅入口 — **已退出**。**同一份情報轉用於直投香港島資深職位。**
