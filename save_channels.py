import sqlite3

def save_channels(channels):

    conn = sqlite3.connect("creators.db")
    cursor = conn.cursor()

    for channel in channels:

        cursor.execute(
            """
            INSERT OR IGNORE
            INTO creators
            VALUES (?,?)
            """,

            (
                channel["channel_id"],
                channel["channel_name"]
            )
        )

    conn.commit()
    conn.close()