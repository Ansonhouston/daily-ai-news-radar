# video-shotcraft 判斷詞彙抽錄（美術總監查閱版）

## 0. 頭部說明

- **來源 repo**：`Vincentwei1021/video-shotcraft`（GitHub），commit `0d6f0b57f0d4d6700761644c07f7ef03c3e50234`
- **授權**：Apache-2.0（repo 本體）；音效檔另有 Mixkit 授權細節，見第 5 節
- **抽錄日期**：2026-08-19
- **本檔引用路徑**：全部相對於 repo root（例：`references/shots/effects/slam-entrance-moves.md`）
- **使用原則（鐵律）**：
  1. 呢份嘢係**判斷參考**——借佢嘅 timing / easing / 節奏 / 已知坑判例嚟做美術決策，**唔係**攞嚟接管合成。
  2. 合成一律行 **HyperFrames + 本機 mc-\* 模板**（HTML/CSS/GSAP overlay 疊喺 16:9 A-roll 上面）。video-shotcraft 嘅原生引擎係 Remotion、原生場景係 from-scratch 產品 promo——我哋唔跑佢個 engine、唔 copy 佢啲 TSX。
  3. 卡入面嘅幀數以 **30fps** 為基準（1f ≈ 33ms）。轉做 GSAP 時換算：`秒 = f / 30`（例：18f ≈ 0.6s）。
  4. 所有參數都係佢哋喺灰階 demo 或模板片實戰調校出嚟嘅**起點**，唔係定稿——落地到我哋嘅 overlay 之後照樣要 render 出嚟自己睇（對應佢哋 P1 規則）。
  5. 佢哋成套判例係「全畫面產品片」語境；我哋係 overlay-on-A-roll，人面永遠喺畫面度——**能量上限自動降一檔**（佢哋話全片砸入 ≤2 次，我哋一條片 ≤1 次已經好響）。

---

## 1. 精選 recipe 卡（43 張，按美術總表詞彙分系）

> 每張卡格式：卡名（路徑）→ 點解好用 → 關鍵參數（卡內實數）→ 對應美術總表場景。
> 「命門」= 卡內標明唔可以降檔嘅參數。

### 1.1 stamp-slam 系（盖章 / 砸入 / 重拳強調）

**slam-entrance-moves** `references/shots/effects/slam-entrance-moves.md`
- 點解好用：入場力度嘅天花板，三式選型好清晰——A「佢嚟啦」（透視甩入）、B「佢好重」（砸落）、C「震到全場」（波及鄰卡）。啱晒 stamp-slam 落章嗰下嘅手感字典。
- 關鍵參數：A 甩入 18f `Easing.out(cubic)` + 末 4f 過衝 +5° 彈平 + 6px 震屏 2f；B 砸落 **6f `Easing.in(quad)`（加速砸，唔係減速落——ease-out 係「放低」，ease-in 先係「砸」）**；B 三件套：圓環 80→860px/14f + 塵點飛 160–320px + 震屏 18px 指數衰減 4f；收尾真靜止 ≥45f（重拳 hold 雙倍）。
- 命門：環/塵「擴散用 out-cubic、消散用 linear」要解耦；一個鏡頭只可以有一個震源；砸入必須同幀釘 SFX，無聲會讀作「卡緊度抽搐」。
- 對應：stamp 強調、B01 title lockup 落章、KPI 數字卡登場。

**impact-feedback** `references/shots/effects/impact-feedback.md`
- 點解好用：管「落位嗰一瞬」——element 到位但冇「砸到咗」嘅反饋就係 PPT 飛入。B 式連招計數（頓幀+傷害數字+combo 跳字）啱三點 checklist 連打。
- 關鍵參數：B 三卡各隔 30f、命中前 10f ease-in(quad) 砸落、每命中**全局凍結 2f**；傷害數字 scale 1.4→1 + 上浮 40–60px + 12f 漸隱；計數器脈衝逐次加碼 1.3/1.45/1.6 + rotate −2/−4/−6°（三次一樣大就讀唔出「越打越狠」）。C 式打擊幀：撞停起 **3f** `invert(1) grayscale(1)` + 集中線 + 紅青色散，第 4f 全撤（4f 起觀眾開始睇清負片，魔術穿崩）。
- 命門：B 頓幀必須全局（背景都要凍埋）；C 全片限高潮一次 + 必須同幀 impact 音。
- 對應：三點 checklist 逐項入場加 punch、全片唯一高潮嗰一下。

**cel-flash-stomp** `references/shots/typography/cel-flash-stomp.md`
- 點解好用：「主體穩、背景閃」——同震屏完全相反嘅路線，打擊感來自周邊視野。三連詞口號（動漫必殺技字卡）嘅 UI 翻譯。
- 關鍵參數：每詞 ~30f 硬切零 crossfade；入場 6f scale 1.18→0.98→1（`Easing.out(poly(5))` 2% 過衝）+ rotate 交替 ±2.5°（歪角係「圖章」嘅一半）；落定幀起**背景兩色每 2f 交替共 6f**、文字獨立上層紋絲不動；末詞閃 8f 加倍 + 標籤條 14f 淡入；收尾 ≥45f。
- 命門：底閃層唔可以有任何內容元素（閃嘅必須係「空氣」）；每詞砸落要一聲 kick 對拍；全片 ≤1 段。
- 對應：stamp 三連（「快・靚・正」式口號卡）、高能 chapter card。

**brand-frame-snap** `references/shots/effects/brand-frame-snap.md`
- 點解好用：用一圈粗色框做「章節/模式」語義編碼，翻色一幀硬切就係視覺換擋聲。啱做全片 overlay 包裝層或者章節顏色系統。
- 關鍵參數：框厚 44px@1080p、生長 18f ease-out **先於內容 14f**；翻色帧三件事同幀（框色 + 佈局 + 角標文字），錯開 2f 就散；白閃脈衝 2–3f 0.55→0.19；框厚阻尼彈跳 `exp(-0.22t)·cos(0.9t)·10px`；翻色前落定要坐穩 ≥30f。全片翻色 ≤2 次。
- 對應：chapter cards 顏色編碼、雙主題對比章節。

### 1.2 spring-pop 系（彈入 / 逐項入場 / 卡片堆疊）

**list-reveal** `references/shots/ui-entrance/list-reveal.md`
- 點解好用：逐項入場唔死板嘅標準答案——「逐項搵位」+「整體呼吸」兩層解耦，畫面冇一幀係釘死。低能量默認卡。
- 關鍵參數：stagger **0.09/項（≈10f，「讀得完」嘅間隔）**；單項行程 ≈26f（行程係 stagger 嘅 2.6 倍→相鄰三項同時郁，隊列連綿）；scale 0.78→1 + translateY 14→0 + `E.outBack` 軟過衝；透明度 `min(1, p*2.2)`（45% 行程已全實）；容器全程 linear 漂移 32px。
- 對應：三點 checklist 逐項入場（spring-pop light）、side panel 選單。

**card-stack** `references/shots/ui-entrance/card-stack.md`
- 點解好用：「先俾整體再俾個體」——8 張卡先疊成一嚿（數量感）再一次過展成扇面（多樣性），順序係命門。
- 關鍵參數：入場 stagger 0.033/張（≈4f「一串」手感；≥8f 變逐張點名）、y 300→0、`E.spring(0.3)` 一次回彈；展開窗 0.55→0.8 inOutCubic；扇形每張 rot `k*8°` + 橫移 `k*34px` + `transform-origin: 50% 130%`（扇柄喺手，唔係風車）。
- 對應：comparison 多卡建立鏡、模板/選項一覽。

**list-stack-press** `references/shots/ui-entrance/list-stack-press.md`
- 點解好用：「堆疊有重量」——每張新卡落嚟成疊被壓低 6px 再彈返，觀眾由物理反饋讀出「實打實儲落嚟」。計數器同步跳格釘死數量感。
- 關鍵參數：節拍 CUES 12f 等距、每張飛 22f `bezier(0.45,0.05,0.25,1.12)` 末端過衝；壓感脈衝 [cue,cue+4,cue+8]→[0,6,0]；陰影空中 `0 32px 64px`→落定 `0 2px 8px`；高亮條滯後落地 2–4f 先長出（次級動作唔同幀搶戲）；DigitRoll 每位 delay i·4、22f 滾定、**必須 tabular-nums**。
- 命門：堆疊/列表信息鏡必須正視機位（佢哋 Q6 判例：全片斜化被回滾）。
- 對應：checklist 累積、成績/清單逐項疊、數字聯動。

