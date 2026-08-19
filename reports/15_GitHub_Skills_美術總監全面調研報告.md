# GitHub Skills 美術總監能力全面調研報告（v2）

> 項目：《覺得人哋好蠢》v4（16:9 talking-head）美術包裝線
> 調研日期：2026-08-19（所有星數、活躍度、授權均為當日經 GitHub API / 頁面核實）
> 對照資料：`13_美術總表_125x.md`、`14_GitHub_Skills_美術合成調研報告.md`、YouTube 參考片
> 狀態：只做調研與建議，**未安裝任何新 Skill**，等 Anson 決定

---

## 0. 結論先行（TL;DR）

1. **「YouTube FX Commander」喺 GitHub 上完全冇公開版本**。經全面搜索（GitHub repo / code search、skill 市集、中英文網絡），確認佢唔係一個公開 repo 或市集 skill；最大可能係參考片作者 Chuchu豬 TV 個 email-gated 指令包（【AI複製影片風格剪輯指令包】）入面嘅角色名，或者係你自己根據佢嘅 prompt 砌出嚟嘅本機 agent bundle。所以**冇得「安裝返個原裝 FX Commander」，只可以用公開 skill 疊出同等甚至更好嘅效果**。
2. **參考片本身唔係 coding agent 流程**。已核實逐字稿：條片教嘅係 Claude 網頁版寫風格指令 → Gemini Omni（Google Flow）或 Higgsfield AI **生成式重繪**成品，仲要因為廣東話配音口音問題（「譚仔口音」）要人手換返原聲。你而家行緊嘅「A-roll 不動 + 程式化 overlay 合成」路線，喺可控性、廣東話、品牌一致性上全部優於條片示範嘅方法 — 方向唔使改。
3. **能達到美術總監效果、而且信譽真正高嘅 skill，第一名依然係已安裝嘅 HyperFrames**（41,608★、Apache-2.0、調研當日仍有 commit）。今次新發現嘅高信譽補強選項有四個：`Vincentwei1021/video-shotcraft`（5.4K★ 鏡頭/動效/SFX 判斷庫）、`remotion-dev/skills`（4.3K★ 官方）、`op7418/Youtube-clipper-skill`（2.1K★，中文字幕燒錄）、`digitalsamba/claude-code-video-toolkit`（1.9K★，公司出品全家桶）。
4. **上一份報告（14）嘅首選 `LottieFiles/motion-design-skill` 維持建議**（1,037★、官方 vendor、MIT），佢仍然係唯一一個純粹教「美術判斷」而唔綁引擎嘅 vendor skill。
5. 市場有一個明確缺口：**冇任何一個 skill 同時做到「CJK 字幕」+「完整 overlay 設計系統」**。你現有嘅 `embedded-captions`（HyperFrames）+ 本機 `mc-*` 模板組合，其實已經係全網最接近填補呢個缺口嘅配置 — 呢個係「你的 stack 比市場先進」嘅信號，唔係缺陷。

**最終建議維持「少而精」：方案 A = LottieFiles motion-design-skill（美術判斷）+ 把 video-shotcraft 當參考庫抽規則，唔換主引擎。** 詳見第 9 節。

---

## 1. 「YouTube FX Commander」追查結果（重要澄清）

### 1.1 已核實嘅負面結果

| 搜索途徑 | 結果 |
|---|---|
| GitHub repo search `fx-commander` | 只有 3 個無關 repo（Clojure 玩具、Beef CLI、WW1 遊戲 mod） |
| GitHub code search `"FX Commander"`、`"美術總監" agent`、`"複製剪輯風格"` | 零相關命中 |
| Skill 市集（mcpmarket、claudemarketplaces、awesomeskill.ai 等） | 無此名 |
| 參考片完整 zh-HK 逐字稿 + 全部 20 條留言（經 API 抽取） | **完全冇提過 FX Commander、sub-agent 或 Claude Code** |
| 作者 GitHub（chuchucarmen / chuchuchutv） | 零公開 repo |

