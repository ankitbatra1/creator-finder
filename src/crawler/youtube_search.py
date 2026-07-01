from urllib.parse import quote_plus

from config import (
    YOUTUBE_SEARCH,
    VIDEO_FILTER,
    CHANNEL_FILTER
)

from src.crawler.scroll_manager import ScrollManager
from src.crawler.browser import BrowserManager


class YouTubeSearch:

    def __init__(self, browser: BrowserManager):

        self.browser = browser

    # =====================================================

    async def _load(

        self,

        keyword: str,

        search_filter: str,

        max_scrolls: int

    ):

        url = (

            YOUTUBE_SEARCH

            + quote_plus(keyword)

            + search_filter

        )

        print(f"\nSearching : {keyword}")

        await self.browser.goto(url)

        scroll = ScrollManager(

            self.browser.page,

            delay=1500,

            max_scrolls=max_scrolls,

            max_empty_scrolls=3

        )

        await scroll.scroll_to_bottom()

        return await self.browser.html()

    # =====================================================

    async def video(

        self,

        keyword: str

    ):

        return await self._load(

            keyword,

            VIDEO_FILTER,

            25

        )

    # =====================================================

    async def channel(

        self,

        keyword: str

    ):

        return await self._load(

            keyword,

            CHANNEL_FILTER,

            10

        )