**deck-deal-flyin** `references/shots/ui-entrance/deck-deal-flyin.md`
- 點解好用：「大量嘢湧入」嘅最高判例密度卡——加速度先係速度感（R2），群體運動要揸住物理隱喻（發牌）先收斂。
- 關鍵參數：出牌間隔 `4k − 0.0792·k(k−1)`，由 4f 硬加速收縮到 0.2f；單卡 deal 8f `bezier(0.3,0,0.2,1)` + settle 4f `bezier(0.3,0,0.25,1.15)` 輕過衝 + press 0.996→1 回彈 2f（快停配足緩衝 ≈ 飛行 30%）；預備拍幅度判例：4px 完全無感、**放大 12 倍（48/30px）先過**；滿板後靜止 0.5s 係用戶逐字要求。
- 對應：多項素材湧入、B-roll 卡牆建立；「預備拍要過肉眼閾值」係通用判例。

**element-body-moves** `references/shots/ui-entrance/element-body-moves.md`
- 點解好用：補「身體在變」——A 拉絲（squash & stretch 嘅 UI 翻譯）俾速度一個肉身；B 接觸陰影（卡浮起、影留喺枱面）係 2.5D 懸浮嘅物理台詞。
- 關鍵參數：A 速度差分驅動，v∈[2,140]px/f 映射拉伸 0→滿（scaleX 2.2/scaleY 0.72），落點 8f 回彈；B 抬起 10f out-cubic：卡 −28px + scale 1.08、獨立橢圓陰影 scale 1→1.72 / opacity 0.55→0.18 反向；**判例鎖死：抬升 <12px 禁用（8px 實測完全無感）**；B 一次只抬一張。
- 對應：glassCard 點名浮起、spring-pop heavy 落地質感。

**hashtag-to-pill-materialize** `references/shots/interaction/hashtag-to-pill-materialize.md`
- 點解好用：「兩次硬切夾一次滑動」節奏骨架——文字變實體用 **1 幀硬切**（原片實測無任何過渡），確定感全靠硬切，任何漸變都會軟化成「特效」。
- 關鍵參數：打字 4–6f/字、紅實心光標**恆亮唔閃**；硬切後僅 3f 1.03→1 微落定；膠囊 hold ~18f（0.6s）；縮移 ~0.55x、14f、`bezier(0.5,0,0.25,1)` 位置縮放同曲線；落位 +3f 再 1 幀硬切揭示。
- 對應：tag/keyword pill 入場、字幕詞升級做 UI 元素。

**skeleton-reveal** `references/shots/ui-entrance/skeleton-reveal.md`
- 點解好用：「草稿→骨架→內容」三級保真度躍遷，借 skeleton screen 嘅日常語法免費攞到觀眾預期。
- 關鍵參數：塗鴉煮沸每 5f 換 seed、抖幅 ±6–10px；換真一拍 8f 加速縮退 + spring(damping 16, stiffness 160) 彈入；顯影每行錯峰 13f、行內 12f；逐詞 2.5f 步進上浮 14px；**末詞 +14f 晚半拍**做收尾頓點。
- 對應：side panel / 圖表「由諗法變成品」嘅登場敘事。

### 1.3 blur/settle 系（虛焦浮現 / 柔性落定）

**blur-slide** `references/shots/typography/blur-slide.md`
- 點解好用：文字 reveal 嘅**默認解**、我哋 blur-settle 嘅直系參數源。專業感全在一件事：y / blur / opacity 三通道**共用同一條 progress 同一條 easing**——「由虛焦浮出嚟」而唔係「滑入順便淡一下」。
- 關鍵參數：詞間 stagger 主標題 ≈3.5f / 副標題 ≈2.5f（3–4f 係「逐詞」甜點）；單詞入場窗 ≈20f `outCubic`；y 位移主 40px / 副 26px（**層級差靠幅度唔靠時長**）；blur `(1-p)·10px`；主副錯峰重疊 32f（排隊會讀成兩拍）；收尾靜置 ≥8f。
- 命門：三通道分開寫三條 easing（就算曲線一樣）都會「位移到咗但仲矇」；中文要手動按語義切 3–5 個 span，唔好退化成逐字。
- 對應：blur-settle 標題、quote card 主副行、旁白字卡默認入場。

**type-entrance-moves** `references/shots/typography/type-entrance-moves.md`
- 點解好用：標題入場另外兩種性格——A 乱碼解碼（技術自信）、B 字符墜落彈跳（輕鬆破冰）。同片標題入場手法 ≤2 種。
- 關鍵參數：A 亂碼期每 2f 跳字、解碼 6f/字（下限；上限 10f）、鎖定前 2f 反色閃；B 墜落重力 `(t/24)²`、彈跳衰減 30%→9%（三跳以上讀作果凍）、落地歪斜 ±6°、全員齊整歸位 6f ease-out。
- 對應：B01 title lockup 嘅高能變體、tech 主題 chapter card。

**vertical-word-roll-blur-cycle** `references/shots/typography/vertical-word-roll-blur-cycle.md`
- 點解好用：句尾換詞用滾輪唔用淡入淡出——滾輪自帶方向（「仲有下一個」）。相鄰行垂直 blur（滾筒景深）+ 落定瞬間染色（灰→強調色，「呢個先係答案」）係兩個身份記號。
- 關鍵參數：3 次換詞各 ≈16f（0.55s），段間靜置 ≈13f 俾人讀詞；easing 配方 `0.7·outQuint + 0.3·outBack`（機械減速 + 落定微過衝）；行高 44px、mask 露 3 行（露 1 行就讀作淡入淡出）；染色映射 `1 − 2.4d`（只喺落定瞬間上色）。
- 對應：「AI 幫你 ___」句式列舉、標題句尾動態詞。

**paper-title-card** `references/shots/typography/paper-title-card.md`
- 點解好用：呼吸位字卡定式——逐詞壓印（letterpress）+ 一句恰好一個 accent 詞 + 下劃線收束。佢哋成個模板片 4 張字卡全部同一節奏。
- 關鍵參數：第 i 詞 delay 4+i·4、9f `bezier(0.2,0.75,0.3,1)`、scale 1.28→1 + blur 7px→0；下劃線 16→34f scaleX 0→1；**全片字卡統一 50–55f（≈1.8s）**——觀眾讀完一句話嘅時間；重點詞 = 功能名/收益詞（兩個 accent 等於冇 accent）。
- 對應：chapter card、quote card、重要功能出場前嘅引導字卡。

### 1.4 wipe/transition 系（擦除 / 換章 / 藏切）

**wipe-transitions** `references/shots/transition/wipe-transitions.md`
- 點解好用：幾何擦除兩式（時鐘掃 / 百葉窗），唔依賴構圖有合適元素，邊度都用得。命門判例好值錢：**擦除邊界必須帶亮線/高光，冇亮線嘅 wipe 讀作 PPT 轉場**。
- 關鍵參數：A 時鐘掃 30–90f 純 linear（加 easing 就唔係雷達係鐘擺）；B 百葉窗 12 條、delay = 列號×2f、每條 10f `Easing.in(cubic)`；亮線多層配方（白柔光 + 黑描邊 + 白核——白底靠黑描邊、深底靠白核）；擦完**摘罩**（opacity 0 唔算摘）；幾何擦除全片 ≤2 次。
- 對應：wipe 轉場基本盤、資料刷新/翻頁語義。

**color-block-step-wipe** `references/shots/transition/color-block-step-wipe.md`
- 點解好用：全程**零插值零 easing** 嘅階躍色塊吞屏——3–5 聲「咔、咔、咔」比一次平滑掃過更有宣告感，頓挫本身就係節奏。
- 關鍵參數：A 4–5 跳（w 0→280→820→1340→1920 @ 8f 間隔）；B 3 跳；跳位間隔 6–12f **不等距**（等距讀作 GIF 掉幀）；徽章過衝都用階躍 0→0.55→1.12→1 三跳（同一語法貫穿到底，用 spring 就似「另一部片」）；鋪滿後 hold ≥30f。每跳一聲打點，無聲讀作播放器窒。
- 對應：品牌色 wipe、章節交接、high-energy 段 stamp 前奏。