### 1.2 參考片真身（全部已核實）

- 頻道：**Chuchu豬 TV**（@chuchuchutv，香港廣東話 AI 教學頻道，主理人 Carmen Chu）
- 片名：《🔥唔想自己剪片? 1條參考短片👉AI幫你複製剪輯風格➡️自動剪!》，2026-08-14 出街，10:43，3,253 views
- 實際流程：**方法一** Claude 免費網頁版（Sonnet 5）分析 A-roll + 參考片 → 出風格指令文件 → 貼入 Google Flow 嘅 Gemini Omni（要 Google AI Pro，30 秒上限，每次生成約 10 秒）重繪 → 因廣東話口音問題剝走 AI 音軌、鋪返原聲；**方法二** Higgsfield AI Shorts Studio 用參考片砌 Preset 整條重繪，同樣換返原聲
- 配套資源全部係 email-gated lead magnet（`ai.edit.shorts.page.chuchucarmen.com`），冇 GitHub

### 1.3 對你嘅意義

「美術總監 sub-agent 要求嘅效果」實際規格唔係嚟自條片，而係你自己嘅 `13_美術總表_125x.md`（54 beats、品牌色、進出場、安全區）— 呢份嘢比條片嘅生成式重繪精細得多。所以本報告嘅評核基準直接用美術總表，唔用條片。

---

## 2. 評核基準：美術總監要求嘅效果

由 `13_美術總表_125x.md` 歸納為 8 項能力：

| # | 能力 | 具體內容 |
|---|---|---|
| R1 | 時間同步 overlay | title lockup、章節卡、glassCard、quote、對比雙卡、side panel、CTA，A-roll 不動 |
| R2 | 動作語法 | blur-settle、spring-pop、stamp-slam、wipe、fade-scale、draw-on 箭咀/刪除線 |
| R3 | 鏡頭語法 | punch-in 8–12%、reframe、Ken Burns、pan |
| R4 | 廣東話字幕 | 本地轉錄、重點詞、CJK 字型正確渲染 |
| R5 | 聲音層 | whoosh、stamp impact、BGM、ducking、loudness |
| R6 | 素材管理 | B-roll、icon、logo、字型、LUT、重用 ledger |
| R7 | 美術判斷 | 每拍點解要動／點樣動／幾時唔好動；timing、easing、層次、留白 |
| R8 | QC 迴路 | 抽幀自檢、接駁位驗證、可重複 render |

**信譽評級方法**：⭐ 星數 + 是否 vendor 官方 repo + 最近 push 日期 + 授權 + 市集安裝量／awesome list 收錄。星數截至 2026-08-19，經 GitHub API 核實；skills.sh 安裝量因網絡限制只能引自搜尋快照，下文標明「未直接核實」。

---

## 3. 第一梯隊：高信譽 + 直接對應（可安心考慮）

### 3.1 heygen-com/hyperframes — 主引擎，地位不變 ✅ 已安裝

- **41,608★ / 3,985 forks｜Apache-2.0｜2026-08-19 當日仍有 push（~3,928 commits）｜HeyGen 官方**
- skills.sh 顯示約 240 萬總安裝（未直接核實）
- **點解可以**：HTML-native「Write HTML. Render video.」— 你嘅 `remote-editor-kit 3/templates`（HTML/CSS/GSAP + `render.mjs`）可以零移植直接掛入；`talking-head-recut` 官方定義就係「clip plays untouched underneath」嘅時間同步 graphic cards（R1）；`hyperframes-keyframes` 明文支援 punch-in/zoom/reframe/pan/mask（R3）；`hyperframes-animation` 做 seek-safe 逐幀 GSAP/WAAPI（R2）；`embedded-captions` 有本地轉錄 + 人像 matte（R4）；`media-use` + `hyperframes-audio` 覆蓋 R5/R6。
- **⚠️ 本次核實到嘅變化**：skill 目錄現時 20 個，**`graphic-overlays` 已唔再係獨立 skill** — router 而家將 graphic-overlay 請求全部導向 `/talking-head-recut`；新增咗 `product-launch-video`、`faceless-explainer`、`pr-to-video`、`music-to-video`、`slideshow`、`remotion-to-hyperframes`、`figma` 等。**建議行一次 `npx hyperframes skills update` 同步本機版本**，否則你本機嘅 router 路由表同上游對唔上。
- **局限**：唔會自動提供美術判斷（R7 要另補）。

