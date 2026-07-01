from urllib.parse import urlparse


class URLUtils:

    @staticmethod
    def instagram_username(url):

        if not url:

            return ""

        try:

            path = urlparse(url).path.strip("/")

            if not path:

                return ""

            return path.split("/")[0]

        except:

            return ""

    # ===================================================

    @staticmethod
    def is_instagram(url):

        return "instagram.com" in url.lower()

    # ===================================================

    @staticmethod
    def is_linktree(url):

        return "linktr.ee" in url.lower()