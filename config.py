import os

# ============================================================
# PROJECT
# ============================================================

PROJECT_NAME = "Creator Finder"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# DIRECTORIES
# ============================================================

DATA_DIR = os.path.join(BASE_DIR, "data")
EXPORT_DIR = os.path.join(BASE_DIR, "exports")
LOG_DIR = os.path.join(BASE_DIR, "logs")
PROFILE_DIR = os.path.join(DATA_DIR, "browser_profile")

for directory in [
    DATA_DIR,
    EXPORT_DIR,
    LOG_DIR,
    PROFILE_DIR
]:
    os.makedirs(directory, exist_ok=True)

# ============================================================
# DATABASE
# ============================================================

DATABASE_PATH = os.path.join(
    DATA_DIR,
    "creator_finder.db"
)

# ============================================================
# FILES
# ============================================================

KEYWORDS_PATH = os.path.join(
    DATA_DIR,
    "keywords.json"
)

API_KEYS_PATH = os.path.join(
    DATA_DIR,
    "api_keys.json"
)

# ============================================================
# PLAYWRIGHT
# ============================================================

HEADLESS = False

SLOW_MO = 50

VIEWPORT = {
    "width": 1600,
    "height": 900
}

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/137.0.0.0 Safari/537.36"
)

SEARCH_TIMEOUT = 30000

SCROLL_DELAY = 2000

MAX_SCROLLS = 100

MAX_EMPTY_SCROLLS = 5

# ============================================================
# SEARCH FILTERS
# ============================================================

VIDEO_FILTER = "&sp=EgIQAQ%253D%253D"

CHANNEL_FILTER = "&sp=EgIQAg%253D%253D"

YOUTUBE_SEARCH = (
    "https://www.youtube.com/results?search_query="
)

# ============================================================
# WEBSITE
# ============================================================

REQUEST_TIMEOUT = 20

MAX_CONTACT_PAGES = 10

# ============================================================
# DATABASE
# ============================================================

COMMIT_BATCH = 100