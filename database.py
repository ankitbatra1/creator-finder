import sqlite3

conn = sqlite3.connect("creators.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS creators(
    channel_id TEXT PRIMARY KEY,
    channel_name TEXT
)
""")

conn.commit()
conn.close()