### 3.2 Vincentwei1021/video-shotcraft — 🆕 本次最大新發現（判斷庫）

- **5,400★｜Apache-2.0｜2026-08-14 有 push｜`npx skills add Vincentwei1021/video-shotcraft`**
- **點解可以**：呢個係全網最大嘅開源「鏡頭語感」庫 — **152 張 shot recipe 卡、209 個動作預覽、149 個 SFX（16 類）、BGM 拍點同步方法論、明文美學規則同 visual-QA 標準**。對應 R2/R3/R5/R7/R8：美術總監「呢一拍應該用邊種鏡頭/動作/音效」嘅判斷，可以直接引用佢嘅 recipe 卡做決策詞彙。
- **局限（重要）**：佢設計目標係**由零生成 cinematic 產品片**，唔係喺現有 A-roll 上疊 overlay；引擎係 Remotion。所以正確用法係**當佢係「判斷參考庫 + SFX 庫」抽規則**，唔好俾佢接管合成（合成留返俾 HyperFrames）。

### 3.3 remotion-dev/skills — 官方備用引擎（維持 14 號報告建議）

- **4,340★｜2026-08-18 有 push｜Remotion 官方｜12 個 skill**（best-practices / create / markup / studio / render / captions / multimedia / interactivity / maps / saas / docs / upgrade）
- skills.sh 顯示約 90 萬總安裝、`remotion-best-practices` 單獨約 48 萬（未直接核實）；2026 年 1 月上線時一週 25K 安裝，係 skills.sh 影片類第一
- **點解可以**：覆蓋文字動畫、spring/interpolate、轉場、**透明影片（alpha overlay）**、Lottie、3D、字幕、音效 — 即 HyperFrames 做唔到嘅例外元件（R1/R2 嘅 React/3D/particle 特例）。
- **⚠️ 授權（比 14 號報告要更小心）**：skills repo 本身**冇 LICENSE 檔**；佢驅動嘅 Remotion 框架行「Remotion License」— 個人、非牟利、**3 名員工以下**牟利機構免費，超出要買 Company License。以 @AIeasyjob 現時規模應該符合免費資格，但要你確認使用主體。
- **定位**：第二引擎，只喺 HyperFrames + 本機 kit 做唔到先用。

### 3.4 op7418/Youtube-clipper-skill — 🆕 中文字幕燒錄管線（信譽高）

- **2,100★｜MIT｜`npx skills add` 支援｜作者 op7418 即「歸藏」，中文 AI 圈頭部創作者**
- **點解可以**：唯一高星數、有**實證中文（雙語 zh/en）SRT + FFmpeg/libass 字幕燒錄**管線嘅 skill（R4），CJK 字型渲染係佢核心場景。
- **局限**：定位係「剪人哋條片做切片」，同你嘅原創 A-roll 流程唔同；得 2 個 commit。**建議唔安裝、只借鏡佢嘅 libass 燒錄參數** — 你已有 `embedded-captions` 做廣東話。

### 3.5 digitalsamba/claude-code-video-toolkit — 🆕 公司級全家桶（備選）

