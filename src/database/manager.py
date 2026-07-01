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

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(

            channel_id TEXT PRIMARY KEY,

            youtube_email TEXT,

            youtube_phone TEXT,

            website TEXT,

            website_email TEXT,

            website_phone TEXT,

            instagram TEXT,

            instagram_email TEXT,

            instagram_phone TEXT,

            linktree TEXT,

            final_email TEXT,

            final_phone TEXT,

            email_source TEXT,

            phone_source TEXT,

            completed INTEGER DEFAULT 0

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs(

            keyword TEXT,

            search_type TEXT,

            status TEXT,

            PRIMARY KEY(keyword, search_type)

        )
        """)

        self.conn.commit()

    # =====================================================

    def commit(self):

        self.conn.commit()

    # =====================================================

    def fetchone(self):

        return self.cursor.fetchone()

    # =====================================================

    def fetchall(self):

        return self.cursor.fetchall()

    # =====================================================

    def close(self):

        self.conn.commit()

        self.conn.close()