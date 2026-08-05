# Session 打包 — Reel 總司令拆解 → 52 秒成品

**日期**：2026-08-05
**Branch**：`claude/reel-commander-breakdown-dd7n9z`（已 push，未開 PR）
**起點**：Anson 貼咗一條對手 IG Reel，要「總司令拆解」

---

## 已完成（呢個 session）

| # | 產出 | 檔案 |
|---|---|---|
| 1 | 對手 Reel 完整拆解 + 逐字稿 + 爆款歸因 | `docs/teardown-dotai-DbqHhNiCgV3.md` |
| 2 | 52.5 秒廣東話逐字稿（可即開機錄） | `docs/script-ai-agent-3-levels-52s.md` |
| 3 | 同一份稿嘅機讀 EDL | `edl/ai-agent-3-levels-52s.json` |
| 4 | 剪片 agent（EDL → 9:16 成品，字幕燒入） | `reel_cutter/` + `README.md` + `SKILL.md` |
| 5 | 22 個單元測試（含稿件語速回歸測試） | `tests/test_reel_cutter.py` |

**已驗證**（真跑過）：animatic 同真素材兩條路徑都出到準確 52.500s / 1080×1920 / 30fps，中央裁切同中文燒入字幕正常，22/22 測試通過。

**未做**：
- `media/` 空白 —— 素材、VO、音樂全部未有（gitignore，唔入 repo）
- 未開 PR
- 未攞對手 Reel 嘅實際數據（views / 爆款指數）—— vidIQ 只回咗畫面層

---

## 環境注意

- 呢個 repo 原本係 `daily-ai-news-radar`（Python 新聞 pipeline，喺 `scripts/`）。
  `reel-cutter/` 係新加嘅獨立子項目，**同 news pipeline 冇任何耦合**。
- `reel-cutter` 純標準庫，只依賴 `ffmpeg`（要 libass）。
- 字體自動偵測：本機 Mac 會揀 Noto Sans HK / PingFang HK，唔使配置。

---

# 三份 Session Brief（可獨立並行）

每份都係自足嘅 —— 開新 session 直接貼落去就跑得，唔使睇返呢個對話。

---

## 🎨 Session A — 素材生產

**貼呢段落新 session：**

> Repo `daily-ai-news-radar`，branch `claude/reel-commander-breakdown-dd7n9z`。
> 先讀 `reel-cutter/docs/script-ai-agent-3-levels-52s.md` 同 `reel-cutter/edl/ai-agent-3-levels-52s.json`。
>
> 我要為呢條 52.5 秒 Reel 生產全部畫面素材。分兩類：
>
> **(a) 五張圖表 — 出 text-to-image prompt（我自己去 Nanobanana / ChatGPT Image 跑）**
> - S3（7–10s）3 宮格：自己跑 Research／自己出 Post／自己入 CRM
> - S6（22–29s）四塊卡砌成方格：知識庫=Context／Skill=步驟／清晰目標=自主／API=做得到嘢
> - S8（36.5–39.5s）節點圖：中間一個人，外圍六個 Agent 節點連線
> - S9（39.5–44.5s）一分為二：左「人＝判斷」右「Agent＝串接」
> - S10（44.5–48s）三級樓梯：1X 執行者 → 10X 管理者 → 100X 建造者
>
> 要求：9:16 直度、深色底、高對比、**圖入面唔好放中文字**（字幕會另外燒上去，會撞）。
> 五張要同一套視覺語言（同色板、同線條粗度、同 icon 風格）。
>
> **(b) 六段錄屏 — 出 shot list（我自己錄）**
> S1 / S2 / S4 / S5 / S7 / S11。逐段講明錄咩畫面、幾多秒、鏡頭點郁、要 highlight 邊個位。
> 特別注意 S7（29–36.5s）係全片可信度支柱，要真錄屏連拍 5 步：
> prompt 輸入 → research 輸出 → Post 草稿 → Google Sheet 入行 → Mailchimp send，每步 1.5 秒。
>
> 出完寫入 `reel-cutter/docs/asset-brief.md`，commit push 返同一條 branch。

**驗收**：五個 prompt 可以直接貼去出圖；shot list 每段有秒數同具體操作步驟。

