from playwright.async_api import Page


class ScrollManager:
    """
    Handles infinite scrolling on YouTube pages.
    """

    def __init__(
        self,
        page: Page,
        delay: int = 1500,
        max_scrolls: int = 100,
        max_empty_scrolls: int = 5
    ):

        self.page = page
        self.delay = delay
        self.max_scrolls = max_scrolls
        self.max_empty_scrolls = max_empty_scrolls

    # =====================================================

    async def current_height(self) -> int:

        return await self.page.evaluate(
            "document.documentElement.scrollHeight"
        )

    # =====================================================

    async def scroll_once(self):

        await self.page.evaluate(
            """
            window.scrollTo(
                0,
                document.documentElement.scrollHeight
            );
            """
        )

        await self.page.wait_for_timeout(
            self.delay
        )

    # =====================================================

    async def scroll_to_bottom(self):

        last_height = await self.current_height()

        empty_scrolls = 0

        total_scrolls = 0

        while True:

            if total_scrolls >= self.max_scrolls:

                print("\nReached maximum scroll limit.")

                break

            await self.scroll_once()

            new_height = await self.current_height()

            total_scrolls += 1

            print(
                f"\rScroll : {total_scrolls}",
                end=""
            )

            if new_height == last_height:

                empty_scrolls += 1

            else:

                empty_scrolls = 0

            if empty_scrolls >= self.max_empty_scrolls:

                print("\nNo more results.")

                break

            last_height = new_height

        print(
            f"\nTotal Scrolls : {total_scrolls}"
        )

        return total_scrolls

    # =====================================================

    async def scroll_n_times(
        self,
        count: int
    ):

        for i in range(count):

            await self.scroll_once()

            print(
                f"\rScroll {i+1}/{count}",
                end=""
            )

        print()