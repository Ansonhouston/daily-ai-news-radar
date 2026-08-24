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
| Facebook Group | [`facebook-group-short.md`](./facebook-group-short.md) | 中英雙語 · 朋友向精簡版（約 300 字）· 冇 hashtag / 冇 CTA 漏斗 |

## 產出方法

1. 讀 YouTube transcript（廣東話原片）抽事實 → 建立唯一事實來源
2. 載入 `facebook-copywriter` skill（Mode D 跨平台改寫）
3. 3 個 sub agent 並行：LinkedIn / Facebook / Instagram，各自跟平台演算法規則寫中英雙語

## 全包共用規則

- **反作料**：所有數字只可以來自原片 —— 20 倍效率、62K views（Facebook）、outlier 門檻 5x 起 / 收窄到 10x、12 條對照片、1700 萬 views（外部對照片）、片長 9:45
- **誠實 caveat 必須保留**：生產線只證明「系統生產得出一條片」，唔證明「生產線令條片爆」
- **Brand voice**：健吾式中立旁觀者，🚫 唔講「最強 / 全網第一」
- **ManyChat trigger 必須完整 phrase**，配 3 條 reply rotation

## ⚠️ 出街前要 Anson 確認（三個平台共通）

1. **🔴 留言 trigger 字眼（最關鍵）** —— 片尾 CTA 嗰段 ASR 聽唔清，FB / IG 文案暫用完整 phrase「我想睇總指揮」／「I WANT THE ORCHESTRATOR」做 placeholder。出街前一定要對返條片實際口播，caption、Story CTA、ManyChat trigger 三個位要同步改（建議兩句都加入 ManyChat trigger list 做保險）。
2. **62K 嘅平台同時間點** —— 文案寫「喺 Facebook 跑到 62K views」。若果係跨平台合計，或者條數仲喺度升，要改講法／加「截至目前」。
3. **ManyChat 派發物** —— 暫時只派長片連結 + 下一集 waitlist，冇作任何 PDF / Notion / .skill。有實物派就要改 delivery DM。
4. **工具名** —— transcript 冇提供實際用邊個 agent / 影片生成平台，全文用泛指。想寫實就要 Anson 補。
5. **IG link in bio 目的地** —— 現時假設指去 YouTube 條片；若導去 landing page 要改 Story link sticker + caption 尾句。
6. **LinkedIn 用語** —— 中文版「總指揮」要唔要統一寫 orchestrator。
7. **發佈時間** —— 跟返片入面講嘅原則：內容同出街時間都要由人批，文案冇代定。

## 各平台規格對照

| | LinkedIn | Facebook | Instagram |
|---|---|---|---|
| 首行截斷 | ~210 字元 | ~125 字元 | ~125 字元 |
| Hashtag | 3-5 | 3-5 | 8-15 |
| 連結策略 | 第一條留言（另備正文版） | 第一條留言（另備正文版） | link in bio / DM 派發 |
| CTA 主軸 | 驅討論留言 | 驅留言 + 分享 + DM | 驅 save + share + DM |
| 額外格式 | — | ManyChat 漏斗版 | Carousel 10 版大綱 + 4 版 Story |
