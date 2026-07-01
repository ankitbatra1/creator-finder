from src.database.manager import DatabaseManager
from src.crawler.browser import BrowserManager
from src.crawler.search_engine import SearchEngine


class DiscoveryService:

    def __init__(self):

        self.db = DatabaseManager()

        self.browser = BrowserManager()

        self.search = SearchEngine(

            browser=self.browser,

            db=self.db

        )

    async def run(

        self,

        limit=100,

        workers=1

    ):

        print("\n========== DISCOVERY ==========\n")

        await self.browser.start()

        try:

            await self.search.run(

                limit=limit

            )

        finally:

            await self.browser.close()

            self.db.close()

        print("\nFinished.")