- **1,951★ / 328 forks｜MIT｜2026-08-19 當日有 push｜Digital Samba（歐洲視像會議公司）官方**
- **點解可以**：Remotion + MoviePy + FFmpeg + ElevenLabs + Playwright 一站式；有轉場庫（glitch、RGB split、zoom blur、light leak）、卡拉 OK 式燒錄字幕、SFX/音樂生成（ACE-Step）、同埋一個 frontend-design 判斷 skill（部分 R7）。
- **局限**：CJK 字幕未有文檔；部分管線假設用佢嘅 project template；AI 生成功能要 Modal/RunPod 帳號。**同你現有 stack 重疊度高，唔建議今次裝**，但係值得放入雷達 — 佢係增長最快嘅公司級競品。

### 3.6 LottieFiles/motion-design-skill — 美術判斷層首選（維持第一優先）

- **1,037★｜MIT｜LottieFiles 官方｜`npx skills add LottieFiles/motion-design-skill`**
- 最後 push 2026-05-18（3 個月前）— 但佢係**純文檔型判斷 skill**（4 個 commit：three pillars、Disney 12 原則、情緒→動作映射、choreography、entrance/exit patterns、timing/easing 表、quality checklist），冇 code 依賴，停更影響細
- **點解可以**：正正補 R7 — 將 `spring-pop` 分輕中重、判斷元件係「搶視線」定「做支撐」、為 B03 因果鏈／B15 三問／B26 三能力建立真 sequence、強調留白同節奏 — 即係直接修正你批評「一式一樣」嘅問題。Framework-agnostic（CSS/GSAP/Lottie 都適用），可以直接掛喺 HyperFrames 上面。
- **局限**：偏 UI motion 原則，唔識影片時間線 — 一定要同 HyperFrames 配合用。

### 3.7 browser-use/video-use — ⚠️ 已安裝，注意停更信號

- **21,063★｜MIT｜但最後 push 2026-07-01，之後 7 星期零活動，總共只有 18 commits**
- 星數高（browser-use 公司光環）但活躍度轉弱。你嘅用法（總裝嵌 + QC 層，唔重啟自動剪輯）唔受影響，照用；只係**唔好再加深對佢嘅依賴**，QC 職能長遠可考慮由 HyperFrames 生態接手。

---

## 4. 第二梯隊：能力啱、信譽中等（有條件考慮）

| Repo | ★ | 授權 | 能力對應 | 判斷 |
|---|---|---|---|---|
| `iart-ai/motion-skills` | 367 | MIT | 51 skills / 15 包：kinetic typography、data animation、YouTube & podcast 包；Remotion/GSAP/Manim/Three.js | 廣而不深；同 HyperFrames 路由衝突風險高，暫不裝 |
| `louisedesadeleer/clipify` | 534 | MIT | talking-head 追臉 reframe、三款 caption 風格 | 係二創切片工具，非美術層；不對題 |
| `av/remotion-bits` | 444 | MIT（README 聲稱；無 LICENSE 檔） | 現成 Remotion 元件（文字、粒子、3D）+ MCP | **2026-03-11 起停更 5 個月**；只在裝咗 Remotion 後、要例外元件先考慮 |
| `veedstudio/open-edit` | 289 | Apache-2.0 | VEED 官方；lower thirds、motion graphics、逐字 caption | **渲染器閉源行雲端**，輸出受 PolyForm Shield 約束 — 同你「全本地可控」原則衝突，不建議 |
| `AgriciDaniel/claude-shorts` | 186 | MIT | Remotion 動態字幕（Bold/Bounce/Clean）、AI 選段 | Shorts 場景、無 CJK；不對題 |
| `haidrrrry/claude-remotion-skill` | 58 | MIT | 「10 條鐵律」+ render→抽幀→修正迴路（R8 思路好） | 由零生成向；可借鏡佢嘅 QC 迴路條文 |
| `AbubakrChan/product-launch-motion` | 45 | MIT | HTML/GSAP 鏡頭語法 + SFX + loudness mastering | 由零生成 launch film；可借鏡音頻 mastering 條文 |
| `oil-oil/screen-studio-editor` | 29 | MIT | **CJK 混排字幕燒錄**、AAC 時間漂移處理 | ASR 用阿里 Bailian（普通話向，廣東話未證）；借鏡 CJK 排版處理即可 |
| `ytrofr/claude-remotion-editor` | 26 | MIT | 有獨立 `audio-mixing-and-ducking` SKILL.md | App demo 向；佢個 ducking skill 寫法可借鏡 |

