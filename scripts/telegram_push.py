"""
telegram_push.py — Telegram bot push
====================================
透過 Telegram Bot API 推送訊息。長訊息自動 split。
"""

from __future__ import annotations
import logging
import time
import requests
from typing import List

import config
from formatter import split_for_telegram

log = logging.getLogger(__name__)


def _send_one(text: str) -> bool:
    """Send 一段訊息。Return True/False。"""
    if config.DRY_RUN:
        log.info(f"[telegram] DRY_RUN — 唔真係 send，訊息長度 {len(text)}")
        return True

    if not config.TELEGRAM_BOT_TOKEN or not config.TELEGRAM_CHAT_ID:
        log.error("[telegram] Bot token / chat ID 未設定")
        return False

    url = f"{config.TELEGRAM_API_BASE}/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": config.TELEGRAM_CHAT_ID,
        "text": text,
        "disable_web_page_preview": False,  # 開 link preview
    }

    for attempt in range(3):
        try:
            resp = requests.post(url, json=payload, timeout=30)
            data = resp.json()
            if resp.status_code == 200 and data.get("ok"):
                log.info(f"[telegram] ✅ 送出（{len(text)} 字）")
                return True
            log.warning(f"[telegram] 第 {attempt+1} 次失敗: {resp.status_code} / {data}")
            # Telegram rate limit handling
            if resp.status_code == 429:
                retry_after = data.get("parameters", {}).get("retry_after", 5)
                time.sleep(retry_after + 1)
            else:
                time.sleep(2 ** attempt)
        except Exception as e:
            log.warning(f"[telegram] 第 {attempt+1} 次 exception: {e}")
            time.sleep(2 ** attempt)
    log.error("[telegram] ❌ 3 次都失敗")
    return False


def push_message(message: str) -> bool:
    """主入口：split + send。"""
    parts = split_for_telegram(message)
    all_ok = True
    for i, part in enumerate(parts, 1):
        ok = _send_one(part)
        all_ok = all_ok and ok
        if i < len(parts):
            time.sleep(1)  # 避 rate limit
    return all_ok
