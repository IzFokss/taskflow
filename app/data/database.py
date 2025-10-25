import sqlite3

def init_db():
    conn = sqlite3.connect("taskflow/app/data/storage.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            priority TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'en cours'
        )
    ''')
    conn.commit()
    conn.close()
