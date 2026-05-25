"""
x_fetcher.py — X (Twitter) 抓取（經 Apify）
==========================================
用 apidojo/tweet-scraper actor 抓指定 AI 帳號過去 LOOKBACK_HOURS 內嘅 tweet。
返回同 RSS fetcher 一致嘅 article dict 結構，方便 clusterer 統一處理。

需要 config.APIFY_API_TOKEN。如果未設定 / X 功能關咗，return []。
"""

from __future__ import annotations
import logging
import requests
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from typing import List, Dict

import config

log = logging.getLogger(__name__)

APIFY_ACTOR = "apidojo~tweet-scraper"  # apidojo/tweet-scraper（~ 係 API 格式）
APIFY_RUN_SYNC_URL = (
    "https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items"
)


def _lookback_start_dt() -> datetime:
    # X 用獨立（較闊）lookback，因為帳號唔係日日 tweet
    hours = getattr(config, "X_LOOKBACK_HOURS", getattr(config, "LOOKBACK_HOURS", 24))
    return datetime.now(ZoneInfo("UTC")) - timedelta(hours=hours)


def _lookback_start_iso() -> str:
    """actor 嘅 start filter（YYYY-MM-DD_HH:MM:SS_UTC）。注意：actor 有時唔尊重，
    所以下面仲會做 code 層時間過濾兜底。"""
    return _lookback_start_dt().strftime("%Y-%m-%d_%H:%M:%S_UTC")


def fetch_x() -> List[Dict]:
    """
    抓 X tweet，返回 article list（同 RSS fetcher 一致結構），
    多加 engagement 欄位（likes / retweets / replies）方便排序。
    """
    if not config.X_ENABLED:
        log.info("[x] X 功能未開（X_ENABLED=false），skip")
        return []
    if not config.APIFY_API_TOKEN:
        log.warning("[x] APIFY_API_TOKEN 未設定，skip X")
        return []
    if not config.X_HANDLES:
        log.warning("[x] 冇設定 X_HANDLES，skip")
        return []

    payload = {
        "twitterHandles": config.X_HANDLES,
        "start": _lookback_start_iso(),
        "sort": "Latest",
        "maxItems": config.X_MAX_ITEMS,
        "tweetLanguage": "en",
        # 過濾低質：至少有少少 engagement（減 noise）
        "minimumFavorites": config.X_MIN_FAVORITES,
    }

    url = APIFY_RUN_SYNC_URL.format(actor=APIFY_ACTOR)
    log.info(f"[x] 抓 {len(config.X_HANDLES)} 個帳號 tweet（過去 {config.X_LOOKBACK_HOURS}h）...")

    try:
        resp = requests.post(
            url,
            params={"token": config.APIFY_API_TOKEN},
            json=payload,
            timeout=180,  # Apify actor 跑要時間
        )
        if resp.status_code >= 300:
            log.error(f"[x] Apify run 失敗 {resp.status_code}: {resp.text[:300]}")
            return []
        items = resp.json()
    except Exception as e:
        log.error(f"[x] Apify 抓 X 失敗: {e}")
        return []

    since_utc = _lookback_start_dt()
    articles = []
    dropped_old = 0
    for tw in items:
        # apidojo/tweet-scraper output 欄位
        text = (tw.get("text") or tw.get("fullText") or "").strip()
        if not text:
            continue
        # 過濾掉純 retweet（text 以 "RT @" 開頭）
        if text.startswith("RT @"):
            continue

        author = tw.get("author") or {}
        handle = author.get("userName") or author.get("screen_name") or tw.get("username") or "?"
        url_tw = tw.get("url") or tw.get("twitterUrl") or ""
        created = tw.get("createdAt") or tw.get("created_at") or ""

        # parse 時間（apidojo 用 ISO 或 Twitter 格式）
        pub_utc = _parse_tweet_time(created)
        if not pub_utc:
            continue
        # ─── code 層時間過濾兜底（actor start filter 唔可靠）
        if pub_utc < since_utc:
            dropped_old += 1
            continue

        likes = tw.get("likeCount") or tw.get("favoriteCount") or 0
        rts = tw.get("retweetCount") or 0
        replies = tw.get("replyCount") or 0
        views = tw.get("viewCount") or 0

        articles.append({
            "source": f"@{handle}",
            "title": text[:280],          # tweet 全文當標題
            "summary": text[:500],
            "link": url_tw,
            "pub_utc": pub_utc.isoformat(),
            "pub_hkt": pub_utc.astimezone(ZoneInfo(config.HKT_TZ)).isoformat(),
            "pub_et": pub_utc.astimezone(ZoneInfo(config.ET_TZ)).isoformat(),
            "engagement": {"likes": likes, "retweets": rts, "replies": replies, "views": views},
            "engagement_score": int(likes) + int(rts) * 2 + int(replies),
        })

    # 按 engagement 排，畀 Gemini 嘅輸入已經係 high-signal
    articles.sort(key=lambda a: a.get("engagement_score", 0), reverse=True)
    log.info(f"[x] 抓到 {len(articles)} 條有效 tweet（隔走 {dropped_old} 條超過 {config.X_LOOKBACK_HOURS}h）")
    return articles[: config.X_MAX_ITEMS]


def _parse_tweet_time(s: str) -> datetime | None:
    if not s:
        return None
    # Try ISO first
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ZoneInfo("UTC"))
        return dt
    except Exception:
        pass
    # Twitter 格式: "Wed May 20 02:30:00 +0000 2026"
    try:
        from email.utils import parsedate_to_datetime
        return parsedate_to_datetime(s)
    except Exception:
        pass
    try:
        dt = datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
        return dt
    except Exception:
        return None
