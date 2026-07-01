from src.database.manager import DatabaseManager


class ChannelRepository:

    def __init__(self, db: DatabaseManager):

        self.db = db

    # =====================================================

    def save(self, channel):

        self.db.cursor.execute(
            """
            INSERT OR IGNORE INTO channels(

                channel_id,

                channel_name,

                channel_url,

                subscribers,

                total_views,

                video_count,

                description,

                country,

                language,

                category,

                keyword_found,

                discovered_from,

                processed

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?,?,?,?,?

            )
            """,
            (

                channel.get("channel_id"),

                channel.get("channel_name"),

                channel.get("channel_url"),

                channel.get("subscribers", 0),

                channel.get("total_views", 0),

                channel.get("video_count", 0),

                channel.get("description", ""),

                channel.get("country", ""),

                channel.get("language", ""),

                channel.get("category", ""),

                channel.get("keyword", ""),

                channel.get("source", ""),

                channel.get("processed", 0)

            )
        )

    # =====================================================

    def save_many(self, channels):

        for channel in channels:

            self.save(channel)

        self.db.commit()

    # =====================================================

    def get_unprocessed(self):

        self.db.cursor.execute(
            """
            SELECT *

            FROM channels

            WHERE processed=0
            """
        )

        return self.db.fetchall()

    # =====================================================

    def mark_processed(self, channel_id):

        self.db.cursor.execute(
            """
            UPDATE channels

            SET processed=1

            WHERE channel_id=?
            """,
            (channel_id,)
        )

        self.db.commit()

    # =====================================================

    def exists(self, channel_id):

        self.db.cursor.execute(
            """
            SELECT 1

            FROM channels

            WHERE channel_id=?

            LIMIT 1
            """,
            (channel_id,)
        )

        return self.db.fetchone() is not None

    # =====================================================

    def total(self):

        self.db.cursor.execute(
            """
            SELECT COUNT(*)

            FROM channels
            """
        )

        return self.db.fetchone()[0]