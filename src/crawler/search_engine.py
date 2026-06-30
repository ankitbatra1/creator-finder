from urllib.parse import quote_plus

from src.crawler.scroll_manager import ScrollManager
from src.crawler.channel_collector import ChannelCollector
from src.database.manager import DatabaseManager
from src.crawler.browser import BrowserManager

from config import (
    YOUTUBE_SEARCH,
    VIDEO_FILTER,
    CHANNEL_FILTER
)


class SearchEngine:

    def __init__(
        self,
        browser: BrowserManager,
        db: DatabaseManager
    ):

        self.browser = browser
        self.db = db

        self.collector = ChannelCollector(db)

    # =====================================================

    async def search_video(
        self,
        keyword: str
    ):

        url = (

            YOUTUBE_SEARCH

            + quote_plus(keyword)

            + VIDEO_FILTER

        )

        print(f"\nSearching Videos : {keyword}")

        await self.browser.goto(url)

        scroll = ScrollManager(

            self.browser.page,

            delay=1500,

            max_scrolls=20,

            max_empty_scrolls=3

        )

        await scroll.scroll_to_bottom()

        html = await self.browser.html()

        added = self.collector.collect(

            html,

            keyword

        )

        print(

            f"Video Search Added : {added}"

        )

    # =====================================================

    async def search_channel(

        self,

        keyword: str

    ):

        url = (

            YOUTUBE_SEARCH

            + quote_plus(keyword)

            + CHANNEL_FILTER

        )

        print(f"\nSearching Channels : {keyword}")

        await self.browser.goto(url)

        scroll = ScrollManager(

            self.browser.page,

            delay=1500,

            max_scrolls=10,

            max_empty_scrolls=3

        )

        await scroll.scroll_to_bottom()

        html = await self.browser.html()

        added = self.collector.collect(

            html,

            keyword

        )

        print(

            f"Channel Search Added : {added}"

        )

    # =====================================================

    async def search(

        self,

        keyword: str

    ):

        await self.search_video(

            keyword

        )

        await self.search_channel(

            keyword

        )

        print(

            "\nDatabase Total :",

            self.db.total_channels()

        )