**bottom-push-stack-wipe** `references/shots/transition/bottom-push-stack-wipe.md`
- 點解好用：「新章頂走舊章」嘅刚性換章——連底色整屏走，觀眾讀到「換咗個世界」。連推幾章 + 飽和底色，換章本身就係全片節拍器。
- 關鍵參數：推入 30f 重 ease-out `cubic-bezier(0.12,0.9,0.2,1)`（快進慢停「哐」一聲）；兩屏位移嚴格同步同 easing；上緣 40px 接縫陰影（黑 0.30 漸變）係物理接觸嘅證據；章間 hold ≈37f；連推 2–4 章、方向全片統一。
- 對應：chapter cards 換章骨架、多賣點分段。

**circle-match-iris** `references/shots/transition/circle-match-iris.md`
- 點解好用：iris 光圈 + match-cut 焊死——光圈由前景真圓元素嘅圓心炸開、圈內新景個圓接喺同一個圓上，「頭像個圓變咗做圖表個圓」，形狀自己講故事。
- 關鍵參數：開圈前錨點 2 次 scale 1→1.15 脈衝定睛（30f）；光圈 22→2100px / 45f `Easing.inOut(cubic)`；**接圓發生喺擴張中途（~40%）**，開晒圈先畫圖 = 匹配感歸零；圓心偏移 >10px 一眼穿崩。
- 對應：頭像→數據、icon→指標嘅語義轉場。

**white-flash-logo-simplify-cut** `references/shots/transition/white-flash-logo-simplify-cut.md`
- 點解好用：一次閃白完成「質感降維」——華麗液態渐變字標 → 冲白過曝 → 白底扁平字標定格。「演出結束，呢個先係正式形象」。
- 關鍵參數：冲白窗 t 0.34–0.42 `inQuad` 加速冲入（**快進慢不退**，白層冲入後保持）；過曝脈衝 blur 5px + brightness ×2.2 sin 包絡；扁平字標 0.48–0.74 淡入 + scale 0.96→1，同冲白之間留 0.06 白屏靜默做呼吸位；扁平版比液態版細一號（62→58px）暗示落定。冲白必配 SFX，無聲讀作跌幀。
- 對應：outro 品牌定妝、CTA 前嘅淨化拍。

**transition-hidden-cut** `references/shots/transition/transition-hidden-cut.md`
- 點解好用：藏切三式（前景遮擋 / 對撞開屏 / 暖色漏光）——硬切藏喺障眼物嘅 1–3 幀入面，觀眾「見唔到把剪刀」。
- 關鍵參數：A 超畫幅卡橫掃 14f `bezier(0.3,0,0.7,1)`、切點喺全遮幀；背景「帶風推擠」±40px（切前拖向掃掠方向、切後 13f 回穩）係無痕感一半功勞；B 對撞 10f ease-in(cubic) + 撞擊幀白閃 3f + shake 12px·e^(−t/1.6)（三件必須同幀）；C 漏光 ease-in 爬升 27f→峰值藏切→ease-out 收斂 43f，峰值時頁面 contrast −45% / brightness +35%（「燒穿」感）。一個接縫只用一式。
- 對應：A-roll 章節間嘅無痕跳切、before/after 開屏。

**shot-transitions** `references/shots/transition/shot-transitions.md`
- 點解好用：接縫選型總表（六式：flash-cut / 穿暗場 / 虛焦接力 / 黑場字卡 / whip-pan / 穿窗）——「接縫裸切會將逐鏡儲落嘅電影感一次漏晒」。分鏡階段逐接縫標注，轉場幀由相鄰鏡頭預算劃走。
- 關鍵參數：flash-cut 切點 ±5f 白閃；whip-pan 甩動 8f 跨 ~1.5 屏、峰值速度 ≥300px/f 先糊得透；whip 急刹款前 70% 路程用 30% 時間 + ease-out 長尾 ~48f；虛焦接力前景 blur 0→8px 同時後景 8→0、交叉窗 10–16f、兩景錯開 2–4f 起跑；穿窗 45f 單段 bezier、窗內新景由 ~0.42 反向補償。
- 對應：所有 overlay 段落之間點樣交棒嘅 decision table。

### 1.5 draw-on/annotate 系（描畫 / 圈重點 / 掃描標注）

**draw-svg-trace** `references/shots/ui-entrance/draw-svg-trace.md`
- 點解好用：「畫出嚟」入場——條線帶筆頭沿輪廓走一圈，閉合瞬間閃黑交棒、內容先淡入。第二用法係標題下劃線 18f 短版。
- 關鍵參數：`pathLength={1}` + dashoffset 1→0、40f `Easing.inOut(cubic)`（<28f 讀唔出「畫緊」、>60f 讀作 loading）；**筆頭**係命門：同路徑疊一層更粗（4→7px）嘅短 dash（0.045）行喺最前——冇筆頭只係「邊框變長」；閉合閃 2f 冲黑加粗 + 6f 回落；下劃線版 18f out cubic、一屏 ≥2 條就讀作裝飾線。
- 對應：draw-on 箭咀/圈注/下劃線嘅參數基準、元素點名。

**marker-underline-title** `references/shots/typography/marker-underline-title.md`
- 點解好用：手繪 marker 下劃線嘅三命門：**快**（8–12f 一筆過，慢咗係 loading bar）、**近**（貼字底，遠咗係分隔線）、**跟字勢**（斜體詞左低右高——畫反咗係最易犯最一眼假嘅錯，有返工判例）。
- 關鍵參數：劃線 10f（14f 版被裁「偏慢」）；字底距離 ≈ −0.1em；筆寬中段 ~0.12em、首尾 ~0.6x（等寬讀作機器線）；時機 = 標題落定 +4~8f 先起筆（同動就搶戲）。
- 對應：draw-on 強調（marker highlight / strikethrough 同一族）。

**scanline-annotate-focus** `references/shots/effects/scanline-annotate-focus.md`
- 點解好用：「AI 睇緊你嘅畫面」嘅因果鏈拍法——掃描線行到邊、邊度就被框住被命名。**先掃到再彈框**，次序一亂就變咗預先編排。
- 關鍵參數：掃描線**匀速零 easing**；觸發時刻由目標 bbox 反算（掃過 bbox 下緣嗰刻）、最小間隔 0.05 防兩框齊彈；取景框 4 個 9px L 角、`outBack` scale **1.75→1**（1.2 倍睇唔出「對準」動作）；對焦閃 fill 峰值 0.07（>0.15 變「選中高亮」）；標注滯後框 +0.05（「框穩咗先命名」）；計數行實時數 00/06→06/06。
- 對應：screenshot 分析 overlay、重點區域逐個點名。

**scan-bracket-sweep** `references/shots/effects/scan-bracket-sweep.md`
- 點解好用：「份嘢畀機器逐行讀緊」——四角 L 括號框住目標 + 光帶往復掃 5 趟。命門：**文檔本身完全靜止**，一郁就分唔清係「被檢查」定「載入中」。
- 關鍵參數：括號臂長 34px、stagger 0.022 依次落位（同時出現讀作靜態邊框）；扫 5 趟 linear 切段、趟內 `inOutSine` + 末尾 12% 完全停頓（換氣位）；光帶 2.5px 實線 + 82px 拖尾、方向翻轉時拖尾同 gradient 要一齊反；光帶裁喺同圓角嘅 overflow:hidden 內。
- 對應：文件/截圖「分析中」狀態、上傳→解析中段。

**outline-word-fill** `references/shots/typography/outline-word-fill.md`
- 點解好用：一個詞打成「釘」靠**兩次落定**：空心字 3.2 倍急縮到位（尺寸落定）+ 描邊 0.6 幀內瞬間變實心白（質感落定）。中間虛線圓收縮係「瞄準」。
- 關鍵參數：收縮窗僅 10f outCubic、scale 3.2→1；虛線圓 45f 慢收（全片最慢曲線，同 10f 急縮做快慢對比）+ 自轉 t·18°；**瞬時填充窗 0.02（≈0.6f）**——任何 >3f 嘅慢掃都會降級做美化動畫；輝光峰值 16px、7f 衰完；描邊預熱灰度 86→145。深底專用；點亮幀必須配一記短促重音。
- 對應：卡點上嘅單詞「釘」、賣點詞 beat drop。

