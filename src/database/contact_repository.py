from src.database.manager import DatabaseManager


class ContactRepository:

    def __init__(self, db: DatabaseManager):

        self.db = db

    # =====================================================

    def save(self, contact):

        self.db.cursor.execute(
            """
            INSERT OR REPLACE INTO contacts(

                channel_id,

                youtube_email,
                youtube_phone,

                website,

                website_email,
                website_phone,

                instagram,

                instagram_email,
                instagram_phone,

                linktree,

                final_email,
                final_phone,

                email_source,
                phone_source,

                completed

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?

            )
            """,
            (

                contact.get("channel_id"),

                contact.get("youtube_email", ""),
                contact.get("youtube_phone", ""),

                contact.get("website", ""),

                contact.get("website_email", ""),
                contact.get("website_phone", ""),

                contact.get("instagram", ""),

                contact.get("instagram_email", ""),
                contact.get("instagram_phone", ""),

                contact.get("linktree", ""),

                contact.get("final_email", ""),
                contact.get("final_phone", ""),

                contact.get("email_source", ""),
                contact.get("phone_source", ""),

                contact.get("completed", 0)

            )

        )

        self.db.commit()

    # =====================================================

    def get_pending(self):

        self.db.cursor.execute(
            """
            SELECT *

            FROM contacts

            WHERE completed=0
            """
        )

        return self.db.fetchall()

    # =====================================================

    def mark_completed(self, channel_id):

        self.db.cursor.execute(
            """
            UPDATE contacts

            SET completed=1

            WHERE channel_id=?
            """,
            (channel_id,)
        )

        self.db.commit()

    # =====================================================

    def total(self):

        self.db.cursor.execute(
            """
            SELECT COUNT(*)

            FROM contacts
            """
        )

        return self.db.fetchone()[0]