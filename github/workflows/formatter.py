"""
formatter.py — 將 cluster 結果格式化成 Telegram 訊息
==================================================
跟足 Anson 指定嘅 message template：

━━━━━━━━━━
 AI 日報 | [日期]
━━━━━━━━━━
【 今日重點】
[150 字總結]
◠◡◠◡◠◡◠◡◠◡◠◡
【 英文 Top 5】[英文媒體名稱]
[編號] [英文標題]
   [繁體中文翻譯]
時間：[ET]  |  [HKT]
 [連結]
 [約100字香港口語解釋]
◠◡◠◡◠◡◠◡◠◡◠◡
【 中文 Top 5】[中文媒體名稱]
[編號] [繁體中文標題]  [X 個來源提及]
時間：[HH:MM]
 [連結]
 [約100字香港口語解釋]
◠◡◠◡◠◡◠◡◠◡◠◡
 每日自動更新
"""

from __future__ import annotations
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Dict, List
import logging
import opencc

import config

log = logging.getLogger(__name__)

# 簡 → 繁（香港字型）
_S2HK = opencc.OpenCC("s2hk")


def _to_traditional(text: str) -> str:
    """簡體 → 繁體（香港用字）。"""
    if not text:
        return text
    return _S2HK.convert(text)


def _fmt_et(iso_str: str) -> str:
    """ISO → ET '14:32' 格式。"""
    if not iso_str:
        return "—"
    dt = datetime.fromisoformat(iso_str)
    return dt.astimezone(ZoneInfo(config.ET_TZ)).strftime("%m-%d %H:%M ET")


def _fmt_hkt(iso_str: str) -> str:
    if not iso_str:
        return "—"
    dt = datetime.fromisoformat(iso_str)
    return dt.astimezone(ZoneInfo(config.HKT_TZ)).strftime("%m-%d %H:%M HKT")


def _fmt_hkt_short(iso_str: str) -> str:
    if not iso_str:
        return "—"
    dt = datetime.fromisoformat(iso_str)
    return dt.astimezone(ZoneInfo(config.HKT_TZ)).strftime("%H:%M")


DIVIDER_TOP = "━━━━━━━━━━"
DIVIDER_MID = "◠◡◠◡◠◡◠◡◠◡◠◡"


def format_message(clusters: Dict, today_date_str: str) -> str:
    """
    生成完整 Telegram 訊息（plain text，唔用 HTML format
    因為 Telegram HTML 對某些 unicode 字會有 issue，
    plain text + emoji 已經夠靚仔同 portable）。
    """
    lines: List[str] = []

    # ─────── Header
    lines.append(DIVIDER_TOP)
    lines.append(f"🌅 AI 日報 | {today_date_str}")
    lines.append(DIVIDER_TOP)
    lines.append("")

    # ─────── 今日重點
    today_summary_en = clusters.get("english", {}).get("today_summary", "")
    today_summary_zh = clusters.get("chinese", {}).get("today_summary", "")
    combined_summary = _build_combined_summary(today_summary_en, today_summary_zh)

    lines.append("【📌 今日重點】")
    lines.append("")
    lines.append(_to_traditional(combined_summary))
    lines.append("")
    lines.append(DIVIDER_MID)
    lines.append("")

    # ─────── 英文 Top
    en_clusters = clusters.get("english", {}).get("top_clusters", [])
    if en_clusters:
        lines.append(f"【🇺🇸 英文 Top {len(en_clusters)}】")
        lines.append("")
        for c in en_clusters:
            lines.extend(_render_rich_card(c, kind="english"))
        lines.append(DIVIDER_MID)
        lines.append("")

    # ─────── 中文 Top
    zh_clusters = clusters.get("chinese", {}).get("top_clusters", [])
    if zh_clusters:
        lines.append(f"【🇨🇳 中文 Top {len(zh_clusters)}】")
        lines.append("")
        for c in zh_clusters:
            lines.extend(_render_rich_card(c, kind="chinese"))
        lines.append(DIVIDER_MID)
        lines.append("")

    # ─────── X（Twitter）熱話
    x_clusters = clusters.get("x", {}).get("top_clusters", [])
    if x_clusters:
        lines.append(f"【🐦 X 熱話 Top {len(x_clusters)}】")
        lines.append("")
        for c in x_clusters:
            lines.extend(_render_rich_card(c, kind="x"))
        lines.append(DIVIDER_MID)
        lines.append("")

    lines.append("🤖 每日自動更新 · 23:59 HKT")

    return "\n".join(lines)