**speed-ramp-freeze** `references/shots/rhythm/speed-ramp-freeze.md`
- 點解好用：幀號 remap 兩式——變速（快→0.2x 凝視→快）同定格圈注（停低嚟劃重點）。教學語境嘅 draw-on + 節奏合體。
- 關鍵參數：快慢斜率反差 **≥10 倍**先可感；慢窗 ≥40f / 定格段 ≥45f（R3 寧慢勿快）；定格瞬時切換無緩入；圈注 marker SVG 橢圓 8f 描邊 + 箭咀 6f + `feTurbulence scale≈7` 手繪抖動；解凍段斜率 >1 補時長。快段先糊、慢窗清——「快糊慢清」反差係手法成立嘅一半。
- 對應：punch-in 後定格圈重點、教學 highlight 拍。

### 1.6 camera/punch-in 系（推鏡 / 景深 / 聚光）

**crash-zoom-punch** `references/shots/camera/crash-zoom-punch.md`
- 點解好用：「睇呢度！」嘅一拍急推。慢推係「請看」，急推係命令式。落位二選一：過衝回彈（彈性）or 撞停震屏（重量）。
- 關鍵參數：急推 **6f ease-in**（>10f 就變普通推近）、zoom 1→2.4–2.8（目標佔畫面 60–75%）；回彈款過衝後 5f 回收 3–6%；撞停款震屏 14px·e^(−t/1.8)、6f 收乾；前 hold ≥30f 建立全景、後 hold ≥45f 讀特寫。一支片急推 ≤2 次；兩款唔好溝埋用。
- 對應：punch-in 8–12% 嘅「加辣版」判斷基準（我哋日常 punch-in 幅度細好多，但 easing 方向、hold 預算同源）。

**depth-layer-moves** `references/shots/camera/depth-layer-moves.md`
- 點解好用：平面截圖「有厚度」嘅兩款——3 層視差滑軌（Ken Burns 升級版）同偽 dolly-zoom（主體釘死、世界壓埋嚟）。
- 關鍵參數：視差三層係數 **0.35 / 0.7 / 1.4**（層間梯度 ≥2 倍先分得出）；背景層 +blur 2px + 降飽和 0.92、前景浮塊 +blur 3px（冇 blur/飽和錨就讀作「貼片亂飛」）；dolly-zoom 背景 scale 1→2.0–2.5 由中心膨脹 + blur 0→3.5px、主體落影 12→28px 加深。dolly-zoom 一支片 ≤1 次。
- 對應：Ken Burns / reframe 嘅質感升級、B-roll 靜圖動態化。

**spotlight-hero-card** `references/shots/opening/spotlight-hero-card.md`
- 點解好用：「單一主角」開場範本——聚光引導視線 → 斜側推進 → 卡彈起懸浮 → 輪廓光兩圈 → 貼返原位。開場多卡群舞撐唔起第一印象（Q5 判例：推倒六次先收斂到單卡）。
- 關鍵參數：動作弧 rise 10f `bezier(0.2,1.25,0.3,1)` 過衝 → 懸停 54f（sin bob 振幅 4px 周期 40f）→ reseat 18f + press 0.997；鎖定→落地 ≈98f≈3.3s（質感鏡要放慢到 3 秒，R3）；聚光 4 個中間站先鎖定（直奔目標讀作程序化）；輪廓光兩圈快亮/慢弱；雙層影隨高度生長。側向水平機位優於俯拍（Q6）。
- 對應：B01 title lockup 前嘅主角卡、單一重點物件立傳。

**spotlight-sweep-moves** `references/shots/effects/spotlight-sweep-moves.md`
- 點解好用：暗場「光即敘事」三式——光到邊邊亮、光走即謝幕，聚光同時係照明、運鏡同剪輯。
- 關鍵參數：聚光移動/擴張**嚴格 linear 零 easing**（加 ease 光就有「主觀意圖」，匀速先係探照燈）；C 式半徑終值要啱啱好喺片尾蓋滿全屏（1300@1080p/100f，過大會提前飽和假匀速）；貼邊光線 3–4 層辉光（blur26 寬糊 + blur9 + 亮芯 + 粉偏移），層少讀作細線描邊；顯影罩 feather ~15%。
- 對應：spotlight sweep 強調、暗場 chapter 開版。

**dashboard-glow-highlight-pill** `references/shots/effects/dashboard-glow-highlight-pill.md`
- 點解好用：glow-highlight 嘅連續變形教科書——光斑巡遊（宣告）→ 拉成膠囊（蓄力）→ 起筆描出彈窗輪廓（交棒），三段係同一束光，斷開就變三個唔相干嘅動畫。
- 關鍵參數：光斑 6 段 keyframe 22×22 → 96×16 單調行進（中途回擺一次就讀作「搵緊嘢」）；描邊 draw-on `outQuad` 接住膠囊嘅勢、之後收斂 2.9→1.0px + 色 #fff0c4→#e6c887（**光變成 UI 嘅語義，唔收斂就一直係特效**）；彈窗底板先到（opacity×0.72）、文字後清晰；背景 blur 峰值 4.5px 之後退 52%。
- 對應：glow highlight 指引、彈出注解卡嘅光學交棒。

**light-play-moves** `references/shots/effects/light-play-moves.md`
- 點解好用：光效三種筆觸分職責——A 掃（暗場標題點亮）、B 擦（主角卡 45° sheen 加冕一次）、D 暈（撞停幀 halation 炸開）。地基判例：**白底上提亮不可見**，全部要深底。
- 關鍵參數：A 暗版 0.07 vs 全亮 1.0；B 高光帶寬 1.6×卡寬、峰值 rgba(255,255,255,0.32)、40–68f 掃**一次**、圓角裁住；D 晕層 blur 22px + brightness 1.8、scale 1→1.3 用 6f 猛漲、20f linear 回落（擴散 out-cubic / 消散 linear 解耦判例）。**全片光效合計 ≤2 次**——光係最快跌價嘅手法。
- 對應：glow-highlight 用量紀律、金句卡 sheen。

### 1.7 typography 系（造字 / 字級動效）

**scramble** `references/shots/typography/scramble.md`
- 點解好用：三種「造字」入面嘅「機器在算」——先滿屏噪聲再左→右逐個咬定真字。字數就係節拍數，最挑文案。
- 關鍵參數：每 2f 跳一次亂碼（15 次/秒；1f 糊成灰帶、4f+ 讀作慢翻）；鎖定窗 0.25→0.85 + 每字 ≤6f 隨機抖動（冇抖動就係 progress bar）；鎖定閃 ≈3f + 光暈 18px；**必須等寬字體 + 固定槽寬 0.62em**；起手 6f 空屏。文案 ~20 字符係甜點。
- 對應：tech 感標題、版本號/代號揭曉。

**typewriter-moves** `references/shots/typography/typewriter-moves.md`
- 點解好用：A 打字當**引信**（terminal 敲完命令、回車幀急推硬切入產品）；B 打字當**獨白**（打平庸詞→猶豫→退格→更快打出賣點詞嘅三幕劇）。
- 關鍵參數：A 2f/字符、光標 f%12<6 方波閃、回車幀 6f 急推 scale 1→3.2 + 末 2f blur 10px 硬切；B 三檔速度 打 2f / 停 16f / 退 1.5f / 重打 1.5f 零猶豫（**三檔差必須可感**，等速改口讀作 bug）；光標三態：打刪常亮＝果斷、停頓先閃＝猶豫。B 全片 ≤1 次。
- 對應：CLI/教學開場、否定式文案卡（「唔係 X，係 Y」）。

**split-flap-title** `references/shots/typography/split-flap-title.md`
- 點解好用：機場翻牌屏「播報腔」——倒計時/發佈日期/數據揭曉天然啱。明暗差比 rotateX 本身更被肉眼讀到。
- 關鍵參數：單次翻牌 5f `Easing.in(quad)`（重力感，匀速讀作電子屏假翻）；每格翻 3 次（2 亂碼 + 1 落定）；stagger 4f 左→右成波；停定咔嗒 6px 下沉回彈（**4px 無感判例**——加幅度唔好調曲線）；掉落葉 brightness 1→0.55。開頭 ≥20f 靜止建立、收尾 ≥15f。一支片 ≤1 次。
- 對應：日期/數字宣告卡、機械感 chapter card。

**gradient-word-sweep** `references/shots/typography/gradient-word-sweep.md`
- 點解好用：整句白字得個關鍵詞「通電」——彩光左→右掃過充能、波前最亮向後衰減、填滿後字符間跳細閃電。判例三條全係用戶逐字裁決。
- 關鍵參數：掃充 **15–20f 要快**（>28f 讀作 progress bar）；波前增亮帶 ~34% 詞寬；穩態泛光 4 層 opacity 0.55–0.72 檔（0.75+ 被裁「泛光有啲強」）；閃電紫紅系、外 6 / 中 2.4 / 核 1.4px、同屏 ≤2 道、間歇 >8f；**填充過程禁跟隨光點**（判例：讀作廉價裝飾）。關鍵詞以外正文保持純白靜止。
- 對應：金句卡賣點詞充能、黑場口號幀。

