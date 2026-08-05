---
name: reel-cutter
description: >
  🎬 剪片員工 — 由一個 EDL JSON 出 9:16 Reel 成品，廣東話字幕燒入，唔使開 Filmora。
  先驗語速（units/秒）確保讀得切，再出 animatic 零素材預覽節奏，最後補真素材出片。
  觸發：「剪條 Reel」「出 animatic」「驗下條稿讀唔讀得切」「燒字幕」「reel-cutter」
  「幫我砌條 52 秒片」「EDL 出片」「呢條稿排時間軸」。
  需要：Bash（ffmpeg + Python 3.9+）。唔需要任何 pip 依賴。
---

# reel-cutter

## 幾時用

- Anson 寫完短片稿，想知**讀唔讀得切**、邊段趕
- 想喺**開機拍之前**先聽一次節奏（animatic）
- 已經有 VO / 錄屏素材，要出一條字幕燒好嘅 9:16 成品
- 要一份 SRT（轉用途：YouTube Shorts / Threads / 字幕翻譯）

唔好用嚟：需要動態轉場、色調分級、多軌合成嘅片 — 嗰啲仲係開 Filmora。

## 位置

`reel-cutter/`（此 repo）。所有指令喺該目錄下跑。

## 流程

### 1. 有稿冇 EDL → 先寫 EDL

用 `edl/ai-agent-3-levels-52s.json` 做模板。每段填：
`id / start / end / beat / vo / sub / sub_style / shot / source / sfx`

段落切法：**一個意思一段**，3–8 秒。要一段拆幾個鏡就拆多幾段。

### 2. 驗

```bash
python3 -m reel_cutter validate edl/<name>.json
```

見到 `!` 就係語速出界。> 6.8 units/s 要剪字，< 3.0 要收時間。
**改到零 warning 至好去下一步** — 呢一步慳返成日錄音重錄。

### 3. Animatic（零素材）

```bash
python3 -m reel_cutter animatic edl/<name>.json -o out/animatic.mp4
```

出一條有字幕、有 slate（段號 / beat / 拍咩）嘅計時預覽。
畀 Anson 睇：節奏散唔散、hook 夠唔夠早、CTA 夠唔夠時間。

### 4. 補素材 → 出片

素材放 `media/`，檔名對返 EDL 嘅 `source`。補幾多用幾多。

```bash
python3 -m reel_cutter render edl/<name>.json -o out/reel.mp4
# 最終版
python3 -m reel_cutter render edl/<name>.json -o out/reel.mp4 --preset slow --crf 18
```

## 硬規矩

1. **字幕一定燒入。** IG 自動字幕認唔到廣東話，會出錯字。
2. **CTA 用完整詞組，唔用單字。** ManyChat trigger 例如 `我要 Agent 攻略`，
   唔好用 `100X` 呢類單 keyword — 會被其他 post 留言誤觸，亦冇上下文。
3. **底部字幕 margin_v ≥ 300px**，避開 IG 嘅 caption / UI 遮擋。
4. **Hook 用置中大字（`sub_style: "hook"`）**，7 秒後先轉底部字幕條。
5. **可信度段落用真錄屏**，唔好用 mockup。

## 改嘢改邊度

| 想改 | 改邊度 |
|---|---|
| 字幕大細 / 位置 / 描邊 | EDL `style` |
| 字體 | EDL `style.font`（`null` = 自動偵測） |
| 音樂音量 / ducking | EDL `audio.music_gain_db` / `duck_db` |
| 語速容忍範圍 | `reel_cutter/edl.py` 頂部三個常數 |
| 字體偵測次序 | `reel_cutter/fonts.py` 嘅 `PREFERRED` |
| ffmpeg 參數 | `reel_cutter/render.py` 嘅 `build_command` |

## 驗收

```bash
python3 -m unittest discover -s tests   # 22 個測試
```

含回歸測試：shipped 嘅 52 秒稿改到語速超標會即刻紅。

## Lessons

- 2026-08-05：初版。對手 Reel（Dot.ai `DbqHhNiCgV3`, 89 秒）拆解後定型，
  確認全硬切 + 逐字燒入字幕係呢個 niche 嘅基準做法，所以工具刻意唔做轉場特效。
- 素材長度同 EDL 對唔上係常態。`tpad` hold 尾格 + `trim` 裁到準秒，
  所以「素材短咗少少」唔會令成條片走位 —— 唔好靠手動對齊。
