"""
fetcher.py — RSS 抓取 + HKT 00:00 過濾
=====================================
抓 4 個來源、parse 日期、轉 HKT、過濾返「今日 HKT 00:00 之後」嘅文章。
"""

from __future__ import annotations
import feedparser
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from typing import List, Dict
import logging
import re
from html import unescape

import config

log = logging.getLogger(__name__)


def _strip_html(text: str) -> str:
    """簡單 strip HTML tags 同 normalize whitespace。"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _parse_pub_date(entry) -> datetime | None:
    """從 RSS entry 攞 published_parsed / updated_parsed，轉做 UTC datetime。"""
    for key in ("published_parsed", "updated_parsed"):
        struct = entry.get(key)
        if struct:
            try:
                return datetime(*struct[:6], tzinfo=ZoneInfo("UTC"))
            except Exception:
                continue
    return None


def _matches_ai(title: str, summary: str, keywords: List[str]) -> bool:
    """Keyword filter：title 或 summary 任一 match 就算 AI 文。Case-insensitive。"""
    if not keywords:
        return True
    haystack = (title + " " + summary).lower()
    return any(kw.lower() in haystack for kw in keywords)


def _lookback_start() -> datetime:
    """
    抓取起點（UTC return）。

    設計：因為 script 喺 HKT 02:00 跑，如果只取「當日 00:00 後」會得 2 個鐘
    內容（太少）。所以實際抓取「過去 24 小時內」嘅文章 — 即昨日 02:00 HKT
    起，覆蓋完整一日週期。

    可由 config.py 嘅 LOOKBACK_HOURS override。
    """
    hours = getattr(config, "LOOKBACK_HOURS", 24)
    now_utc = datetime.now(ZoneInfo("UTC"))
    return now_utc - timedelta(hours=hours)


def fetch_source(source: Dict, since_utc: datetime) -> List[Dict]:
    """抓單一 RSS source，返回過濾後嘅 article list。"""
    name = source["name"]
    url = source["url"]
    log.info(f"[fetch] {name} <- {url}")

    headers = {"User-Agent": "Mozilla/5.0 (compatible; DailyAINewsRadar/1.0)"}
    try:
        resp = requests.get(url, headers=headers, timeout=30)
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except Exception as e:
        log.error(f"[fetch] {name} 抓 RSS 失敗: {e}")
        return []

    articles = []
    for entry in feed.entries:
        title = _strip_html(entry.get("title", ""))
        summary = _strip_html(entry.get("summary", "") or entry.get("description", ""))
        link = entry.get("link", "")

        pub_utc = _parse_pub_date(entry)
        if not pub_utc:
            continue  # 冇日期嘅 entry 略過
        if pub_utc < since_utc:
            continue  # 早過 HKT 00:00 嘅 skip

        # AI keyword filter（淨係用喺 ai_filter=True 嘅 source）
        if source.get("ai_filter", False):
            if not _matches_ai(title, summary, source.get("ai_keywords", [])):
                continue

        articles.append({
            "source": name,
            "title": title,
            "summary": summary[:500],  # cap 500 字 control prompt size
            "link": link,
            "pub_utc": pub_utc.isoformat(),
            "pub_hkt": pub_utc.astimezone(ZoneInfo(config.HKT_TZ)).isoformat(),
            "pub_et": pub_utc.astimezone(ZoneInfo(config.ET_TZ)).isoformat(),
        })

    log.info(f"[fetch] {name} 過濾後 {len(articles)} 條")
    return articles


def fetch_all() -> Dict[str, List[Dict]]:
    """
    返 dict:
      {
        "english": [{source, title, summary, link, pub_utc, pub_hkt, pub_et}, ...],
        "chinese": [...]
      }
    """
    since_utc = _lookback_start()
    hours = getattr(config, "LOOKBACK_HOURS", 24)
    log.info(f"[fetch] 過濾起點: {since_utc.isoformat()} (過去 {hours} 小時)")

    result = {"english": [], "chinese": []}
    for lang in ("english", "chinese"):
        for source in config.RSS_SOURCES[lang]:
            articles = fetch_source(source, since_utc)
            result[lang].extend(articles)

    log.info(f"[fetch] 英文總數: {len(result['english'])}, 中文總數: {len(result['chinese'])}")
    return result
