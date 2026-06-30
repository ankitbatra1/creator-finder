from bs4 import BeautifulSoup
from urllib.parse import urljoin


class YouTubeParser:
    """
    Parses YouTube Search HTML.

    Returns unique channels from:
        - Video Search
        - Channel Search
    """

    BASE_URL = "https://www.youtube.com"

    def __init__(self, html: str):

        self.soup = BeautifulSoup(
            html,
            "lxml"
        )

    # =========================================================

    def video_channels(self):

        channels = {}

        videos = self.soup.select(
            "ytd-video-renderer"
        )

        for video in videos:

            link = video.select_one(
                "a.yt-simple-endpoint.yt-formatted-string"
            )

            if link is None:
                continue

            href = link.get("href", "")

            if not href.startswith("/@") and not href.startswith("/channel/"):
                continue

            channel_url = urljoin(
                self.BASE_URL,
                href
            )

            channel_name = (
                link.get_text(strip=True)
            )

            channel_id = href

            channels[channel_id] = {

                "channel_id": channel_id,

                "channel_name": channel_name,

                "channel_url": channel_url,

                "source": "video"

            }

        return list(
            channels.values()
        )

    # =========================================================

    def channel_results(self):

        channels = {}

        cards = self.soup.select(
            "ytd-channel-renderer"
        )

        for card in cards:

            link = card.select_one(
                "a#main-link"
            )

            if link is None:

                link = card.select_one(
                    "a.yt-simple-endpoint"
                )

            if link is None:
                continue

            href = link.get(
                "href",
                ""
            )

            if not href:
                continue

            channel_url = urljoin(
                self.BASE_URL,
                href
            )

            channel_name = (
                link.get_text(strip=True)
            )

            channel_id = href

            channels[channel_id] = {

                "channel_id": channel_id,

                "channel_name": channel_name,

                "channel_url": channel_url,

                "source": "channel"

            }

        return list(
            channels.values()
        )

    # =========================================================

    def all_channels(self):

        data = {}

        for channel in self.video_channels():

            data[
                channel["channel_id"]
            ] = channel

        for channel in self.channel_results():

            data[
                channel["channel_id"]
            ] = channel

        return list(
            data.values()
        )