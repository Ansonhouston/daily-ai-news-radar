"""
clusterer.py — 用 Claude 做語意聚類 + 揀 Top 5
============================================
中英分開排：將中/英文章 list 交畀 Claude，由佢做語意 cluster、
按「被幾多個來源報導」+「重要性」排序，揀出最 HIT 嘅 Top N。

返 Top 5 list，每條包含：
- source（原來嘅媒體）
- title（原文標題）
- title_zh（繁體中文翻譯，只用喺英文 list）
- link
- pub_hkt / pub_et
- cluster_size（幾多個來源報同樣話題）
- explanation（約 100 字香港廣東話書面語解釋，專業術語括號保留英文）

另外亦會 return「今日重點」150 字 summary。
"""

from __future__ import annotations
import json
import logging
from typing import List, Dict, Tuple

import config

log = logging.getLogger(__name__)

# ─────────────────────────────────────────────
# Prompts
# ─────────────────────────────────────────────

SYSTEM_PROMPT_BASE = """你係 Anson 個 AI 新聞編輯兼資深科技記者，負責幫佢每朝睇晒今日 AI 圈嘅新聞，揀出最 HIT 嘅內容，再寫成深入嘅分析卡。

語言要求（NON-NEGOTIABLE）：
- 全部用「香港廣東話書面語」（唔係普通話書面語，唔係純口語）
- 例：用「呢個」唔用「這個」；用「啲」、「嚟」、「咗」、「喺」、「畀」、「點解」、「即係」、「而家」
- 但保持書面感，專業、清晰，避免太過口語化
- 專業術語括號保留英文原文，例：「大型語言模型（LLM）」、「智能體（Agent）」
- 所有中文一律繁體

你嘅任務：
1. 將相近話題嘅文章 cluster 埋一齊
2. 按「被幾多個【唔同來源】報導」+「重要性／突破性」排序
3. 揀出 Top N 個 cluster，每個揀一條最權威/最完整嘅代表文章
4. 每條寫成一張【深入分析卡】，包含：新標題、原來標題、文章摘要、三個關鍵詞、總括分析（詳見輸出格式）
5. 寫一段約 150 字嘅「今日重點」總結，分段（段與段之間空一行）

每張分析卡嘅內容要求：
- new_title（新標題）：你改寫嘅一句清晰、精準、有資訊量嘅繁體中文標題（去除原標題嘅標題黨味，保留重點）
- original_title（原來標題）：原文標題原樣（英文新聞保留英文原文；中文新聞用繁體）
- summary（文章摘要）：2-3 段廣東話書面語，每段之間用 \\n\\n 分隔，講清楚件事嘅來龍去脈、背景同細節（總共約 150-200 字）
- keywords（三個關鍵詞）：揀 3 個同呢單新聞相關嘅專業詞，每個有 term（中文詞）、en（英文原文/縮寫）、explain（一句廣東話書面語解釋）
- analysis（總括分析）：1 段約 80-120 字廣東話書面語，分析件事嘅意義、影響、或者對行業/觀眾嘅啟示

⚠️ cluster_size 定義：有幾多個【唔同來源】報同一話題（唔係文章數）。RSS 每語言最多 2 個媒體，X 最多睇幾多個唔同帳號。
"""

CLUSTER_USER_PROMPT_TEMPLATE = """以下係今日（HKT）抓返嚟嘅 {lang_label}，共 {count} 條。

請：語意 cluster → 按來源數+重要性排序 → 揀 Top {top_n} → 每條寫深入分析卡 → 出 150 字「今日重點」。

{source_instruction}

原始資料（JSON）：
```json
{articles_json}
```

請**只** return 以下 JSON（唔好 wrap markdown code block，唔好加任何 prefix/suffix）：

{{
  "today_summary": "（約 150 字廣東話書面語總結，分段，段之間用 \\n\\n）",
  "top_clusters": [
    {{
      "rank": 1,
      "source": "（代表文章來源{source_label}）",
      "new_title": "（你改寫嘅清晰繁體中文新標題）",
      "original_title": "（原文標題；英文新聞保留英文）",
      "link": "（代表文章連結）",
      "pub_hkt": "（pub_hkt ISO 時間）",
      "pub_et": "（pub_et ISO 時間{pub_et_note}）",
      "cluster_size": 1,
      "summary": "（2-3 段廣東話書面語摘要，段之間用 \\n\\n）",
      "keywords": [
        {{"term": "（中文詞）", "en": "（英文原文/縮寫）", "explain": "（一句廣東話解釋）"}},
        {{"term": "...", "en": "...", "explain": "..."}},
        {{"term": "...", "en": "...", "explain": "..."}}
      ],
      "analysis": "（約 80-120 字廣東話書面語總括分析）"
    }}
  ]
}}
"""


