"""
notion_archive.py — Notion archive 每日報告
===========================================
將每日報告寫入 Notion database「📰 新聞 Archive」。
每日一個 page，標題 = 日期，content = 完整訊息。
"""

from __future__ import annotations
import logging
import requests
from typing import Dict, List

import config

log = logging.getLogger(__name__)

NOTION_API = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"


def _headers():
    return {
        "Authorization": f"Bearer {config.NOTION_API_TOKEN}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def _text_block(text: str, bold: bool = False) -> Dict:
    """Notion paragraph block。長文要 split。"""
    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "type": "text",
                "text": {"content": text[:2000]},  # Notion rich_text 單個 chunk 上限 2000
                "annotations": {"bold": bold},
            }] if text else [],
        }
    }


def _heading_block(text: str, level: int = 2) -> Dict:
    return {
        "object": "block",
        "type": f"heading_{level}",
        f"heading_{level}": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
        }
    }


def _divider_block() -> Dict:
    return {"object": "block", "type": "divider", "divider": {}}


def _bookmark_block(url: str) -> Dict:
    return {"object": "block", "type": "bookmark", "bookmark": {"url": url}}


def _callout_block(text: str, emoji: str = "💡", color: str = "gray_background") -> Dict:
    """Notion callout（彩色框）block。"""
    return {
        "object": "block",
        "type": "callout",
        "callout": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
            "icon": {"emoji": emoji},
            "color": color,
        }
    }


def _build_blocks(clusters: Dict, today_date_str: str) -> List[Dict]:
    """構建 Notion blocks，靚 layout。"""
    blocks: List[Dict] = []

    # Header
    blocks.append(_heading_block(f"🌅 AI 日報 · {today_date_str}", level=1))

    # 🆕 狀態列 banner（dashboard，一眼睇晒今日狀態）
    _en = len(clusters.get("english", {}).get("top_clusters", []))
    _zh = len(clusters.get("chinese", {}).get("top_clusters", []))
    _x = len(clusters.get("x", {}).get("top_clusters", []))
    blocks.append(_callout_block(
        f"{today_date_str}　｜　📊 英 {_en} · 中 {_zh} · X {_x}　｜　🎨 9 圖：待 combine 生成　｜　🤖 每日 23:59 自動更新",
        emoji="📅", color="gray_background"))

    # 今日重點
    today_summary_zh = clusters.get("chinese", {}).get("today_summary", "") \
        or clusters.get("english", {}).get("today_summary", "")

    # 🆕 今日一句（取今日重點第一句做一眼主線）
    if today_summary_zh:
        _one_liner = today_summary_zh.strip().replace("\n", " ").split("。")[0].strip()
        if _one_liner:
            blocks.append(_callout_block(f"今日一句｜{_one_liner}。", emoji="🔥", color="yellow_background"))

    blocks.append(_heading_block("📌 今日重點", level=2))
    # 分段
    for para in today_summary_zh.split("\n\n"):
        para = para.strip()
        if para:
            blocks.append(_text_block(para))

    # 英文 Top
    en_clusters = clusters.get("english", {}).get("top_clusters", [])
    if en_clusters:
        blocks.append(_divider_block())
        blocks.append(_heading_block(f"🇺🇸 英文 Top {len(en_clusters)}", level=2))
        for c in en_clusters:
            blocks.extend(_card_blocks(c, kind="english"))

    # 中文 Top
    zh_clusters = clusters.get("chinese", {}).get("top_clusters", [])
    if zh_clusters:
        blocks.append(_divider_block())
        blocks.append(_heading_block(f"🇨🇳 中文 Top {len(zh_clusters)}", level=2))
        for c in zh_clusters:
            blocks.extend(_card_blocks(c, kind="chinese"))

    # X（Twitter）熱話
    x_clusters = clusters.get("x", {}).get("top_clusters", [])
    if x_clusters:
        blocks.append(_divider_block())
        blocks.append(_heading_block(f"🐦 X 熱話 Top {len(x_clusters)}", level=2))
        for c in x_clusters:
            blocks.extend(_card_blocks(c, kind="x"))

    blocks.append(_divider_block())
    blocks.append(_text_block("🤖 每日自動更新 · 23:59 HKT · daily-ai-news-radar"))

    return blocks


def _bulleted_block(text: str) -> Dict:
    return {
        "object": "block",
        "type": "bulleted_list_item",
        "bulleted_list_item": {
            "rich_text": [{"type": "text", "text": {"content": text[:2000]}}],
        }
    }


def _card_blocks(c: Dict, kind: str) -> List[Dict]:
    """一張深入分析卡 → Notion blocks。"""
    out: List[Dict] = []
    rank = c.get("rank", "?")
    source = c.get("source", "")
    cluster_size = c.get("cluster_size", 1)
    mention_word = "帳號討論" if kind == "x" else "來源提及"
    mention = f" · {cluster_size} 個{mention_word}" if cluster_size > 1 else ""

    out.append(_heading_block(f"{rank}. 【{source}】{mention}", level=3))
    # 新標題（粗體）
    out.append(_text_block(f"📰 {c.get('new_title','')}", bold=True))
    # 原來標題
    if c.get("original_title"):
        out.append(_text_block(f"原來標題：{c.get('original_title','')}"))
    # 連結
    if c.get("link"):
        out.append(_bookmark_block(c["link"]))
    # 摘要（分段）
    summary = c.get("summary", c.get("explanation", ""))
    if summary:
        out.append(_text_block("📝 文章摘要", bold=True))
        for para in summary.split("\n\n"):
            para = para.strip()
            if para:
                out.append(_text_block(para))
    # 三個關鍵詞
    keywords = c.get("keywords", [])
    if keywords:
        out.append(_text_block("🔑 三個關鍵詞", bold=True))
        for kw in keywords[:3]:
            term = kw.get("term", "")
            en = kw.get("en", "")
            explain = kw.get("explain", "")
            head = f"{term}（{en}）" if en else term
            out.append(_bulleted_block(f"{head}：{explain}"))
    # 總括分析
    if c.get("analysis"):
        out.append(_text_block("🧭 總括分析", bold=True))
        out.append(_text_block(c.get("analysis", "")))
    return out


