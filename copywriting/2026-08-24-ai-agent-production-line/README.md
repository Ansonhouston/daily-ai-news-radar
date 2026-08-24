# 跨平台文案包｜20X AI Agent 短片生產線（2026-08-24）

來源影片：《20X AI Agent 短片生產線 砌 62K Views 爆款 Reel，一人公司由情報採樣到出帖全紀錄公開，唔識砌 AI Agent 生產線創作者，2026 年會愈嚟愈忙》
- 連結：https://youtu.be/coMEPFqh-bA
- 頻道：AI Easy Job・廣東話 AI 實測
- 片長：約 9 分 45 秒

## 檔案

| 平台 | 檔案 | 內容 |
|---|---|---|
| LinkedIn | [`linkedin.md`](./linkedin.md) | 中英雙語 · Hook 3 選 1 · 連結放留言版 + 正文版 |
| Facebook | [`facebook.md`](./facebook.md) | 中英雙語 · Hook 3 選 1 · 連結放留言版 + 正文版 + ManyChat 漏斗版 |
| Instagram | [`instagram.md`](./instagram.md) | 中英雙語 · Reel caption / Carousel caption + slide 大綱 / Story · ManyChat |

## 產出方法

1. 讀 YouTube transcript（廣東話原片）抽事實 → 建立唯一事實來源
2. 載入 `facebook-copywriter` skill（Mode D 跨平台改寫）
3. 3 個 sub agent 並行：LinkedIn / Facebook / Instagram，各自跟平台演算法規則寫中英雙語

## 全包共用規則

- **反作料**：所有數字只可以來自原片 —— 20 倍效率、62K views（Facebook）、outlier 門檻 5x 起 / 收窄到 10x、12 條對照片、1700 萬 views（外部對照片）、片長 9:45
- **誠實 caveat 必須保留**：生產線只證明「系統生產得出一條片」，唔證明「生產線令條片爆」
- **Brand voice**：健吾式中立旁觀者，🚫 唔講「最強 / 全網第一」
- **ManyChat trigger 必須完整 phrase**，配 3 條 reply rotation

## ⚠️ 出街前要 Anson 確認

- 片尾實際嘅留言 trigger 字眼（transcript ASR 唔清晰，文案暫用完整 phrase 佔位）
- 62K 係 Facebook 嘅數，各平台文案要唔要註明平台
- LinkedIn 中文版「總指揮」要唔要統一寫 orchestrator