def _build_user_prompt(articles: List[Dict], lang: str, top_n: int) -> str:
    is_english = lang == "english"
    is_x = lang == "x"

    if is_x:
        lang_label = "X（Twitter）AI 頂級帳號嘅 tweet"
        source_instruction = (
            "呢批係 X 上 AI 大佬／官方帳號嘅英文 tweet：\n"
            "- source 用帳號 handle（例如 @OpenAI）\n"
            "- original_title 用 tweet 原文（英文）；new_title 用你改寫嘅繁體中文標題\n"
            "- cluster_size = 有幾多個【唔同帳號】講同一話題\n"
            "- 排序睇重要性 + engagement（資料有 engagement 數）"
        )
        source_label = "帳號 handle"
        pub_et_note = ""
    elif is_english:
        lang_label = "英文 AI 新聞"
        source_instruction = (
            "呢批係英文新聞：original_title 保留英文原文；new_title 用繁體中文改寫。"
        )
        source_label = "媒體名"
        pub_et_note = ""
    else:
        lang_label = "中文 AI 新聞"
        source_instruction = (
            "呢批係中文新聞：original_title 同 new_title 都用繁體中文。pub_et 可以填空字串。"
        )
        source_label = "媒體名"
        pub_et_note = "，中文新聞可以填空字串"

    articles_json = json.dumps(articles, ensure_ascii=False, indent=2)

    return CLUSTER_USER_PROMPT_TEMPLATE.format(
        lang_label=lang_label,
        count=len(articles),
        top_n=top_n,
        source_instruction=source_instruction,
        source_label=source_label,
        pub_et_note=pub_et_note,
        articles_json=articles_json,
    )


# ─────────────────────────────────────────────
# LLM provider abstraction
# ─────────────────────────────────────────────
# 由 config.LLM_PROVIDER 控制（gemini / claude / deepseek / openai）。
# 預設 gemini（免費 tier）。如果 primary provider 出事，會自動 fallback
# 去 config.LLM_FALLBACK_PROVIDER（如有設）。

def _call_gemini(user_prompt: str) -> str:
    """Google Gemini（免費 tier）。用新 google-genai SDK。"""
    if not config.GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY 未設定（檢查 config/.env）")
    from google import genai
    from google.genai import types
    client = genai.Client(api_key=config.GEMINI_API_KEY)
    cfg_kwargs = dict(
        system_instruction=SYSTEM_PROMPT_BASE,
        temperature=0.4,
        max_output_tokens=config.LLM_MAX_TOKENS,
        response_mime_type="application/json",  # 強制 JSON output
    )
    # gemini-2.5-* 預設開 thinking 會慢好多；關咗加速（once-daily job 唔需要 deep thinking）
    if "2.5" in config.GEMINI_MODEL:
        try:
            cfg_kwargs["thinking_config"] = types.ThinkingConfig(thinking_budget=0)
        except Exception:
            pass
    resp = client.models.generate_content(
        model=config.GEMINI_MODEL,
        contents=user_prompt,
        config=types.GenerateContentConfig(**cfg_kwargs),
    )
    return resp.text


def _call_claude(user_prompt: str) -> str:
    if not config.ANTHROPIC_API_KEY:
        raise RuntimeError("ANTHROPIC_API_KEY 未設定（檢查 config/.env）")
    from anthropic import Anthropic
    client = Anthropic(api_key=config.ANTHROPIC_API_KEY)
    resp = client.messages.create(
        model=config.CLAUDE_MODEL,
        max_tokens=config.LLM_MAX_TOKENS,
        system=SYSTEM_PROMPT_BASE,
        messages=[{"role": "user", "content": user_prompt}],
    )
    parts = []
    for block in resp.content:
        if hasattr(block, "text"):
            parts.append(block.text)
    return "".join(parts)