---

## 5. 觀察名單：能力極貼但信譽太低（唔建議依賴，可讀源碼偷師）

呢批係「做緊同一件事但未有人用」嘅 repo — 價值在於**佢哋嘅 SKILL.md 條文可以抄入你自己嘅 skill**，而唔係安裝：

1. **`adriiita/vertical-video-editing-skill`（5★，MIT，2026-08-04 有 push）** — 全網同你需求最貼嘅單一 skill：HyperFrames HTML/GSAP 喺 talking-head 上疊 headline cards、name pills、highlight bars，eased zoom/pan，**合成 whoosh/click/riser SFX**，face-safe framing 規則，render verification gate。可惜作者無名、5 粒星、9:16 向。**最值得整份 SKILL.md 攞嚟讀**。⚠️ 注意有個 `nopefallacy/vertical-video-editing-skills`（43★）遲一日出現、內容幾乎相同，疑似搬運，出處不明，避開。
2. **`fernandokaraka/remotion-motion-graphics-skill`（7★，MIT）** — 專做**帶真 alpha 嘅 overlay 資產**（透明 ProRes / PNG 序列），「diagnose before decorating」判斷框架。如果日後 HyperFrames 某元件輸出唔到穩定 alpha，佢嘅做法係現成答案。
3. **`assafkip/claude-video-editor`（13★，MIT + Commons Clause）** — 將 video-use + HyperFrames 綑成一個 plugin。同你手動砌嘅架構撞樣，證明你嘅組合方向係社群共識；本身無新能力。
4. **`kingbootoshi/video-alchemy`（4★，MIT，單 commit）** — 剪輯決策用 JSON 表達而非 timeline、B-roll 疊層自動 mute 原聲，README 極詳盡；概念可借鏡。
5. **`BayramAnnakov/remotion-video-director`（40★，2026-03-13 一次性發佈後零活動，無 LICENSE 檔）** — Think→Design→Build→Review 四段創意流程。維持 14 號報告判斷：你已有美術總表，唔需要佢重開創意方向。

---

## 6. 唔建議安裝（本次覆核後降級／維持否決）

| Repo | ★ | 原因 |
|---|---|---|
| `soilmass/motion-design-agent` | **1** | 14 號報告列為「可考慮」，本次覆核**降級為否決**：2026-01-24 創建當日之後零活動、1 星 0 fork、README 聲稱 73 skills 但**連安裝方法都冇寫**。條文可讀，唔好裝。 |
| `zhengxn1/auto-cut-skill` | **1** | 單一 commit（2026-07-05）、Codex 手動安裝、與現有 stack 高度重疊。維持否決。 |
| `delaney939/remotion-motion-graphics-skill` | 0 | 能力描述極貼（talking-head overlay + 11 種 data-viz）但授權寫明「not for redistribution」— **直接失格**，只可當設計參考。 |
| `HKUDS/CLI-Anything` | 47,800 | 星數極高（港大 HKUDS 學術團隊）但佢嘅 `cli-anything-shotcut` 係驅動 Shotcut NLE，overlay/caption 細節無文檔；同你 pipeline 唔同範式。 |
| `video-db/skills` | 117 | 全部行 VideoDB 雲 API（要 key、計費）；違反本地優先原則。 |
| NLE 直控類（Jumper MCP、After Effects MCP 等） | — | unwire.hk 實測 Claude 直控 Adobe：改個尺寸 3 分鐘、3 條字幕 9 分鐘、video+BGM 直接失敗，結論「唔建議」。 |

