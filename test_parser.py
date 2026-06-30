import asyncio

from src.crawler.browser import BrowserManager
from src.parser.youtube_parser import YouTubeParser


async def main():

    browser = BrowserManager()

    await browser.start()

    await browser.goto(
        "https://www.youtube.com/results?search_query=college+vlog+india"
    )

    html = await browser.html()

    parser = YouTubeParser(html)

    channels = parser.all_channels()

    print(len(channels))

    for channel in channels[:10]:

        print(channel)

    await browser.close()


asyncio.run(main())