**title-demote-to-label** `references/shots/typography/title-demote-to-label.md`
- 點解好用：標題「降格而不退場」——居中大字企穩一拍後一條連續補間縮到 0.3x 飛去左上角做欄目標籤，觀眾免費攞到空間記憶，內容喺降格途中已開始生長、交接零空檔。
- 關鍵參數：降格**單次連續補間** 20f `Easing.inOut(cubic)`（分兩段「先縮後飛」會讀作兩個動作）；顯影 12f blur 12→0；顯影後企穩 ≥18f 先降格；骨架生長起點 = 降格開始 +12f；標題文案 ≤3 個詞（縮完仲要做得標籤）。
- 對應：chapter card → 常駐角標嘅過渡、section label 系統。

**type-rhythm-sync** `references/shots/typography/type-rhythm-sync.md`
- 點解好用：「字唔郁、屬性郁」——A 字重隨鼓點脈衝（標題做低音炮）、B 卡拉OK填色跟旁白逐詞點亮（口播視線引導，啱晒 talking-head！）。
- 關鍵參數：A 脈衝包絡 `(1−t/10)^0.8`、stroke 連續衰減 + fontWeight 400↔900 離散跳變疊加、拍距 20f > 衰減窗 10f；B 逐詞 [start,end] 幀區間 linear 填充、詞間留 4–10f 換氣、**讀指下劃線 8px**（4px 喺 1080p 縮圖下不可見——實渲踩坑）、詞數 ≤6/屏。兩式都係聲音強依賴。
- 對應：字幕跟讀高亮、拍點字卡；A 全片 ≤1 段。

### 1.8 rhythm/拍點 系（切點 / 打斷 / 節拍器）

**beat-cut-moves** `references/shots/rhythm/beat-cut-moves.md`
- 點解好用：「切」本身當鼓點——A 遞進硬切串（間隔減半加速逼近，預告片式）、B 三閃定格（快門連拍加冕）。切串完 hold 要俾**雙倍**。
- 關鍵參數：A 切點間隔 **16→12→8→6→4f 減半律**（等差縮讀唔出加速；末間隔 <4f 眼追唔切）；切幀 1f brightness 1.05 + 6% 白層（「咔」唔係閃光燈）；末刀定格 hold 35f；B 三閃 22f→18f 漸緊、白閃 0.95→0 走 4f、快門餘韻 scale 1.03→1 + −16px 沉降、末段 hold 60f。真硬切零過渡幀——手多加 2f crossfade 節拍感即刻糊。切串全片 ≤1 次。
- 對應：高潮段 montage、三連 punch 收結。

**rhythm-interrupt-moves** `references/shots/rhythm/rhythm-interrupt-moves.md`
- 點解好用：「打斷連續性」當節奏器——B 三級跳切推近（1x→1.6x→2.6x 零補間，「睇呢度、再近啲、就係佢」）、C 頻閃黑幀倒數蓄壓。
- 關鍵參數：B 挡差 ≥1.5×先讀得出（唔係「畫面抖咗一下」）、每跳 2f 加深脈衝當 tick、各挡 hold ≥35f、三挡**同 transform-origin 釘死目標**；C 黑幀表 [40,48,55,61,66,70,73,76,79] 各 2f、間隔 8f→3f 收斂（等距頻閃只係閃冇「逼近」）、末閃掀開 scale 1.35 落錘。C 有光敏警示、全片 ≤1 次。
- 對應：jump-cut punch-in（我哋 punch-in 嘅節奏版）、高潮前倒數。

**beat-step-list-theme-cycle** `references/shots/rhythm/beat-step-list-theme-cycle.md`
- 點解好用：三通道節拍器——列表行、膠囊色、全場底色**鎖死同一拍點**齊跳，用最平嘅變量切換砌出全片最高節奏密度。
- 關鍵參數：拍長 18f（0.6s ≈100BPM，改佢就係改 BPM 對音軌）；**跳變窗僅拍頭 6f** `1-(1-x)^3.2` 陡 ease-out、其餘 12f 完全靜置（「跳」唔係「滑」）；膠囊 squash 1.12→0.97→1；相鄰主題底色同明度不同色相（明度跳變讀作閃屏）；開拍前 30f 靜置鋪墊、末拍後 hold ≥30f；詞表 ≥ 拍數+2。
- 對應：多主題/多氣質連打、歌詞式列舉段。

**timeline-travel** `references/shots/data/timeline-travel.md`
- 點解好用：changelog/發展史拍成「沿時間軸旅行」——緩起→衝刺→急刹三段變速，速度講「發展快」、急停講「而家最緊要」。
- 關鍵參數：變速斷點 [0,0.15,0.88,1]→[0,0.055,0.9,1]（中段唔夠快就冇旅行感）；卡片喺相機到達刻度**前 6f** spring 彈立（damping ~11，到咗先彈已經錯過）；急停推近 scale 1→1.28 / 10f；急停後靜止 ≥30f 預算**前置**（首版 25f 唔達標要將急停幀前移）。次刻度小點係速度感參照物，刪咗就感覺唔到快。
- 對應：timeline 卡、里程碑回顧段。

### 1.9 data/數字 系（計數 / 對比）

**odometer-digit-roll** `references/shots/data/odometer-digit-roll.md`
- 點解好用：王牌數字「機械系」登場——唔係飛入嚟，係「計出嚟」。滾動自帶懸念、逐位鎖定自帶節奏（噠、噠、噠）。
- 關鍵參數：位 i 於 20+i×7f 開始、16f `Easing.out(cubic)` 減速至目標 **+0.5 行過衝**、再 6f 彈回鎖定；殘影 2 個錯幀副本 opacity 0.25/0.12、速度門控；全體鎖定幀整體加深脈衝 8f + 1.035 微縮放；**tabular-nums 必開**（非等寬每滾一格整行抖）；數位 ≤6、大數用縮寫（12.4M）；滾嘅必須係真值各位（亂數會俾暫停黨捉到）。
- 對應：數據卡主菜、成績/訂閱數揭曉。

**counter-confetti** `references/shots/data/counter-confetti.md`
- 點解好用：數字唔係「顯示」係「衝線」——easeOutQuart 前 1/3 時間跑完 2/3 數值；靈魂係**搶拍**：彩紙比數字到位早 0.04（≈5f）爆開，慶祝先於結果、情緒壓過信息。
- 關鍵參數：計數窗 0.06–0.56 easeOutQuart；scale 0.2→1.3 冲入再 outBack 回落；BURST=0.52（提前 0–0.02 讀作同拍、>0.08 似「別人嘅慶祝」）；52 片紙屑真物理（g≈2.5×|vy| 令拋物線頂喺畫面上 1/3）；標籤字距 11px→5px 收緊做「落章」。
- 對應：里程碑慶祝卡、訂閱/成績爆數。

**before-after-slider-scrub** `references/shots/data/before-after-slider-scrub.md`
- 點解好用：「用前 vs 用後」一鏡講清——**快甩慢掃嘅速度對比就係節奏**：快甩宣告「變咗」、慢掃證明「變咗喺邊」。
- 關鍵參數：快甩 12f（8%→76% out cubic 過衝）→ 回彈 12f → 停 ~18f → 慢掃 ~48f（70%→40%）；速度比 ~5:1（<3:1 對比不可感）；慢掃終點停 40% 唔係 0%（留 after 喺畫面做結論）；手柄速度差分驅動 scaleX 微拉伸峰值 1.18；before 要可信，唔好自黑式整醜。
- 對應：comparison double-cards 嘅動態版、AI 前後對比。

### 1.10 outro/CTA 系

**logo-shrink-wordmark-lockup** `references/shots/outro/logo-shrink-wordmark-lockup.md`
- 點解好用：片尾「盖章」——滿屏圖形能量坍縮成一枚小 icon（演出態→標準態），然後按 lockup 規範逐步落位：icon 讓位、字標入場、標語押尾。
- 關鍵參數：收束 scale 5.4→1（t 0.02–0.28 inOutCubic）+ 過衝刹車 `sin(π)*0.06`（到位脹 6% 再回落）；缺口愈合/變色同收束**同軌完成**（落位後仲變緊色讀作「未準備好」）；icon 左移 −68px（0.34–0.47）同字母首入（0.46）無縫；字母 stagger 0.035/字；標語整行淡入唔逐字（注腳唔係主角）。
- 對應：CTA / 頻道 logo 收版。