另外核實：**Anthropic 官方 `anthropics/skills`（170K★）冇任何影片／motion 類 skill** — 即係官方冇「欽定答案」，社群 skill 係唯一選擇。

---

## 7. 需求 → Skill 對應矩陣（2026-08-19 更新版）

| 需求 | 首選（已裝） | 判斷補強 | 例外引擎 | 可偷師對象 |
|---|---|---|---|---|
| R1 overlay 卡片系統 | HyperFrames `talking-head-recut`（graphic-overlays 已併入） | — | Remotion 透明片 | adriiita、fernandokaraka |
| R2 動作語法 | `hyperframes-animation` | **LottieFiles motion-design** | remotion-bits 元件 | video-shotcraft 209 動作預覽 |
| R3 鏡頭語法 | `hyperframes-keyframes` | video-shotcraft 152 recipe 卡 | — | — |
| R4 廣東話字幕 | `embedded-captions` | — | — | op7418（libass 參數）、oil-oil（CJK 混排） |
| R5 SFX/BGM/ducking | `media-use` + `hyperframes-audio` | video-shotcraft 149 SFX + 拍點方法論 | — | ytrofr ducking skill、AbubakrChan mastering |
| R6 素材管理 | `media-use` | — | — | — |
| R7 美術判斷 | ❌ 現時缺口 | **LottieFiles motion-design（第一優先）** | — | video-shotcraft 美學規則 |
| R8 QC 迴路 | video-use（注意停更） | — | — | haidrrrry render→抽幀→修正條文 |

**市場缺口確認**：全網冇一個 skill 同時覆蓋 R4（CJK）+ R1（完整 overlay 設計系統）。你嘅「HyperFrames + embedded-captions + 本機 mc-* 模板 + 美術總表」組合已經係最接近嘅配置。

---

## 8. 社群實戰共識（佐證架構選擇）

2026 年中文 + 英文社群對「AI 剪片合成層」嘅收斂結論（多篇 Zhihu/53AI/Threads/實戰文交叉核實）：

> 分析（逐字稿/抽幀）→ FFmpeg 落剪 → **HyperFrames 或 Remotion 做花字/字幕/zoom 合成** → FFmpeg 合流

- HyperFrames 係中文教學圈增長最快嘅合成層推薦（aiposthub 有 zh-TW 專文）
- video-use 係中文圈聲量最大嘅剪輯層（Zhihu 兩篇高熱文），但上游開發已放緩
- Remotion 適合 React 熟手；直控 Adobe 全網劣評
- 你而家嘅架構同社群共識完全一致，唔使轉向

---

## 9. 安裝建議方案

### 方案 A — 最小、最適合今次（推薦，同 14 號報告一致，本次數據再驗證）

```bash
npx skills add LottieFiles/motion-design-skill
npx hyperframes skills update   # 同步 graphic-overlays→talking-head-recut 路由變化
```

唔新增引擎。另外用一次性動作把 `video-shotcraft` 嘅 recipe 卡／SFX 分類**抽錄成你自己嘅參考文檔**（clone 落暫存目錄讀，唔安裝），供美術總監 sub-agent 引用。

### 方案 B — 加備用元件引擎（未來多片種先考慮）

方案 A 之上：

```bash
npx skills add remotion-dev/skills
npx skills add av/remotion-bits --skill remotion-bits   # 注意已停更 5 個月
```

前提：確認 Remotion 授權主體（≤3 員工免費）。remotion-bits 停更風險自負，只做例外元件庫。

### 方案 C — 判斷庫全開（下一條片、想擴鏡頭語感先做）

