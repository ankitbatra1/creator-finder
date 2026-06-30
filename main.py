import asyncio
import argparse

from src.crawler.browser import BrowserManager


class CreatorFinder:

    def __init__(self):

        self.browser = BrowserManager()

    # =====================================================

    async def discover(self):

        print("\n========== DISCOVERY ==========\n")

        await self.browser.start()

        await self.browser.goto(
            "https://www.youtube.com"
        )

        print(
            "Browser Started"
        )

        print(
            "Title :",
            await self.browser.title()
        )

        print(
            "URL :",
            await self.browser.url()
        )

        await self.browser.close()

        print(
            "\nDiscovery Finished."
        )

    # =====================================================

    async def contacts(self):

        print(
            "\nContacts Module (Coming Soon)"
        )

    # =====================================================

    async def export(self):

        print(
            "\nExport Module (Coming Soon)"
        )

    # =====================================================

    async def full(self):

        await self.discover()

        await self.contacts()

        await self.export()


# =========================================================

async def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(

        "command",

        choices=[
            "discover",
            "contacts",
            "export",
            "full"
        ]

    )

    args = parser.parse_args()

    app = CreatorFinder()

    if args.command == "discover":

        await app.discover()

    elif args.command == "contacts":

        await app.contacts()

    elif args.command == "export":

        await app.export()

    elif args.command == "full":

        await app.full()


# =========================================================

if __name__ == "__main__":

    asyncio.run(main())