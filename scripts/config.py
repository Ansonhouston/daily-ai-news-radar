"""
Daily AI News Radar — Configuration
====================================
所有 RSS sources / API endpoints / 排程設定都集中喺呢度。
敏感 keys（Telegram bot token / Anthropic API key / Notion API token）
經由 .env 載入，唔會 hardcode 入 source code。
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
LOGS_DIR = PROJECT_ROOT / "logs"
ARCHIVE_DIR = PROJECT_ROOT / "archive"

# 載入 .env（key 全部放呢度，唔入 git）
load_dotenv(CONFIG_DIR / ".env")

# ─────────────────────────────────────────────
# API Keys（由 .env 載入）
# ─────────────────────────────────────────────
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
APIFY_API_TOKEN = os.getenv("APIFY_API_TOKEN", "")  # X (Twitter) scraper
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
NOTION_API_TOKEN = os.getenv("NOTION_API_TOKEN", "")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID", "")  # 子 database for archive
NOTION_PARENT_PAGE_ID = os.getenv("NOTION_PARENT_PAGE_ID", "")  # 「🌅 每日 AI 新聞速報」hub page

# ─────────────────────────────────────────────
# RSS Sources
# ─────────────────────────────────────────────
RSS_SOURCES = {
    "english": [
        {
            "name": "The Verge",
            "url": "https://www.theverge.com/rss/index.xml",
            "ai_filter": True,  # The Verge 主 feed 唔限 AI，要 keyword filter
            "ai_keywords": ["ai", "artificial intelligence", "openai", "anthropic",
                            "google", "gpt", "claude", "gemini", "llm", "chatbot",
                            "machine learning", "neural", "robot", "deepmind",
                            "nvidia", "model", "agent"],
        },
        {
            "name": "TechCrunch AI",
            "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
            "ai_filter": False,  # 整個 feed 已經係 AI
            "ai_keywords": [],
        },
    ],
    "chinese": [
        {
            "name": "36氪",
            "url": "https://www.36kr.com/feed",
            "ai_filter": True,
            "ai_keywords": ["AI", "人工智能", "大模型", "ChatGPT", "GPT", "OpenAI",
                            "Claude", "Gemini", "Anthropic", "DeepSeek", "智能體",
                            "Agent", "機器學習", "深度學習", "Sora", "Nvidia", "英偉達",
                            "大語言模型", "LLM", "AIGC", "生成式"],
        },
        {
            "name": "量子位",
            "url": "https://www.qbitai.com/feed",
            "ai_filter": False,  # 整個 feed 已經係 AI
            "ai_keywords": [],
        },
    ],
}

# ─────────────────────────────────────────────
# Timezones
# ─────────────────────────────────────────────
HKT_TZ = "Asia/Hong_Kong"
ET_TZ = "America/New_York"

# ─────────────────────────────────────────────
# Top selection
# ─────────────────────────────────────────────
TOP_N_ENGLISH = 3
TOP_N_CHINESE = 3
TOP_N_X = 3
MIN_ARTICLES_PER_SOURCE = 1  # 至少抓返一條

# ─────────────────────────────────────────────
# X (Twitter) — 經 Apify
# ─────────────────────────────────────────────
X_ENABLED = os.getenv("X_ENABLED", "true").lower() == "true"
# 追蹤嘅 AI 帳號（唔使加 @）
X_HANDLES = os.getenv("X_HANDLES", "").split(",") if os.getenv("X_HANDLES") else [
    "OpenAI",
    "AnthropicAI",
    "GoogleDeepMind",
    "sama",          # Sam Altman
    "karpathy",      # Andrej Karpathy
    "demishassabis", # Demis Hassabis
    "ylecun",        # Yann LeCun
    "xai",
    "GoogleAI",
    "midjourney",
]
X_MAX_ITEMS = int(os.getenv("X_MAX_ITEMS", "60"))  # 抓返嚟畀 Gemini 篩嘅上限
X_MIN_FAVORITES = int(os.getenv("X_MIN_FAVORITES", "20"))  # 過濾低 engagement noise
# X 帳號唔係日日 tweet，所以 X 用獨立（較闊）lookback，確保 section 有料
X_LOOKBACK_HOURS = int(os.getenv("X_LOOKBACK_HOURS", "48"))

# 抓取 lookback window（小時）— 預設 24h，即過去一日內容
# 想嚴格「當日 HKT 00:00 後」可改細啲（但 02:00 跑會得 2h 內容）
LOOKBACK_HOURS = int(os.getenv("LOOKBACK_HOURS", "24"))

# ─────────────────────────────────────────────
# LLM provider（語意聚類引擎）
# ─────────────────────────────────────────────
# primary provider：gemini（免費 tier）/ claude / deepseek / openai
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")
# 失敗時 fallback provider（留空 = 唔 fallback）
LLM_FALLBACK_PROVIDER = os.getenv("LLM_FALLBACK_PROVIDER", "")
LLM_MAX_TOKENS = int(os.getenv("LLM_MAX_TOKENS", "8000"))

# 各 provider 嘅 model 名（可由 .env override）
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
CLAUDE_MODEL = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-5")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ─────────────────────────────────────────────
# Telegram
# ─────────────────────────────────────────────
TELEGRAM_API_BASE = "https://api.telegram.org"
TELEGRAM_PARSE_MODE = "HTML"  # 用 HTML 避免 Markdown escape 問題
TELEGRAM_MAX_MESSAGE_LENGTH = 4096  # Telegram 單訊息字數上限

# ─────────────────────────────────────────────
# Behavior flags
# ─────────────────────────────────────────────
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"  # 唔 push 落 Telegram / Notion
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