方案 A/B 之上正式安裝 `Vincentwei1021/video-shotcraft`（5.4K★、Apache-2.0、活躍）。⚠️ 必須喺 CLAUDE.md 寫死路由：**佢只可以被查詢（recipe/SFX/美學規則），唔可以接管合成** — 否則佢會傾向由零生成 Remotion 產品片風格，撞爛你嘅品牌語法。

### 路由優先級（三個方案通用，寫死喺美術總監 agent 度）

1. 本機 `mc-*` 模板有相符元件 → 必須重用
2. HyperFrames 可完成 → HyperFrames
3. 都唔得 → Remotion（先搜 remotion-bits，冇先新寫）
4. 判斷問題查 LottieFiles motion-design + video-shotcraft 參考文檔
5. 一切新元件服從 `13_美術總表_125x.md` 嘅色彩/字型/安全區/進出場

---

## 10. 安裝前安全與品質檢查（維持 14 號報告清單，加兩條）

1. 先 clone 落暫存目錄，讀 `SKILL.md`、install script、`package.json` postinstall、外部 API 同環境變數，先至執行
2. 核對授權：Remotion 使用主體員工人數；remotion-bits / remotion-video-director **實際上冇 LICENSE 檔**，README 聲稱 MIT 唔等於有法律效力 — 商用前要留意
3. **新增**：避開搬運 repo（例：nopefallacy 版 vertical-video-editing-skills）— 裝 skill 一律用原作者 namespace
4. **新增**：`npx hyperframes skills update` 後 diff 一次本機 skill 目錄，確認冇引入你唔想要嘅新路由（例如 faceless-explainer 唔應該喺 talking-head 項目觸發）
5. 安裝後用 10–15 秒 sandbox composition 做 smoke test，唔直接拿正片測
6. 保留原片、舊 render、上一版 EDL；新輸出寫入版本化 `work/renders/`

---

## 11. 最終建議

**採用方案 A。** 三個研究方向嘅數據全部指向同一結論：

1. FX Commander 冇公開版可裝 — 佢嘅職能要靠「HyperFrames（手）+ LottieFiles motion-design（美術腦）+ 美術總表（劇本）」呢個組合實現，而呢個組合你已經有咗三分之二。
2. 高星新秀（video-shotcraft、digitalsamba）全部係「由零生成」範式，直接安裝會同你嘅「A-roll 不動」原則打架；正確用法係抽佢哋嘅判斷條文做參考庫。
3. 真正未補嘅只有 R7 美術判斷層 — 即係 LottieFiles motion-design-skill 一個 `npx skills add` 就填到嘅窿。

---

## 附錄：全部 24 個已核實 repo 一覽（截至 2026-08-19）

