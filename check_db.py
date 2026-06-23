import sqlite3

conn = sqlite3.connect("creators.db")

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM creators"
)

print(cursor.fetchone())

conn.close()