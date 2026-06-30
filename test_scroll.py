import asyncio

from src.crawler.browser import BrowserManager
from src.crawler.scroll_manager import ScrollManager


async def main():

    browser = BrowserManager()

    await browser.start()

    await browser.goto(
        "https://www.youtube.com/results?search_query=college+vlog+india"
    )

    scroll = ScrollManager(

        browser.page,

        delay=2000,

        max_scrolls=20

    )

    await scroll.scroll_to_bottom()

    print(

        "Finished"

    )

    await browser.close()


asyncio.run(main())