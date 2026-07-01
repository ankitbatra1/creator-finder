from src.crawler.youtube_search import YouTubeSearch
from src.crawler.channel_collector import ChannelCollector
from src.crawler.query_generator import QueryGenerator

from src.database.channel_repository import ChannelRepository
from src.database.job_repository import JobRepository
from src.database.manager import DatabaseManager

from src.crawler.browser import BrowserManager


class SearchEngine:

    def __init__(

        self,

        browser: BrowserManager,

        db: DatabaseManager

    ):

        self.browser = browser

        self.db = db

        self.repository = ChannelRepository(db)

        self.collector = ChannelCollector(

            self.db

        )

        self.jobs = JobRepository(db)

        self.youtube = YouTubeSearch(browser)

        self.generator = QueryGenerator()

    # =====================================================

    async def search_keyword(

        self,

        keyword: str

    ):

        if self.jobs.completed(

            keyword,

            "video"

        ):

            print(

                f"Skipped : {keyword}"

            )

            return

        self.jobs.create(

            keyword,

            "video"

        )

        self.jobs.start(

            keyword,

            "video"

        )

        html = await self.youtube.video(

            keyword

        )

        added = self.collector.collect(

            html,

            keyword

        )

        self.jobs.finish(

            keyword,

            "video"

        )

        print()

        print(

            "Collected :",

            added

        )

        print(

            "Database :",

            self.repository.total()

        )

    # =====================================================

    async def run(

        self,

        limit=None

    ):

        queries = self.generator.generate()

        if limit:

            queries = queries[:limit]

        print()

        print(

            "Queries :",

            len(queries)

        )

        print()

        for i, keyword in enumerate(

            queries,

            start=1

        ):

            print(

                "=" * 60

            )

            print(

                f"{i}/{len(queries)}"

            )

            await self.search_keyword(

                keyword

            )

        print()

        print(

            "=" * 60

        )

        print(

            "Finished"

        )

        print(

            "Total Channels :",

            self.repository.total()

        )