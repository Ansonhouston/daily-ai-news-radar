# reel-cutter

EDL 驅動嘅 9:16 Reel 剪片 agent — 由一個 JSON 出成品，字幕燒入，唔使開 Filmora。

專為 @AIeasyjob 嘅廣東話短片而寫：先驗語速，後出 animatic 睇節奏，最後補真素材出片。

## 點解要有呢樣嘢

寫完稿唔知讀唔讀得切、剪完先發覺節奏散、每次改一句要重排整條 timeline。
reel-cutter 將「稿 + 時間軸 + 字幕 + 素材」全部收埋喺一個 EDL JSON，
改一個數字重跑一次就得。

## 依賴

- Python 3.9+（純標準庫，冇 pip 依賴）
- `ffmpeg`（要有 libass）— macOS `brew install ffmpeg`
- 一隻繁中字體。自動偵測次序：Noto Sans HK → Noto Sans CJK HK → Noto Sans TC
  → Source Han Sans → PingFang HK → 微軟正黑 → WenQuanYi Zen Hei。
  想指定就喺 EDL 寫 `style.font`。

## 四條指令

```bash
cd reel-cutter

# 1. 驗稿：時間軸有冇窿、每段語速讀唔讀得切、邊幾段仲欠素材
python3 -m reel_cutter validate edl/ai-agent-3-levels-52s.json

# 2. 出字幕檔（.ass 燒入用；--srt 出一份 VO 逐字稿俾 Filmora / 轉用途）
python3 -m reel_cutter subs edl/ai-agent-3-levels-52s.json -o out/subs.ass --srt out/vo.srt

# 3. Animatic：零素材都出到一條有字幕有 slate 嘅計時預覽，開機前先聽節奏
python3 -m reel_cutter animatic edl/ai-agent-3-levels-52s.json -o out/animatic.mp4

# 4. 出片：有幾多段素材就用幾多段，未拍嘅自動用 slate 頂住
python3 -m reel_cutter render edl/ai-agent-3-levels-52s.json -o out/reel.mp4
```

`--dry-run` 印 ffmpeg 指令唔執行，`--verbose` 睇 ffmpeg 實時輸出。

## 建議工作流

1. 寫 EDL（或改現成嗰個）→ `validate` 直到零 pacing warning
2. `animatic` → 睇一次，聽節奏。此時**一格素材都未拍**
3. 錄 VO 放 `media/vo.wav` → 再 `animatic`，確認每句對得上畫面
4. 逐段補素材落 `media/` → `render`。補幾多用幾多，唔使一次過齊
5. 全齊 → `render --preset slow --crf 18` 出最終版

## EDL 格式

```jsonc
{
  "title": "…",
  "resolution": [1080, 1920],
  "fps": 30,
  "style": {
    "font": null,            // null = 自動偵測
    "body_size": 68,         // 底部字幕，px @ 1920 高
    "hook_size": 108,        // 置中大字
    "outline": 6,            // 黑描邊粗度
    "body_margin_v": 320,    // 避開 IG 底部 UI
    "side_margin": 90
  },
  "audio": {
    "vo": "media/vo.wav",
    "music": "media/music.mp3",
    "music_gain_db": -19,    // 音樂底噪
    "duck_db": -6            // 有 VO 時額外壓低
  },
  "end_card": { "start": 50.5, "end": 52.5, "text": "第一行\n第二行" },
  "segments": [
    {
      "id": "S1",
      "start": 0.0, "end": 4.0,
      "beat": "呢段做咩",           // animatic slate 會顯示
      "vo":   "旁白逐字",            // 用嚟計語速 + 出 SRT
      "sub":  "燒入字幕\n可以換行",
      "sub_style": "hook",          // "hook" 置中大字 / "body" 底部
      "shot": "拍咩",                // animatic slate 會顯示
      "source": "media/s1.mov",     // 唔存在就自動變 slate
      "in": 0.0,                    // 由素材第幾秒開始攞
      "sfx": "音效備註"
    }
  ]
}
```

規則：

- segments 必須**連續無縫**（上一段 `end` = 下一段 `start`），有窿或者重疊會即刻報錯
- `end_card` 必須喺最後一段之後
- 素材長度唔夠會自動 hold 尾格補足，長度多咗會裁走 — 出嚟一定啱秒數
- 任何比例嘅素材都會 `force_original_aspect_ratio=increase` + 中央裁成 9:16

## 語速檢查

`validate` 用「units／秒」量度。一個 unit = 一個中文字，或者一串連續英文／數字。

| 範圍 | 判斷 |
|---|---|
| < 3.0 | 太慢，收緊時間或者加句 |
| 3.0 – 6.8 | 讀得舒服 |
| > 6.8 | 趕，會出事 — 剪字或者加時間 |

## 測試

```bash
python3 -m unittest discover -s tests
```

包一個回歸測試：`edl/ai-agent-3-levels-52s.json` 改到語速超標會即刻紅。

## 已知限制

- 段內冇 sub-cut：一段 = 一個素材。要一段拆幾個鏡就拆做幾個 segment
- 冇轉場特效（純硬切）。呢個係刻意 — 參考爆款片本身就係全硬切
- 音樂 ducking 用固定 gain，唔係 sidechain 動態壓縮
- 未做 loudness normalise，出片前自己過一次 -14 LUFS
