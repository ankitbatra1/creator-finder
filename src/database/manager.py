import sqlite3

from config import DATABASE_PATH


class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect(DATABASE_PATH)

        self.conn.row_factory = sqlite3.Row

        self.cursor = self.conn.cursor()

        self.create_tables()

    # =====================================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS channels(

            channel_id TEXT PRIMARY KEY,

            channel_name TEXT,

            channel_url TEXT UNIQUE,

            subscribers INTEGER DEFAULT 0,

            total_views INTEGER DEFAULT 0,

            video_count INTEGER DEFAULT 0,

            description TEXT,

            country TEXT,

            language TEXT,

            category TEXT,

            keyword_found TEXT,

            discovered_from TEXT,

            processed INTEGER DEFAULT 0

        )

        """)

        self.conn.commit()

    # =====================================================

    def save_channel(

        self,

        channel

    ):

        self.cursor.execute(

            """

            INSERT OR IGNORE INTO channels(

                channel_id,

                channel_name,

                channel_url,

                keyword_found,

                discovered_from

            )

            VALUES(

                ?,?,?,?,?

            )

            """,

            (

                channel["channel_id"],

                channel["channel_name"],

                channel["channel_url"],

                channel["keyword"],

                channel["source"]

            )

        )

    # =====================================================

    def commit(self):

        self.conn.commit()

    # =====================================================

    def total_channels(self):

        self.cursor.execute(

            """

            SELECT COUNT(*)

            FROM channels

            """

        )

        return self.cursor.fetchone()[0]

    # =====================================================

    def close(self):

        self.conn.commit()

        self.conn.close()