def archive_to_notion(clusters: Dict, today_date_str: str, raw_message: str = "") -> str | None:
    """
    建立一個 Notion page 入 database。
    Return 新 page 嘅 ID（成功），或 None（失敗 / DRY_RUN）。
    """
    if config.DRY_RUN:
        log.info("[notion] DRY_RUN — 跳過 archive")
        return None

    if not config.NOTION_API_TOKEN or not config.NOTION_DATABASE_ID:
        log.error("[notion] NOTION_API_TOKEN / NOTION_DATABASE_ID 未設定")
        return None

    # ─── Notion 上限：children blocks per request 100 個
    blocks = _build_blocks(clusters, today_date_str)
    initial_children = blocks[:100]
    remaining = blocks[100:]

    # ─── 先 detect database schema 嘅 title property 名（防止寫死「Name」唔啱）
    title_prop = _get_title_property_name()

    en_count = len(clusters.get("english", {}).get("top_clusters", []))
    zh_count = len(clusters.get("chinese", {}).get("top_clusters", []))

    payload = {
        "parent": {"database_id": config.NOTION_DATABASE_ID},
        "properties": {
            title_prop: {
                "title": [{"text": {"content": f"AI 日報 · {today_date_str}"}}]
            },
        },
        "icon": {"emoji": "🌅"},
        "children": initial_children,
    }

    try:
        resp = requests.post(
            f"{NOTION_API}/pages",
            headers=_headers(),
            json=payload,
            timeout=30,
        )
        if resp.status_code >= 300:
            log.error(f"[notion] create page 失敗 {resp.status_code}: {resp.text}")
            return None
        page_id = resp.json().get("id")
        log.info(f"[notion] ✅ archive 成功 page_id={page_id}")

        # 補做剩低 blocks
        while remaining:
            chunk = remaining[:100]
            remaining = remaining[100:]
            requests.patch(
                f"{NOTION_API}/blocks/{page_id}/children",
                headers=_headers(),
                json={"children": chunk},
                timeout=30,
            )

        # 嘗試 set 額外 properties（如果 schema 有對應 column）
        today_summary = (clusters.get("chinese", {}).get("today_summary", "")
                         or clusters.get("english", {}).get("today_summary", ""))
        _maybe_set_extra_properties(page_id, en_count, zh_count, today_date_str, today_summary)

        return page_id
    except Exception as e:
        log.error(f"[notion] archive exception: {e}")
        return None


def _get_title_property_name() -> str:
    """Notion database 嘅 title column 名可以唔係「Name」。動態 detect。"""
    try:
        resp = requests.get(
            f"{NOTION_API}/databases/{config.NOTION_DATABASE_ID}",
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code == 200:
            props = resp.json().get("properties", {})
            for name, meta in props.items():
                if meta.get("type") == "title":
                    return name
    except Exception as e:
        log.warning(f"[notion] detect title prop 失敗: {e}")
    return "Name"


def _maybe_set_extra_properties(page_id: str, en_count: int, zh_count: int,
                                date_str: str, today_summary: str = ""):
    """如果 database 有 Date / 英文條數 / 中文條數 / 今日重點 / 推送狀態 column，set 落去。可選。"""
    try:
        resp = requests.get(
            f"{NOTION_API}/databases/{config.NOTION_DATABASE_ID}",
            headers=_headers(),
            timeout=30,
        )
        if resp.status_code != 200:
            return
        schema = resp.json().get("properties", {})
        props = {}
        # date_str 可能係 "2026-05-20" 或 "2026-05-20 [🧪 測試]"，net date 部分
        date_only = date_str.split(" ")[0] if date_str else date_str
        if "日期" in schema and schema["日期"].get("type") == "date":
            props["日期"] = {"date": {"start": date_only}}
        if "英文條數" in schema and schema["英文條數"].get("type") == "number":
            props["英文條數"] = {"number": en_count}
        if "中文條數" in schema and schema["中文條數"].get("type") == "number":
            props["中文條數"] = {"number": zh_count}
        # 今日重點 summary 寫埋落欄位（Notion rich_text 單 chunk 上限 2000）
        if today_summary and "今日重點" in schema and schema["今日重點"].get("type") == "rich_text":
            props["今日重點"] = {"rich_text": [{"text": {"content": today_summary[:2000]}}]}
        # 推送狀態
        if "推送狀態" in schema and schema["推送狀態"].get("type") == "select":
            status = "🧪 測試" if "測試" in date_str else "✅ 已推送"
            props["推送狀態"] = {"select": {"name": status}}
        if props:
            requests.patch(
                f"{NOTION_API}/pages/{page_id}",
                headers=_headers(),
                json={"properties": props},
                timeout=30,
            )
    except Exception as e:
        log.warning(f"[notion] set extra props 失敗: {e}")