def _render_rich_card(c: Dict, kind: str) -> List[str]:
    """渲染一張深入分析卡（新標題/原標題/網址/日期/摘要/3關鍵詞/總括分析）。"""
    out: List[str] = []
    rank = c.get("rank", "?")
    source = c.get("source", "")
    new_title = _to_traditional(c.get("new_title", ""))
    original_title = c.get("original_title", "")
    if kind in ("chinese",):
        original_title = _to_traditional(original_title)
    link = c.get("link", "")
    cluster_size = c.get("cluster_size", 1)
    summary = _to_traditional(c.get("summary", c.get("explanation", "")))
    analysis = _to_traditional(c.get("analysis", ""))
    keywords = c.get("keywords", [])

    mention_word = "帳號討論" if kind == "x" else "來源提及"
    mention_tag = f"  📊 {cluster_size} 個{mention_word}" if cluster_size > 1 else ""

    # 時間：英文/X 用 ET|HKT，中文用 HH:MM
    if kind == "chinese":
        time_line = f"🕐 發佈：{_fmt_hkt(c.get('pub_hkt',''))}"
    else:
        time_line = f"🕐 發佈：{_fmt_et(c.get('pub_et') or c.get('pub_hkt',''))}  |  {_fmt_hkt(c.get('pub_hkt',''))}"

    out.append(f"{rank}. 【{source}】{mention_tag}")
    out.append(f"📰 新標題：{new_title}")
    out.append(f"📄 原來標題：{original_title}")
    out.append(f"🔗 文章網址：{link}")
    out.append(f"{time_line}")
    out.append("")
    out.append("📝 文章摘要：")
    for para in summary.split("\n\n"):
        para = para.strip()
        if para:
            out.append(para)
    out.append("")
    if keywords:
        out.append("🔑 三個關鍵詞：")
        for kw in keywords[:3]:
            term = _to_traditional(kw.get("term", ""))
            en = kw.get("en", "")
            explain = _to_traditional(kw.get("explain", ""))
            head = f"• {term}（{en}）" if en else f"• {term}"
            out.append(f"{head}：{explain}")
        out.append("")
    if analysis:
        out.append("🧭 總括分析：")
        out.append(analysis)
        out.append("")
    return out


def _build_combined_summary(en_summary: str, zh_summary: str) -> str:
    """
    將中英 summary 合成一個 ~150 字總結。
    如果兩邊都有 summary，揀中文嗰個（因為已經係廣東話書面語），
    然後 append 一個英文媒體焦點 hint（如果有）。
    """
    if zh_summary and en_summary:
        # 中文 summary 已經係廣東話書面語，priority 用佢
        return zh_summary.strip()
    if zh_summary:
        return zh_summary.strip()
    if en_summary:
        return en_summary.strip()
    return "（今日冇足夠新聞抓返嚟，請查 log）"


def split_for_telegram(message: str, max_len: int = None) -> List[str]:
    """
    Telegram 單訊息上限 4096 字。如果超過，split 成多段。
    Split point 揀 \\n（換行）邊界，盡量唔切斷一條 cluster。
    """
    max_len = max_len or config.TELEGRAM_MAX_MESSAGE_LENGTH
    if len(message) <= max_len:
        return [message]

    parts: List[str] = []
    buf = ""
    for line in message.split("\n"):
        candidate = buf + line + "\n"
        if len(candidate) > max_len:
            parts.append(buf.rstrip("\n"))
            buf = line + "\n"
        else:
            buf = candidate
    if buf:
        parts.append(buf.rstrip("\n"))

    log.info(f"[fmt] 訊息分 {len(parts)} 段送（共 {len(message)} 字）")
    return parts
