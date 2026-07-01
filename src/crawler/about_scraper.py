import re

from src.extractor.email_extractor import EmailExtractor
from src.extractor.phone_extractor import PhoneExtractor
from src.utils.url_utils import URLUtils


class AboutScraper:

    def __init__(self, browser):

        self.browser = browser

    # =====================================================

    async def scrape(self, channel_url):

        about_url = channel_url.rstrip("/") + "/about"

        try:

            await self.browser.goto(
                about_url,
                timeout=60000
            )

        except Exception:

            return {}

        html = await self.browser.html()

        youtube_email = EmailExtractor.first(html)
        youtube_phone = PhoneExtractor.first(html)

        website = ""
        instagram = ""
        linktree = ""

        urls = re.findall(
            r'https?://[^\s"\']+',
            html,
            flags=re.IGNORECASE
        )

        for url in urls:

            lower = url.lower()

            if "instagram.com" in lower:

                instagram = url

            elif "linktr.ee" in lower:

                linktree = url

            elif "youtube.com" in lower:

                continue

            elif website == "":

                website = url

        return {

            "youtube_email": youtube_email,

            "youtube_phone": youtube_phone,

            "website": website,

            "instagram": instagram,

            "instagram_username":
                URLUtils.instagram_username(
                    instagram
                ),

            "linktree": linktree

        }