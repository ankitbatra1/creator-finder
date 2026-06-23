# top_channels.py

import sqlite3

conn = sqlite3.connect("creators.db")
cursor = conn.cursor()

cursor.execute("""
SELECT
channel_name,
subscribers
FROM creators
ORDER BY subscribers DESC
LIMIT 20
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()