**grain-dissolve** `references/shots/outro/grain-dissolve.md`
- 點解好用：「一句話濃縮成一個詞」拍成物理事件——成句沸騰成顆粒（信息解體）→ 顆粒坍縮成更大更亮嘅短字標（「一切歸結為佢」）。天然 outro 卡點。
- 關鍵參數：`feTurbulence`(0.9→1.3) + `feDisplacementMap`(scale 0→52，<30 只係毛邊、>80 認唔出輪廓) + blur 0→1.1px 同一條 burst 曲線；**seed 每幀換（floor(t*46)，≥20 次/秒）**顆粒先永不靜止；換字交叉 0.60–0.71 藏喺最沸騰段；辉光凝聚冲高 0.7 係卡點位壓 BGM 重音；選區框 0.55–0.64 撤走要早過凝固完成。
- 對應：「XX. Now Live」式上線宣告、金句 outro。

---

## 2. SFX 庫目錄與配樂方法論

### 2.1 檔案位置與攞法

- 檔案留喺 clone / upstream repo，**唔複製入我哋 project**。
- GitHub raw 攞法（pattern）：
  `https://raw.githubusercontent.com/Vincentwei1021/video-shotcraft/0d6f0b57f0d4d6700761644c07f7ef03c3e50234/assets/audio/sfx/<類別>/<檔名>.mp3`
  BGM 同理：`.../assets/audio/bgm/<檔名>.mp3`
- 每檔嘅 Mixkit 原始 URL 記錄喺 `assets/audio/ATTRIBUTION.md`（例：`click-camera.mp3` = https://assets.mixkit.co/active_storage/sfx/1133/1133-preview.mp3）——商用最穩陣係經 ATTRIBUTION 表由 Mixkit 原始連結攞。
- 逐檔時長/峰值/建議釘點：`assets/audio/AUDITION-2026-07-27.md`。

### 2.2 十六類目錄（149 個 SFX + 5 首 BGM，源自 `references/sound-design.md` §3.0）

