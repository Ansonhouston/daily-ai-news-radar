# 多智能體事實紀律模式（總指揮 + 4 現實真人 Subagent）

> 起源：2026-07-31，Codex 獨立審視捉到 v1 分析多處推導錯誤後建立。
> 用途：任何公司審視 / 職位深度分析 / unit economics 推導，一律行呢套，唔准 solo 吹水。

## 觸發條件（任一命中即啟動）

- 用戶要求「公司審視 / 公司分析 / deep dive / 呢間公司點」
- 分析涉及 unit economics（LTV / CAC / payback / 續保率 / 利潤率推導）
- 面試前準備涉及公司財務或行業結構判斷
- 用戶話「唔好吹水 / 要事實 / 要市場數據」
- 任何 v1 分析被第二個 AI（ChatGPT / Codex / Gemini）審視後需要重建

## 架構：總指揮 + 4 Subagent 並行

主對話做總指揮：定分工、寫 prompt、等齊 4 個先合成，唔自己落場填數。
4 個 subagent 用 Agent tool 一次過並行派出（general-purpose，有 WebSearch）。

| # | Subagent | 真人方法論（必須可查證嘅真人/機構） | 職責 |
|---|---|---|---|
| ① | Unit Economics 重建 | Dan McCarthy / Peter Fader（CBCV）+ 精算 survival analysis | 核實公司披露原文措辭；重建收入/客戶/留存模型；sensitivity table 取代點估計 |
| ② | 行業營運模式 | 該行業最有公開披露嘅營運者（保險→Trupanion 10-K/Darryl Rawlings；電商→Shopify/Amazon 披露；SaaS→公開 SaaS metrics） | 用真實倖存者數據驗證「呢盤生意做唔做得掂」，推翻或確認結構性風險論 |
| ③ | 薪酬 + 市場數據核實 | 機構級來源：Michael Page / Morgan McKinley / Robert Walters 薪酬調查、政府統計處、監管機構（保監局/證監會/金管局） | 逐個數字溯源；aggregator 降級做旁證；矛盾數據調解出邊個口徑邊年 |
| ④ | 策略合成 | Alison Green（hiring-manager 視角）+ 上一輪外部 review 全部修正 | 行動排序 vs 職業質量排序分開；薪酬 script；盡職問題庫；十條唔好做 |

## 每個 Subagent Prompt 必須包含嘅鐵律

1. **每個數字要 URL**。搵唔到來源 → 標 `UNVERIFIED`，唔准填數。
2. **引句要盡量原文**；網站被封時註明「經搜尋索引摘錄，未能逐字對照」。
3. 輸出結構強制：`已核實事實（附 URL+引句）→ 分析 → 無法核實清單`。
4. 「你嘅 final message 就係交付物，唔好 meta-commentary。」

## 證據四級分級（所有輸出文件必用）

| 標記 | 意義 | 使用規則 |
|---|---|---|
| 【公開】 | 公司披露、政府統計、監管機構、可查證新聞 | 可直接引用，附 URL |
| 【基準】 | 第三方行業基準 / 薪酬 aggregator | 只做旁證；機構級調查 > aggregator |
| 【推導】 | 自己建構嘅模型假設 | 必須列假設清單；**模型做問題，唔做答案** —— 面試/決策時轉化成提問，唔當事實陳述 |
| 【評分】 | 主觀判斷 | 明確標示，歡迎推翻 |

## Locked Lessons（Codex 2026-07-31 捉到嘅錯，永久規則）

1. **分母口徑先於一切計算。** 「Total policies reached / 累計簽發 / total customers served」≠ in-force / active。分子分母唔同時間口徑嘅除法一律無效。收入要問清：GWP？已賺保費？扣分保後？含非核心收入？
2. **幾何壽命模型（1/(1-churn)）遇到任何披露 cohort 數據必須對數。** 例：90% 續保 → 10 年壽命，被公司自己「2020 cohort 4.5 年剩 52%」推翻。正確做法：分年 survival curve（首年懸崖 + 後期趨穩）+ 折現。
3. **薪酬用機構級調查（Michael Page / Morgan McKinley / Robert Walters），aggregator（PayScale/Glassdoor/Indeed/ERI）只做旁證。** Aggregator 之間同一職位可以差成倍。
4. **市場規模數字要用單一龍頭玩家收入做 sanity check。** 「市場 USD 8.5M」但單一公司收入已 USD 42M → 模板垃圾數，棄用。
5. **政府/施政報告引用嘅統計要查原始調查年份。** 2025 施政報告嗰組寵物數據原來係 2018 年調查。
6. **高管受訪講嘅滲透率/市佔係公司自述，唔係行業事實。** 引用必須註明身份。
7. **「X 會摧毀 Y」呢類結構性斷言要搵實證反例先出街。**（「加價必炸留存」被 Trupanion 加州 +29% 後留存連升四季推翻。）
8. **無來源嘅精確數字（例：6.57%/年）係最危險嘅一種** —— 精確度製造可信假象。寧願寫「約 5%（BLS）」都唔好寫一個查無出處嘅小數點。
9. **每次重建必須出 v1→v2 錯誤更正表**，放文件開頭 —— 唔好將舊錯誤靜靜刪走。
10. **交俾第二個 AI 審視嘅文件，必須帶證據分級 + 指定攻擊點問題清單**，否則對方只會覆述唔會挑戰。

## 合成規則（總指揮）

- 等齊 4 個 subagent 先合成；唔好用未返嘅 agent 嘅預期結果填空。
- 合成文件結構：`第 0 節 錯誤更正表 → 已核實事實 → 重建模型 → 策略 → 無法核實清單`。
- 所有交付物 commit 入 repo / vault，唔好只留喺對話。