| Repo | ★ | 授權 | 最後活動 | 判定 |
|---|---|---|---|---|
| heygen-com/hyperframes | 41,608 | Apache-2.0 | 2026-08-19 | ✅ 主引擎（已裝，要 update） |
| HKUDS/CLI-Anything | 47,800 | Apache-2.0 | 活躍 | ❌ 唔同範式 |
| browser-use/video-use | 21,063 | MIT | 2026-07-01 ⚠️ | ✅ 已裝，凍結依賴 |
| Vincentwei1021/video-shotcraft | 5,400 | Apache-2.0 | 2026-08-14 | 🟡 方案 C／參考庫 |
| remotion-dev/skills | 4,340 | 無 LICENSE（框架行 Remotion License） | 2026-08-18 | 🟡 方案 B 備用引擎 |
| op7418/Youtube-clipper-skill | 2,100 | MIT | — | 📖 借鏡 CJK 燒錄 |
| digitalsamba/claude-code-video-toolkit | 1,951 | MIT | 2026-08-19 | 🟡 雷達觀察 |
| LottieFiles/motion-design-skill | 1,037 | MIT | 2026-05-18 | ✅ **方案 A 安裝** |
| louisedesadeleer/clipify | 534 | MIT | 活躍 | ❌ 不對題 |
| av/remotion-bits | 444 | MIT（無 LICENSE 檔） | 2026-03-11 ⚠️ | 🟡 方案 B 有條件 |
| iart-ai/motion-skills | 367 | MIT | 活躍 | ❌ 路由衝突風險 |
| veedstudio/open-edit | 289 | Apache-2.0 | 活躍 | ❌ 雲端閉源渲染 |
| AgriciDaniel/claude-shorts | 186 | MIT | — | ❌ 不對題 |
| video-db/skills | 117 | MIT | — | ❌ 雲 API 計費 |
| wilwaldon/Claude-Code-Video-Toolkit | 73 | MIT | 2026-02 | 📖 索引參考 |
| haidrrrry/claude-remotion-skill | 58 | MIT | 2026-08-12 | 📖 借鏡 QC 迴路 |
| AbubakrChan/product-launch-motion | 45 | MIT | — | 📖 借鏡 mastering |
| BayramAnnakov/remotion-video-director | 40 | 無 LICENSE 檔 | 2026-03-13 ⚠️ | ❌ 維持否決 |
| oil-oil/screen-studio-editor | 29 | MIT | 2026-08 | 📖 借鏡 CJK 混排 |
| ytrofr/claude-remotion-editor | 26 | MIT | — | 📖 借鏡 ducking |
| assafkip/claude-video-editor | 13 | MIT+Commons Clause | 活躍 | 📖 架構印證 |
| fernandokaraka/remotion-motion-graphics-skill | 7 | MIT | 2026-07-17 | 📖 借鏡 alpha overlay |
| adriiita/vertical-video-editing-skill | 5 | MIT | 2026-08-04 | 📖 **最值得通讀** |
| soilmass/motion-design-agent | 1 | MIT | 2026-01-24 ⚠️ | ❌ 降級否決 |
| zhengxn1/auto-cut-skill | 1 | MIT | 2026-07-05 ⚠️ | ❌ 維持否決 |

### 主要來源

- [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)｜[skills 目錄](https://github.com/heygen-com/hyperframes/tree/main/skills)｜[router SKILL.md](https://raw.githubusercontent.com/heygen-com/hyperframes/main/skills/hyperframes/SKILL.md)
- [browser-use/video-use](https://github.com/browser-use/video-use)
- [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)
- [remotion-dev/skills](https://github.com/remotion-dev/skills)｜[Remotion LICENSE](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft)
- [op7418/Youtube-clipper-skill](https://github.com/op7418/Youtube-clipper-skill)
- [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit)
- [adriiita/vertical-video-editing-skill](https://github.com/adriiita/vertical-video-editing-skill)
- [fernandokaraka/remotion-motion-graphics-skill](https://github.com/fernandokaraka/remotion-motion-graphics-skill)
- [av/remotion-bits](https://github.com/av/remotion-bits)｜[soilmass/motion-design-agent](https://github.com/soilmass/motion-design-agent)｜[BayramAnnakov/remotion-video-director](https://github.com/BayramAnnakov/remotion-video-director)｜[zhengxn1/auto-cut-skill](https://github.com/zhengxn1/auto-cut-skill)
- [anthropics/skills](https://github.com/anthropics/skills)（無影片類 skill）
- 參考片：[Chuchu豬 TV — 1條參考短片 AI 複製剪輯風格](https://www.youtube.com/watch?v=c_paNzLEiYI)（逐字稿經 API 核實）
- 社群實戰：[aiposthub zh-TW HyperFrames 指南](https://www.aiposthub.com/claude-code-hyperframes-video-editing-guide/)、Zhihu video-use 兩篇高熱文、[unwire.hk Claude 直控 Adobe 實測](https://www.threads.com/@unwirehk/video/DYCug0vCMTQ/)

> 註：skills.sh 安裝量數字（hyperframes ~240 萬、remotion ~90 萬）因網絡限制引自搜尋快照，未直接核實；其餘星數、日期、授權全部經 GitHub API 當日核實。
