from src.database.manager import DatabaseManager


class JobRepository:

    def __init__(self, db: DatabaseManager):

        self.db = db

    # =====================================================

    def create(self, keyword, search_type):

        self.db.cursor.execute(
            """
            INSERT OR IGNORE INTO jobs(

                keyword,

                search_type,

                status

            )

            VALUES(

                ?,?,'pending'

            )
            """,
            (

                keyword,

                search_type

            )
        )

        self.db.commit()

    # =====================================================

    def start(self, keyword, search_type):

        self.db.cursor.execute(
            """
            UPDATE jobs

            SET status='running'

            WHERE keyword=?

            AND search_type=?
            """,
            (

                keyword,

                search_type

            )
        )

        self.db.commit()

    # =====================================================

    def finish(self, keyword, search_type):

        self.db.cursor.execute(
            """
            UPDATE jobs

            SET status='completed'

            WHERE keyword=?

            AND search_type=?
            """,
            (

                keyword,

                search_type

            )
        )

        self.db.commit()

    # =====================================================

    def completed(self, keyword, search_type):

        self.db.cursor.execute(
            """
            SELECT status

            FROM jobs

            WHERE keyword=?

            AND search_type=?
            """,
            (

                keyword,

                search_type

            )
        )

        row = self.db.fetchone()

        if row is None:

            return False

        return row["status"] == "completed"