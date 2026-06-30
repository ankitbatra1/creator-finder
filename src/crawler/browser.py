from pathlib import Path
from playwright.async_api import (
    async_playwright,
    BrowserContext,
    Browser,
    Page
)

from config import (
    PROFILE_DIR,
    HEADLESS,
    VIEWPORT,
    USER_AGENT,
    SLOW_MO
)


class BrowserManager:
    """
    Playwright Browser Manager

    Single browser
    Multiple pages
    Persistent profile
    """

    def __init__(self):

        self.playwright = None

        self.browser: Browser | None = None

        self.context: BrowserContext | None = None

        self.page: Page | None = None

    # ======================================================

    async def start(self):

        profile = Path(PROFILE_DIR)

        profile.mkdir(
            parents=True,
            exist_ok=True
        )

        self.playwright = await async_playwright().start()

        self.context = (
            await self.playwright.chromium.launch_persistent_context(

                user_data_dir=str(profile),

                headless=HEADLESS,

                slow_mo=SLOW_MO,

                viewport=VIEWPORT,

                user_agent=USER_AGENT

            )
        )

        pages = self.context.pages

        if pages:

            self.page = pages[0]

        else:

            self.page = await self.context.new_page()

    # ======================================================

    async def goto(
        self,
        url: str
    ):

        await self.page.goto(

            url,

            wait_until="networkidle"

        )

    # ======================================================

    async def html(self):

        return await self.page.content()

    # ======================================================

    async def title(self):

        return await self.page.title()

    # ======================================================

    async def url(self):

        return self.page.url

    # ======================================================

    async def scroll_bottom(self):

        await self.page.evaluate("""

        window.scrollTo(
            0,
            document.body.scrollHeight
        )

        """)

    # ======================================================

    async def page_height(self):

        return await self.page.evaluate(

            "document.body.scrollHeight"

        )

    # ======================================================

    async def wait(
        self,
        milliseconds: int
    ):

        await self.page.wait_for_timeout(

            milliseconds

        )

    # ======================================================

    async def click(
        self,
        selector: str
    ):

        await self.page.locator(

            selector

        ).click()

    # ======================================================

    async def fill(
        self,
        selector: str,
        value: str
    ):

        await self.page.locator(

            selector

        ).fill(value)

    # ======================================================

    async def locator(
        self,
        selector: str
    ):

        return self.page.locator(selector)

    # ======================================================

    async def screenshot(
        self,
        path: str
    ):

        await self.page.screenshot(

            path=path,

            full_page=True

        )

    # ======================================================

    async def new_tab(self):

        return await self.context.new_page()

    # ======================================================

    async def close(self):

        if self.context:

            await self.context.close()

        if self.playwright:

            await self.playwright.stop()