| 類別 | 數量 | 裝乜 | 幾時用 |
|---|---|---|---|
| `transition/` | 23 | whoosh / sweep / 風 | 運鏡、場景切換、元素飛入飛走 |
| `impact/` | 14 | impact / thud / stomp / bass hit | 落地釘點、重拍、slam |
| `riser/` | 1 | 上升鋪墊 | 入 finale / 大鏡頭前蓄力 |
| `camera/` | 10 | 快門、變焦 | punch-in、crash zoom、對焦、iris |
| `ui/` | 18 | 點擊、開關、pop | UI 反饋（**要逐個試聽**，見 2.5） |
| `text/` | 13 | 打字機、鍵盤、書寫 | 打字揭示、描線、下劃線 |
| `paper/` | 10 | 紙、翻頁、印刷 | 翻頁轉場、紙藝 |
| `film/` | 8 | 放映機、膠片、磁帶、黑膠 | 預告片語法、回帶變速 |
| `light/` | 10 | sparkle、光效 | 掃光、點亮、餘韻閃光（**sparkle 目錄名係 light/，冇 sparkle/**） |
| `data/` | 13 | glitch、電流 | HUD、stream 輸出、故障 |
| `scifi/` | 5 | 科技底噪 | 長樣本鋪底 |
| `mech/` | 8 | 機械、鎖 | 組裝、鎖定、形變 |
| `glass/` | 4 | 玻璃碎裂（真實材質音，唔喺禁列） | 碎裂轉場、硬切冲擊 |
| `fluid/` | 5 | 墨水、水、氣泡 | 墨開場、顆粒填充 |
| `crowd/` | 3 | 掌聲、心跳 | 合影收尾、張力 |
| `counter/` | 4 | 計數器、鐘、倒數 | 數字滾動、timeline |

**主力檔名精選**（模板片實戰用過 + 常用）：
- transition/: `transition-soft`（柔轉場，場景切入一發）、`whoosh-fast`、`whoosh-big`（大幅運鏡）、`transition-snap`（0.57s 短促落定）、`swoosh-quick`（0.78s 字卡統一音）、`air-whoosh-powerful`、`sweep-fast`、`swoosh-slow`、`warp-slide`
- impact/: `impact-deep-whoosh`（riser→impact 句式嘅 impact 位；同已刪嘅 impact-cine 字節相同）、`impact-cine-big`（7.9s 長尾混響）、`impact-movie-epic`、`bass-hit-short`、`bass-hit-futuristic`、`stomp-apocalyptic`、`metal-spring-hit`、`hit-fast-exciting`
- riser/: `riser-cine`（4.81s 電影系鋪墊）
- camera/: `click-camera`（0.35s 快門確認，模板片全片最響 vol 0.6）、`camera-shutter-hard`、`camera-autofocus`（9.6s 一般只用前 10–20f）、`zoom-air-fast`、`ui-zoom-in`/`ui-zoom-out`
- light/: `sparkle`（4.55s 光效 reveal）、`shimmer-sparkle-sweep`、`sparkle-poof-hit`、`sparkle-touch`、`stardust-swish`、`light-sweep-magic`
- text/: `keyboard`（19.6s 長樣本，按段落裁 24f/44f 用）、`typewriter-hit-single`/`-hard`/`-soft`（雙樣本交替用）、`typewriter-return-bell`、`marker-pen-line`（marker 下劃線拟音）、`chalk-line`、`pen-write-paper`、`write-fast`
- ui/: `pop`（0.48s 列表逐項落入）、`switch-light`/`switch-tap`/`switch-click-quick`（真實開關拟音 ✅）、`pop-electric`（連發可用）
- paper/: `paper-page-turn`/`-big`、`paper-slide`、`paper-wind-blow`（5.5s）、`paper-slice-quick`
- counter/: `clock-tick-single`、`clock-knob-spin`（呢兩個峰值低，見 2.6）、`countdown-bleeps`
- mech/: `gear-lock-metallic`（翻牌/鎖定）、`lock-quick`、`machine-activate-short`
- data/: `glitch-static`、`power-up-electronic`（5.0s）、`data-scan`、`whoosh-electric`
- crowd/: `applause-rhythmic-loop`（5s 可 loop）、`heartbeat-single`、`clap-single`
- glass/: `glass-break-hammer`、`glass-hit-cine`、`glass-plate-slide`
- fluid/: `water-splash`、`liquid-bubble`、`sand-swish`
- film/: `tape-rewind-cine`/`-fast`、`vinyl-needle-drop`、`projector-spin-antique`（21.7s 底噪）
- bgm/: `bgm-tech-house`（~124BPM，模板片定稿）、`cat-walk`（House ~129）、`house-vibez`（House ~123）、`g-eazy-nba-type`（Hip Hop ~86）、`tonight-hiphop`（Hip Hop ~103）

### 2.3 動效 ↔ SFX 配對方法論（`references/sound-design.md`）

1. **順序鐵律**：畫面結構鎖定 → 先鋪 BGM 定能量骨架 → 逐拍釘 SFX。時間線一改，SFX 全表重釘（佢哋三次重釘有兩次係畫面返工嘅連帶成本）。
2. **詞彙表按「片種」揀，唔係按「事件」揀**：產品片五詞 = whoosh(運鏡)→`transition/` / impact(落地)→`impact/` / riser(鋪墊)→`riser/` / sparkle(光效)→`light/` / transition(轉場)→`transition/`。**禁嘅係音色唔係動作**——判別問句：「呢個音似真實世界嗰件物件發出嘅聲（快門/開關/玻璃/紙），定似遊戲引擎嘅反饋提示音？」前者用、後者棄。
3. **BGM 音量包絡**：模板片 `[0, 30, TOTAL-50, TOTAL] → [0, 0.34, 0.34, 0]`（1s 淡入、1.7s 淡出）；BGM 壓喺 **0.34** 俾 SFX 留 headroom；SFX 常規區間 **0.2–0.6**（點擊確認 0.6 最響、pop 連發尾音 0.25 最輕——用響度表達「呢一拍幾重要」）。
4. **riser→impact→sparkle 三拍句式**（收束大鏡頭固定寫法）：`riser-cine`（鋪墊段起）→ **約 35f 後** `impact-deep-whoosh`（主體 stamp 落地，全片響度峰值）→ **25f 後** `sparkle`（餘韻光效）。模板片 f945→f980→f1005，係定稿後唯一冇改過嘅句式。其他小句式：場景切換 = `transition-soft` 一發；字卡出場 = `swoosh-quick` 統一音；點擊確認 = `click-camera`。
5. **連發防機槍三招**（實證無 playbackRate 變調）：①雙樣本交替（例 `typewriter-hit-hard` + `-soft`；注意 4 對檔案字節相同唔可以互為雙樣本：transition-soft=air-zoom-vacuum、swoosh-quick=sweep-fast-small、impact-transition=impact-epic-trailer、impact-cine=impact-deep-whoosh）；②音量階梯遞減（pop 六連發 0.40/0.37/0.34/0.31/0.28/0.25）；③間隔跟動畫曲線加速（8f→3f），密到糊埋一齊就俾聲音淡出成一條 swoosh，唔逐個配。
6. **拟音優先於裝飾音**：打字畫面配鍵盤聲、逐條落入配逐個 pop——泛用 swoosh 冚唔住有辨識度嘅動作；音頻裁到同動作**嚴格等長**。
7. **釘幀一律相對 shot 起點**（`SHOTS.<shot>.from + offset`），唔寫裸絕對幀號——改前面鏡頭長度時 SFX 自動跟隨。

### 2.4 卡點（beat-sync）方法論（`references/music-beat-sync.md`）

- **音樂先行**：強節奏 BGM 嘅片，網格未驗收唔設計分鏡。
- BPM 唔信 `beat_track` 個 tempo 標量（實測偏差 2%+：129.2 vs 真值 131.97）——攞成條 beat 序列做**最小二乘等距網格拟合** `t_i = t0 + i*T`；驗收：殘差 ≤±15ms、match ≥98%、平均誤差 <10ms、全曲漂移 <5ms。半倍/雙倍歧義用 kick 落拍覆蓋率投票，唔靠聽感。
- 三分類鼓點驅動三類動效：**kick (40–160Hz) → slam/骤縮**；**snare (150–500Hz + 1–3kHz) → 替換/閃切/構圖切換**；**hihat (6–14kHz) → 微動密度**（hihat 疏嘅段落微動效必須收）。
- 時間線用拍號寫（`beatF(n)`）；密集規則切點用網格、**稀疏重音釘真實瞬態**（唔用網格插值點）；最強 slam 幾乎總喺整數拍（佢哋試過釘 b52.5 偏咗 +5.75f）。
- 渲後回測：成片抽音軌重跑網格，切點誤差 **≤3f 合格（感知閾值）、≤1.5f 理想**；30fps 取整誤差上限 ±16.7ms，唔好聲稱 <5ms 視覺精度。
- BGM 鼓點已密時 SFX 要克制：只釘畫面獨有動作，大 slam 全片 2–3 處，其餘讓位俾 BGM 嘅鼓。

### 2.5 `ui/` 目錄逐個試聽表（`sound-design.md` §3.3——全庫唯一質感分裂嘅類別）

- ✅ 直接用（真實物件拟音）：`switch-light`、`switch-tap`、`switch-click-quick`、`pop`
- ⚠️ 成片語境試聽先定：`hitech-touch-magnet`、`chime-crystal`、`pop-electric`、`ui-select-click`
- ❌ 默認唔用（合成 tone/bleep/notification 質感，正正係「遊戲音」禁區）：`ui-click-tone`、`ui-confirm-bleep`、`ui-confirm-tone`、`ui-tone-quick`、`ui-success-soft`、`ui-notify-tech`、`ui-message-pop`、`ui-popup-dry`、`ui-option-select`、`ui-select-modern`。例外：刻意做「系統喺度講嘢」嘅敘事（HUD 播報/AI 回執）先可以用，而且要寫低點解。
- 同樣逐個試聽紀律適用 `data/` 同 `scifi/`。

### 2.6 兩份特殊名單（`sound-design.md` §4.1）

- **>5s 長樣本 21 個必須顯式裁斷**（對應 GSAP 即係要自己 trim / 設 duration）：`scifi-computer-ambience` 23.5s、`projector-spin-antique` 21.7s、`keyboard` 19.6s、`write-blackboard` 13.9s、`mech-robotic-futuristic` 9.6s、`camera-autofocus` 9.6s、`paper-book-browse-fast` 9.3s、`space-intro-futuristic` 8.1s、`light-spell` 8.0s、`impact-cine-big` 7.9s、`tech-hum-futuristic` 6.0s 等。判據：底噪/loop 類按鏡頭長度鋪；動作類按動作長度裁；**帶長尾混響嘅 impact（impact-cine-big / impact-movie-epic / metal-drop-scifi-small）俾尾音自然衰減，硬裁會顯得乾**。
- **峰值 <-12dB 輕音 7 個**（俾到 volume 1.0 都會被 BGM 冚住）：`data-load-os` −24.6dB、`pencil-write-short` −22.7dB、`write-fast` −20.0dB、`wing-flutter` −17.9dB、`ui-zoom-in` −14.3dB、`clock-knob-spin` −14.0dB、`clock-tick-single` −13.9dB。三條出路按優先級：①換素材（首選）②ffmpeg `loudnorm=I=-16:TP=-1.5` 預歸一化 ③俾 >1 增益但渲後查峰值防 clipping。

---

## 3. 美學規則 / QA checklist 抽錄（適用於 overlay-on-A-roll 嘅部分）

源自 `references/aesthetic-rules.md`（判例式，每條有真實返工背景）+ `references/final-review.md`。編號沿用原檔方便回查。

### 節奏（R）
- **R1 落定要呼吸**：載信息嘅元素（字卡/數字/grid 全貌）落定後靜止 **≥1s** 先切；呼吸優先俾品牌記憶點（wordmark hold 滿 1 秒），唔係求其俾件普通元素。
- **R2 速度感來自加速度**：飛入/滾動一律非線性 easing + 錯峰，匀速直線運動讀作廉價 PPT；批量入場要「越嚟越快」嘅硬加速 + 揸住物理隱喻，滿板後靜止 **0.5s** 先切。
- **R3 寧慢勿快**：初版默認放慢一檔；主體動作弧 ≥3s；模擬交互按真人操作速度（觀眾要跟得切做一次）。佢哋全部歷史反饋都係「放慢/停耐啲」，**從未有一次「太慢了」**。排時間線先劃走 hold/rest 幀預算，唔係排完動效先搵窿。

### 質感（Q）
- **Q4 光效寧缺毋濫**：glint/掃光**唔群發**——批量入場靠運動本身，唔靠逐個發光；保留嘅光效必須裁入 border-radius 內（光溢出圓角係廉價感典型來源）；一個鏡頭最多俾主角一次；做完對住 render 幀自問「好唔好睇」先交。
- **Q5 開場單主角**：一個主角、一條完整動作弧（起-承-落），多元素齊舞撐唔起第一印象。
- **Q6 機位服務可讀性**：信息密集（列表/堆疊）保持正視；文字特寫用側向水平角度；風格化傾斜逐鏡驗證，禁止全局一刀切。
- **Q9 飛入終點要係真實槽位**：元素落定後要「嵌入」版面，唔好永久浮喺頁面上空——落唔到地就顯得假。
- **Q11 可讀文字最低有效字高（對 overlay 直接適用）**：1080p 成片按手機/細窗校準——敘事字幕**有效字高 ≥56px（≥5.2% 幀高，推薦 60px 檔）**；副題/統計/URL 等輔助文字 **≥32px（≥3%）**；有效字高 = fontSize × 所有 scale × 透視壓縮，**量 render 出嚟嘅實際 pixel，唔係睇 code 入面個 fontSize**。文字只有兩態：「紋理」（明顯虛化俾人唔去讀）或「要讀」（達標字號 + 夠對比，壓浅底要配 scrim/投影）——「重排咗但仍讀唔清」嘅中間態唔存在，讀唔到嘅字寧願刪。自檢法：抽一幀縮到 480px 寬睇仲讀唔讀得清。

### 聲音（S）
- **S1 按片種唔按事件揀音**：電影系詞彙（whoosh/impact/riser/sparkle/transition），禁遊戲音包**音色**；BGM 候選必須墊入成片試聽（單聽判斷唔到氣質——佢哋 v1→v2 隔 22 分鐘就再被否）。
- **S2 SFX 逐拍釘幀、聲明式表管理**：每條註明對應畫面動作；連發用「雙樣本交替 + 音量階梯遞減 + 間隔加速」三招。
- **S3 聲音喺畫面鎖定後先做**；任何時長/次序改動，收尾固定包含「全表 SFX 重對」。
- **S4 拟音優先**：畫面有咩動作就配嗰個動作嘅真聲；音頻裁到同動作嚴格等長，唔好拖過動作結束仲響緊。

### 文案（C）
- **C1 文案喺畫面鎖定後照最終鏡頭重寫一次**；純動畫段 >3s 要配解說 caption（品牌收尾除外）。
- **C2 標語要具體**：帶功能名 + 具體收益，抽象隱喻詞逐個具體化；重要內容出場前加引導字卡。
- **C3 3D 場景內嘅注記要活喺同一 3D 空間**（同透視、同相機），平面疊字會同場景脫節。

### 流程（P）+ 手法紀律
- **P1 交付前自己 render 截幀逐一檢查**，唔好將首檢交俾用戶／觀眾。
- **P4 一種手法全片只當一次主角**；重複鏡頭/重複 tagline 一律刪；剪輯自檢問「呢個鏡頭俾咗咩新信息」。
- 各卡自帶用量上限（全部照抄可用）：砸入 ≤2、急推 ≤2、硬切串 ≤1、頻閃 ≤1、翻牌字 ≤1、改口打字 ≤1、光效合計 ≤2、幾何擦除 ≤2、dolly-zoom ≤1、字重脈衝 ≤1 段、cel-flash ≤1 段。**Overlay 語境建議再收緊一級。**
- **能量骨架**（`references/sequences/promo-energy-arc.md`，可移植做長片 overlay 規劃）：①低開品牌（8–12%，hold ≥1s）→ ②單主角立傳（12–15%，全片最慢最有質感）→ ③功能爬升段（55–65%，高能↔穩節奏交替，每 1–2 個功能鏡插一張 50–55f 呼吸字卡）→ ④峰值收場（13–16%，全片能量最高點）。信息密度最高嘅段放喺峰值收場之前。兩端（開場 hold / 結尾峰值）唔可以慳。
- **QA 報告格式**（`references/final-review.md`）：逐條編號 `✓` 或 `✗(位置=鏡頭/幀號)` + 截圖證據；唔好用冇證據嘅「整體唔錯」代替逐項檢查。音頻專項：SFX 有冇釘喺真實動作幀（A2）、卡點誤差 ≤3f（A3）、riser→impact→sparkle 句式成唔成立（A4）、長樣本有冇拖尾（A5）、每條 SFX 喺渲染產物度真係聽唔聽到（A6）、UI 音係唔係合成提示音（A7）。

---

## 4. 授權與 attribution（商用前必讀）

### 4.1 Repo 本體（recipe 卡、規則文檔、demo 代碼）
- **Apache-2.0**（`LICENSE`）——判斷詞彙、參數、規則攞嚟參考同改寫**冇問題**，包括商用。如果將佢哋文檔內容大段複製再分發，保留 Apache-2.0 授權聲明同 attribution 係規矩。

### 4.2 鏡頭卡嘅「靈感來源」（`references/shots/ATTRIBUTION.md`——重要 nuance）
- 2026-08 批次 48 張卡係研究自公開發佈嘅產品片/開源主頁（anime.js、remotion-bits.dev、多個 X 帳號、抖音帳號、Firecrawl/Willow Voice/Bear/Notion/Slack/ClickUp/Perplexity 等宣傳片），**全部從零重寫、無原片素材**。
- 佢哋自己講明：「來源作品公開發佈**唔等於**授予複刻或衍生嘅許可。本表記錄嘅係研究溯源，**唔係授權憑證**。」抽象嘅動效**手法/技法**（時序、easing、編排邏輯）屬方法範疇；**具體表達**（原片畫面、美術、品牌元素、可辨識嘅整體視聽呈現）受版權/商標保護。
- **對我哋嘅意思**：用卡入面嘅 timing/easing/節奏判斷嚟指導自家 HyperFrames overlay = 安全；**逐幀複刻某張卡背後嗰條原片嘅完整視聽表達（連構圖連配色連文案）= 有風險**，唔好做。

### 4.3 音效 / BGM（`assets/audio/ATTRIBUTION.md`）
- **主體**：絕大多數係 **Mixkit Sound Effects Free License / Mixkit Stock Music Free License——免費商用、免署名**。扩充兩批（2026-07-19 / 2026-07-27 下載）全部有逐檔原名 + URL，商用穩陣。
- **⚠️ 例外名單（商用前須逐個確認來源）**：首批批量下載時 metadata 被抹，以下檔案**無法反查**——`keyboard.mp3`、`riser-cine.mp3`、`sparkle.mp3`、`whoosh-big.mp3`（標 Mixkit 但反查唔到原曲目）、`pop.mp3`（**來源待考**，連係咪 Mixkit 都未肯定）、`bgm-tech-house.mp3`（Mixkit 但無法逐曲對回曲庫）。呢六個檔要商用嘅話：一係搵到出處確認，一係用同類別有 URL 嘅替代（例：sparkle → `shimmer-sparkle-sweep`；riser 可上 Mixkit 自己搵一條登記返 URL；pop → `pop-electric` 或自搵）。
- 其餘 4 首 BGM（cat-walk / g-eazy-nba-type / house-vibez / tonight-hiphop）有齊藝術家 + URL，Mixkit Music Free License 免署名可商用。
- 歷史備考：佢哋曾用 incompetech（Kevin MacLeod，**CC-BY 4.0 要署名**）同 Kenney（CC0），兩批都已移除唔喺 repo 度——如果我哋自己去呢啲源攞嘢，記住 CC-BY 嘅署名義務。
- 佢哋嘅紀律值得照抄：**下載素材當場記錄曲名/URL**（事後反查唔到就係上面六個檔嘅下場）；新素材入庫先跑 md5 去重（佢哋發現 4 對檔案係同一素材下載咗兩次改咗名）。

---

## 5. 美術總監查閱指引（sub-agent 用）

1. 收到一個 beat，先問三樣：**情緒能量**（高/中/低）、**功能**（強調/入場/轉場/數據/收尾）、**畫面語境**（overlay 疊喺人面旁邊定全幅插卡）。
2. 由情緒×功能揀「系」：落章強調 → 1.1 stamp-slam 系；逐項/卡片入場 → 1.2 spring-pop 系；標題/字卡浮現 → 1.3 blur/settle 系；換章/接縫 → 1.4 wipe/transition 系；圈重點/教學標注 → 1.5 draw-on 系；視線引導/推鏡 → 1.6 camera 系；造字/字級戲 → 1.7 typography 系；卡點/montage → 1.8 rhythm 系；數字/對比 → 1.9 data 系；收版 → 1.10 outro 系。
3. 系入面揀卡：先讀「點解好用」對語義，再直接攞「關鍵參數」做 GSAP 換算起點（f ÷ 30 = 秒），**「命門」標明嘅參數唔准降檔**。
4. 每張卡出手前過三關：①佢個用量上限（第 3 節手法紀律表）今條片用咗未？②落定之後有冇 R1 嘅 ≥1s 呼吸／批量收尾 0.5s？③文字過唔過 Q11 字高線（字幕 ≥56px、輔助 ≥32px @1080p）？
5. 配 SFX：動效類別 → 2.2 目錄表搵類 → 2.3 句式（大鏡頭收束用 riser→impact→sparkle 三拍：riser 起 → +35f impact → +25f sparkle）→ 連發用防機槍三招 → `ui/` 檔查 2.5 三色表 → 長樣本/輕音查 2.6 名單。
6. 卡點片：切點誤差目標 ≤3f；kick 配 slam、snare 配替換/閃切、hihat 密度決定微動密度；稀疏重音釘真實鼓點唔釘網格。
7. 授權紅線：第 4.3 節六個「無法反查」音檔商用前要換或確認；鏡頭卡只借判斷、唔逐幀複刻原片表達。
8. 記住成套嘢最大嘅單一教訓：**歷史反饋全部指向「放慢/停耐啲」，一次「太快了」嘅反向投訴都冇**——猶豫嗰陣，慢一檔、hold 長一啲，永遠係贏面高嗰邊。

---
*抽錄完。原始 repo 唔好改、唔好跑佢個 Remotion pipeline——要新判例就去 upstream 讀最新 commit。*
