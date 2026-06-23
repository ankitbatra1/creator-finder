# update_db.py

import sqlite3

conn = sqlite3.connect("creators.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE creators
ADD COLUMN subscribers INTEGER
""")

cursor.execute("""
ALTER TABLE creators
ADD COLUMN total_views INTEGER
""")

cursor.execute("""
ALTER TABLE creators
ADD COLUMN video_count INTEGER
""")

cursor.execute("""
ALTER TABLE creators
ADD COLUMN country TEXT
""")

conn.commit()
conn.close()

print("Database Updated")