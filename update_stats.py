import sqlite3
from fetch_stats import get_channel_stats

conn = sqlite3.connect("creators.db")
cursor = conn.cursor()

cursor.execute("""
SELECT channel_id
FROM creators
""")

channels = cursor.fetchall()

total = len(channels)

for index, channel in enumerate(channels):

    channel_id = channel[0]

    print(
        f"{index+1}/{total}"
    )

    stats = get_channel_stats(channel_id)

    if stats:

        cursor.execute(
            """
            UPDATE creators
            SET
            subscribers=?,
            total_views=?,
            video_count=?,
            country=?
            WHERE channel_id=?
            """,
            (
                stats["subscribers"],
                stats["total_views"],
                stats["video_count"],
                stats["country"],
                channel_id
            )
        )

conn.commit()
conn.close()

print("Finished")