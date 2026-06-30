import asyncio

from src.database.manager import DatabaseManager
from src.crawler.browser import BrowserManager
from src.crawler.search_engine import SearchEngine


async def main():

    db = DatabaseManager()

    browser = BrowserManager()

    await browser.start()

    engine = SearchEngine(

        browser,

        db

    )

    await engine.search(

        "college vlog india"

    )

    await browser.close()

    db.close()


asyncio.run(main())