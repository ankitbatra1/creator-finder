from src.crawler.about_scraper import AboutScraper
from src.crawler.website_scraper import WebsiteScraper
from src.crawler.linktree_scraper import LinktreeScraper


class ContactManager:

    def __init__(

        self,

        browser

    ):

        self.about = AboutScraper(browser)

        self.website = WebsiteScraper()

        self.linktree = LinktreeScraper(browser)

    # =====================================================

    async def scrape(

        self,

        channel

    ):

        result = {}

        # ---------------------------------------------

        about = await self.about.scrape(

            channel["channel_url"]

        )

        result.update(about)

        # ---------------------------------------------

        if result.get("website"):

            website = self.website.scrape(

                result["website"]

            )

            result.update(website)

        # ---------------------------------------------

        if (

            not result.get("website_email")

            and

            result.get("linktree")

        ):

            linktree = await self.linktree.scrape(

                result["linktree"]

            )

            result.update(linktree)

        # ---------------------------------------------

        result["final_email"] = ""

        result["email_source"] = ""

        for source in [

            ("youtube_email", "YouTube"),

            ("website_email", "Website"),

            ("linktree_email", "Linktree")

        ]:

            if result.get(source[0]):

                result["final_email"] = result[source[0]]

                result["email_source"] = source[1]

                break

        # ---------------------------------------------

        result["final_phone"] = ""

        result["phone_source"] = ""

        for source in [

            ("youtube_phone", "YouTube"),

            ("website_phone", "Website"),

            ("linktree_phone", "Linktree")

        ]:

            if result.get(source[0]):

                result["final_phone"] = result[source[0]]

                result["phone_source"] = source[1]

                break

        return result