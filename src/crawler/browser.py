from playwright.sync_api import sync_playwright

from config import (
    HEADLESS,
    SLOW_MO,
    VIEWPORT,
    USER_AGENT,
    PROFILE_DIR
)


class Browser:

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    # =====================================================

    def start(self):

        self.playwright = sync_playwright().start()

        self.context = self.playwright.chromium.launch_persistent_context(

            user_data_dir=PROFILE_DIR,

            headless=HEADLESS,

            slow_mo=SLOW_MO,

            viewport=VIEWPORT,

            user_agent=USER_AGENT

        )

        self.page = self.context.new_page()

    # =====================================================

    def open(self, url):

        self.page.goto(

            url,

            wait_until="networkidle"

        )

    # =====================================================

    def html(self):

        return self.page.content()

    # =====================================================

    def title(self):

        return self.page.title()

    # =====================================================

    def scroll_bottom(self):

        self.page.evaluate("""

        window.scrollTo(
            0,
            document.body.scrollHeight
        )

        """)

    # =====================================================

    def page_height(self):

        return self.page.evaluate("""

        document.body.scrollHeight

        """)

    # =====================================================

    def wait(self, seconds):

        self.page.wait_for_timeout(

            seconds * 1000

        )

    # =====================================================

    def click(self, selector):

        self.page.locator(selector).click()

    # =====================================================

    def locator(self, selector):

        return self.page.locator(selector)

    # =====================================================

    def close(self):

        self.context.close()

        self.playwright.stop()