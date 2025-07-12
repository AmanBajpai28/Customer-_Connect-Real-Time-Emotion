import sqlite3
import os

# Exact same path used in app.py
db_path = "database/feedback.db"
abs_path = os.path.abspath(db_path)
print(f"📂 Creating database at: {abs_path}")

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Create table if not exists
c.execute('''
    CREATE TABLE IF NOT EXISTS emotions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT NOT NULL,
        feedback TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

conn.commit()
conn.close()

print("✅ Database and table created successfully.")
