from bs4 import BeautifulSoup

from src.extractor.email_extractor import EmailExtractor
from src.extractor.phone_extractor import PhoneExtractor


class LinktreeScraper:

    def __init__(self, browser):

        self.browser = browser

    # =====================================================

    async def scrape(self, url):

        if not url:

            return {}

        try:

            await self.browser.goto(
                url,
                timeout=60000
            )

        except Exception:

            return {}

        html = await self.browser.html()

        soup = BeautifulSoup(

            html,

            "lxml"

        )

        text = soup.get_text(

            " ",

            strip=True

        )

        emails = EmailExtractor.extract(text)

        phones = PhoneExtractor.extract(text)

        links = []

        for a in soup.select("a[href]"):

            href = a.get("href", "").strip()

            if href.startswith("http"):

                links.append(href)

        return {

            "linktree_email":

                emails[0] if emails else "",

            "linktree_phone":

                phones[0] if phones else "",

            "external_links":

                list(set(links))

        }