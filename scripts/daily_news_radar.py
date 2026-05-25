#!/usr/bin/env python3
"""
daily_news_radar.py — 主入口
===========================
完整 pipeline：
  fetch → cluster (Claude) → format → Telegram + Notion archive → log

執行方式：
  python3 daily_news_radar.py            # 正式跑
  DRY_RUN=true python3 daily_news_radar.py   # 唔真係 push
  DEBUG=true python3 daily_news_radar.py     # verbose log

排程：由 macOS launchd 每日 02:00 HKT 觸發
（plist 喺 launchd/com.anson.daily-news-radar.plist）
"""

from __future__ import annotations
import sys
import json
import logging
from datetime import datetime
from zoneinfo import ZoneInfo
from pathlib import Path

import config


def setup_logging():
    config.LOGS_DIR.mkdir(parents=True, exist_ok=True)
    log_file = config.LOGS_DIR / f"radar_{datetime.now().strftime('%Y%m%d')}.log"
    level = logging.DEBUG if config.DEBUG else logging.INFO

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )


def main() -> int:
    setup_logging()
    log = logging.getLogger("radar")

    hkt_now = datetime.now(ZoneInfo(config.HKT_TZ))
    today_date_str = hkt_now.strftime("%Y-%m-%d (%a)")

    log.info("=" * 60)
    log.info(f"🌅 Daily AI News Radar — {hkt_now.isoformat()}")
    log.info(f"DRY_RUN={config.DRY_RUN}  DEBUG={config.DEBUG}")
    log.info("=" * 60)

    # ─── Step 1: Fetch RSS
    from fetcher import fetch_all
    articles_by_lang = fetch_all()

    # ─── Step 1b: Fetch X（Twitter，經 Apify）
    try:
        from x_fetcher import fetch_x
        x_articles = fetch_x()
        if x_articles:
            articles_by_lang["x"] = x_articles
    except Exception as e:
        log.error(f"[x] X 抓取出錯（唔影響其他來源）: {e}")

    total = (len(articles_by_lang.get("english", []))
             + len(articles_by_lang.get("chinese", []))
             + len(articles_by_lang.get("x", [])))
    if total == 0:
        log.warning("⚠️ 0 條文章抓到。今日唔 send。")
        return 1

    # ─── Step 2: Cluster via Claude
    from clusterer import cluster_and_rank
    clusters = cluster_and_rank(articles_by_lang)

    # ─── Step 3: Format
    from formatter import format_message
    message = format_message(clusters, today_date_str)

    # ─── 留個 raw archive backup
    today_date_iso = hkt_now.strftime("%Y-%m-%d")
    archive_file = config.ARCHIVE_DIR / f"radar_{today_date_iso}.json"
    archive_file.parent.mkdir(parents=True, exist_ok=True)
    archive_file.write_text(
        json.dumps({
            "date": today_date_iso,
            "articles_by_lang": articles_by_lang,
            "clusters": clusters,
            "message": message,
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    log.info(f"📁 Raw archive: {archive_file}")

    txt_file = config.ARCHIVE_DIR / f"radar_{today_date_iso}.txt"
    txt_file.write_text(message, encoding="utf-8")
    log.info(f"📄 Message txt: {txt_file}")

    # ─── Step 4: Push Telegram
    from telegram_push import push_message
    tg_ok = push_message(message)

    # ─── Step 5: Archive 入 Notion
    from notion_archive import archive_to_notion
    page_id = archive_to_notion(clusters, today_date_iso, message)

    # ─── Summary
    log.info("=" * 60)
    log.info(f"Telegram: {'✅' if tg_ok else '❌'}")
    log.info(f"Notion: {'✅ ' + page_id if page_id else '❌/skip'}")
    log.info(f"英文 Top: {len(clusters.get('english', {}).get('top_clusters', []))}")
    log.info(f"中文 Top: {len(clusters.get('chinese', {}).get('top_clusters', []))}")
    log.info(f"X 熱話 Top: {len(clusters.get('x', {}).get('top_clusters', []))}")
    log.info("=" * 60)

    return 0 if tg_ok else 2


if __name__ == "__main__":
    sys.exit(main())
