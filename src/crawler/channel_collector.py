from src.parser.youtube_parser import YouTubeParser
from src.database.manager import DatabaseManager


class ChannelCollector:
    """
    Parses search HTML and stores unique channels.
    """

    def __init__(self, db: DatabaseManager):

        self.db = db

        self.seen = set()

    # =====================================================

    def collect(

        self,

        html: str,

        keyword: str

    ) -> int:

        parser = YouTubeParser(html)

        channels = parser.all_channels()

        new_channels = 0

        for channel in channels:

            channel["keyword"] = keyword

            cid = channel["channel_id"]

            if cid in self.seen:

                continue

            self.seen.add(cid)

            self.db.save_channel(channel)

            new_channels += 1

        self.db.commit()

        return new_channels

    # =====================================================

    def reset(self):

        self.seen.clear()