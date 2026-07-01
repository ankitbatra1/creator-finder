from src.parser.youtube_parser import YouTubeParser
from src.database.manager import DatabaseManager


class ChannelCollector:

    def __init__(self, db: DatabaseManager):

        self.db = db

        self.memory = set()

    # =====================================================

    def collect(self, html: str, keyword: str):

        parser = YouTubeParser(html)

        channels = parser.all_channels()

        added = 0

        for channel in channels:

            channel["keyword"] = keyword

            cid = channel["channel_id"]

            if cid in self.memory:
                continue

            self.memory.add(cid)

            self.db.save_channel(channel)

            added += 1

        self.db.commit()

        return added

    # =====================================================

    def clear(self):

        self.memory.clear()