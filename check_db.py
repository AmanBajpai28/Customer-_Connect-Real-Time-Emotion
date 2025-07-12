import sqlite3

conn = sqlite3.connect("database/feedback.db")
c = conn.cursor()

# Check what tables exist
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = c.fetchall()

print("📦 Tables found in DB:")
for table in tables:
    print(" -", table[0])

conn.close()
