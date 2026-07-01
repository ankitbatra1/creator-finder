import requests

from bs4 import BeautifulSoup

from src.extractor.email_extractor import EmailExtractor
from src.extractor.phone_extractor import PhoneExtractor


class WebsiteScraper:

    def __init__(self):

        self.headers = {

            "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

        }

        self.contact_pages = [

            "",

            "/contact",

            "/contact-us",

            "/about",

            "/about-us",

            "/support",

            "/team",

            "/connect"

        ]

    # =====================================================

    def scrape(self, website):

        if not website:

            return {}

        emails = set()

        phones = set()

        pages_scanned = 0

        visited = set()

        for page in self.contact_pages:

            url = website.rstrip("/") + page

            if url in visited:

                continue

            visited.add(url)

            try:

                response = requests.get(

                    url,

                    headers=self.headers,

                    timeout=10,

                    allow_redirects=True

                )

            except Exception:

                continue

            if response.status_code != 200:

                continue

            pages_scanned += 1

            html = response.text

            soup = BeautifulSoup(

                html,

                "lxml"

            )

            # -----------------------------------------------
            # mailto: & tel:
            # -----------------------------------------------

            for a in soup.select("a[href]"):

                href = a.get("href", "").strip()

                if href.startswith("mailto:"):

                    email = href.replace(
                        "mailto:",
                        ""
                    ).strip()

                    if email:

                        emails.add(email)

                elif href.startswith("tel:"):

                    phone = href.replace(
                        "tel:",
                        ""
                    ).strip()

                    if phone:

                        phones.add(phone)

            # -----------------------------------------------
            # Plain text
            # -----------------------------------------------

            text = soup.get_text(

                " ",

                strip=True

            )

            emails.update(

                EmailExtractor.extract(text)

            )

            emails.update(

                EmailExtractor.extract(html)

            )

            phones.update(

                PhoneExtractor.extract(text)

            )

            phones.update(

                PhoneExtractor.extract(html)

            )

        return {

            "website_email":

                sorted(emails)[0]

                if emails else "",

            "website_phone":

                sorted(phones)[0]

                if phones else "",

            "pages_scanned":

                pages_scanned

        }