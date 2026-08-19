# skills-library — 美術總監升級包（方案 A）

> 對應報告：`reports/15_GitHub_Skills_美術總監全面調研報告.md`
> 打包日期：2026-08-19｜已按報告第 10 節安全清單審核源碼（純 Markdown，零 script／postinstall／外部 API）

## 內容

| 目錄 | 內容 | 來源 |
|---|---|---|
| `motion-design/` | LottieFiles Motion Design Skill 完整 vendor 版（SKILL.md + director/ + patterns/ + reference/ + LICENSE） | [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill) @ `f9a8a04`，MIT |
| `reference/video-shotcraft_抽錄.md` | video-shotcraft 鏡頭 recipe／SFX 方法論／美學規則精選抽錄（只做判斷參考庫，唔安裝原 repo） | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) @ `0d6f0b5`，Apache-2.0 |

## 喺部 Mac 執行嘅三步（方案 A）

```bash
# 1. 正式安裝 motion-design skill（用官方渠道裝，日後有得 update；
#    本目錄嘅 vendor 版係已審核快照，供離線比對／應急用）
npx skills add LottieFiles/motion-design-skill

# 2. 同步 HyperFrames skill 路由
#    ⚠️ 上游已將 graphic-overlays 併入 talking-head-recut，
#    並新增 product-launch-video / faceless-explainer 等 20 個 skill
npx hyperframes skills update

# 3. 將參考文檔放入 vault 俾美術總監 sub-agent 查閱
#    （pull 呢個 branch 之後）
cp skills-library/reference/video-shotcraft_抽錄.md \
   "<你嘅 vault 路徑>/🧠 brain/50_情報/"
```

第 2 步跑完後 diff 一次本機 skill 目錄，確認冇引入唔想要嘅新路由（例如 faceless-explainer 唔應該喺 talking-head 項目觸發）。

## 貼入美術總監 agent 定義嘅路由優先級

```text
合成路由（寫死，不可偏離）：
1. 本機 mc-* 模板有相符元件 → 必須重用
2. HyperFrames 可完成 → 用 HyperFrames（talking-head-recut / animation / keyframes）
3. 都唔得 → 先問 Anson，先至考慮 Remotion
判斷路由：
4. 「呢一拍應唔應該動／點樣動」→ 查 motion-design skill
   （timing/easing 表、emotion-mapping、choreography、quality checklist）
5. 「用邊種鏡頭／動作／SFX」→ 查 skills-library/reference/video-shotcraft_抽錄.md
   （只可查詢，嚴禁按佢嘅 Remotion 範式接管合成）
6. 一切新元件服從 13_美術總表_125x.md 嘅色彩／字型／安全區／進出場／留白
```

## 未做（等你決定）

- 方案 B（`remotion-dev/skills` + `av/remotion-bits`）：要先確認 Remotion 授權主體（≤3 員工免費）；remotion-bits 已停更 5 個月
- video-shotcraft 正式安裝（方案 C）：暫時只抽錄，唔裝