def _call_openai_compatible(user_prompt: str, api_key: str, base_url: str, model: str) -> str:
    """OpenAI / DeepSeek（OpenAI-compatible endpoint）。"""
    if not api_key:
        raise RuntimeError(f"{model} API key 未設定（檢查 config/.env）")
    from openai import OpenAI
    client = OpenAI(api_key=api_key, base_url=base_url)
    resp = client.chat.completions.create(
        model=model,
        max_tokens=config.LLM_MAX_TOKENS,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_BASE},
            {"role": "user", "content": user_prompt},
        ],
        response_format={"type": "json_object"},
    )
    return resp.choices[0].message.content


def _call_provider(provider: str, user_prompt: str) -> str:
    """根據 provider 名 dispatch。"""
    provider = provider.lower()
    if provider == "gemini":
        return _call_gemini(user_prompt)
    if provider == "claude":
        return _call_claude(user_prompt)
    if provider == "deepseek":
        return _call_openai_compatible(
            user_prompt, config.DEEPSEEK_API_KEY,
            "https://api.deepseek.com", config.DEEPSEEK_MODEL,
        )
    if provider == "openai":
        return _call_openai_compatible(
            user_prompt, config.OPENAI_API_KEY,
            "https://api.openai.com/v1", config.OPENAI_MODEL,
        )
    raise ValueError(f"未知 LLM_PROVIDER: {provider}")


def _call_llm(user_prompt: str) -> str:
    """主入口：primary provider，失敗 fallback。"""
    primary = config.LLM_PROVIDER
    try:
        log.info(f"[llm] 用 primary provider: {primary}")
        return _call_provider(primary, user_prompt)
    except Exception as e:
        log.error(f"[llm] primary ({primary}) 失敗: {e}")
        fallback = getattr(config, "LLM_FALLBACK_PROVIDER", "")
        if fallback and fallback.lower() != primary.lower():
            log.warning(f"[llm] 嘗試 fallback provider: {fallback}")
            return _call_provider(fallback, user_prompt)
        raise


def _safe_parse_json(text: str) -> Dict:
    """Claude 可能會包 markdown code block，try clean。"""
    text = text.strip()
    if text.startswith("```"):
        # strip ```json ... ``` 或 ``` ... ```
        lines = text.split("\n")
        # 去頭尾 fence
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    return json.loads(text)


def cluster_and_rank(articles_by_lang: Dict[str, List[Dict]]) -> Dict:
    """
    Input: {"english": [...], "chinese": [...]}
    Output: {
      "english": {"today_summary": "...", "top_clusters": [...]},
      "chinese": {"today_summary": "...", "top_clusters": [...]}
    }
    """
    result = {}
    plan = [("english", config.TOP_N_ENGLISH), ("chinese", config.TOP_N_CHINESE)]
    if articles_by_lang.get("x"):
        plan.append(("x", config.TOP_N_X))
    for lang, top_n in plan:
        articles = articles_by_lang.get(lang, [])
        if not articles:
            log.warning(f"[cluster] {lang} 0 條文章，skip")
            result[lang] = {"today_summary": "", "top_clusters": []}
            continue

        log.info(f"[cluster] {lang}: {len(articles)} 條 → Top {top_n}")
        prompt = _build_user_prompt(articles, lang, top_n)
        raw = _call_llm(prompt)
        if config.DEBUG:
            log.debug(f"[cluster] {lang} raw Claude response:\n{raw[:1000]}")
        try:
            parsed = _safe_parse_json(raw)
        except json.JSONDecodeError as e:
            log.error(f"[cluster] {lang} JSON parse 失敗: {e}\nraw:\n{raw}")
            parsed = {"today_summary": "(語意聚類失敗，請查 log)", "top_clusters": []}

        # ─── 防呆：clamp cluster_size 到實際來源數（Gemini 有時當成文章數）
        if lang == "x":
            max_sources = len(config.X_HANDLES) or 10
        else:
            max_sources = len(config.RSS_SOURCES.get(lang, [])) or 2
        for c in parsed.get("top_clusters", []):
            try:
                cs = int(c.get("cluster_size", 1))
            except (ValueError, TypeError):
                cs = 1
            c["cluster_size"] = max(1, min(cs, max_sources))

        result[lang] = parsed

    return result