---

## 🎬 Session B — 錄音、出片、封面

**貼呢段落新 session：**

> Repo `daily-ai-news-radar`，branch `claude/reel-commander-breakdown-dd7n9z`。
> 先讀 `reel-cutter/README.md` 同 `reel-cutter/SKILL.md`。
>
> 素材已經放咗喺 `reel-cutter/media/`（VO：`vo.wav`，音樂：`music.mp3`，畫面：`s1_*.mov` 等，
> 檔名對返 EDL 嘅 `source` 欄）。幫我：
>
> 1. `python3 -m reel_cutter validate edl/ai-agent-3-levels-52s.json` — 確認零 warning
> 2. 用 whisper 對 `vo.wav` 出時間軸，**核對每段 VO 實際長度同 EDL 對唔對得上**；
>    對唔上就改 EDL 嘅 start/end（唔好改稿），改完重跑 validate
> 3. `render` 出片，`--preset slow --crf 18`
> 4. 用 ffmpeg 做 loudness normalise 到 **-14 LUFS**（IG 標準），出最終檔
> 5. 抽首幀做封面候選 3 個（0.3s / 3.5s / 37s），輸出 PNG
> 6. 檢查成品：52.5s、1080×1920、30fps、字幕冇被底部裁到
>
> 全部 commit push 返同一條 branch（成品 mp4 唔入 git，gitignore 已擋）。

**驗收**：一條可以直接上傳 IG 嘅 mp4 + 3 個封面候選。

---

## 📣 Session C — 分發、改編、漏斗

**貼呢段落新 session：**

> Repo `daily-ai-news-radar`，branch `claude/reel-commander-breakdown-dd7n9z`。
> 先讀 `reel-cutter/docs/script-ai-agent-3-levels-52s.md` 同
> `reel-cutter/docs/teardown-dotai-DbqHhNiCgV3.md`。
>
> 條 Reel 嘅內容要一稿多用。幫我出：
>
> 1. **IG Reel caption** — hook 第一行 + 內文 + CTA + hashtag。
>    CTA 用完整詞組 `我要 Agent 攻略`（**唔好用單字**，會被其他 post 留言誤觸）。
> 2. **ManyChat 設定** — trigger phrase、DM 第一句（要覆述佢留咗咩）、第二句先出 link、
>    以及一個 follow-up 訊息。
> 3. **IG carousel 7 頁** — 用 teardown 入面「三宗罪 → 四件事公式 → 三層階梯」拆。
>    每頁出標題 + 內文 + 視覺描述。
> 4. **跨平台改寫** — 同一內容改成 Threads 貼文、Facebook 貼文、YouTube Shorts 描述。
> 5. **Notion 存檔** — 將 teardown 寫入競品分析 DB。
>
> 可用 skill：`ig-carousel-generator`、`facebook-copywriter`、`video-post-optimizer`。
> 文字產出寫入 `reel-cutter/docs/distribution.md`，commit push 返同一條 branch。

**驗收**：caption + ManyChat 全套 + carousel 7 頁 + 3 個平台改寫版本。

---

## 三條 session 之間嘅依賴

```
Session A（素材）─┐
                  ├─→ Session B（出片）
       VO 錄音 ───┘

Session C（分發）── 完全獨立，可以即刻開，唔使等 A/B
```

- **A 同 C 可以同時開。** C 唔依賴任何素材。
- **B 要等 A 出完素材 + 你錄好 VO。**
- 三條都 push 同一條 branch，記住開工前 `git pull origin claude/reel-commander-breakdown-dd7n9z`。

---

## 未決事項（要 Anson 決定）

1. **開唔開 PR？** 呢個 session 冇開，branch 已 push。
2. **對手數據要唔要驗？** 跑 `vidiq_ig_profile_reels` 攞 Dot.ai 帳號 outlier multiplier，
   確認嗰條 89 秒片係咪真爆 —— 如果唔爆，成套模仿邏輯要重新檢視。
3. **`reel-cutter` 要唔要搬出 `daily-ai-news-radar`？** 兩者冇耦合，
   長遠放喺 skills-library 或者獨立 repo 會清爽啲。
