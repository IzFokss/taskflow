# app/core/task_manager.py
import sqlite3

DB_PATH = "taskflow/app/data/storage.db"

def add_task(title, description, priority, due_date):
    """Ajoute une tâche dans la base de données."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, description, priority, due_date, status)
        VALUES (?, ?, ?, ?, 'en cours')
    """, (title, description, priority, due_date))
    conn.commit()
    conn.close()

def get_all_tasks():
    """Récupère toutes les tâches."""
    conn = sqlite3.connect(DB_PATH) 
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(title):
    """Supprime une tâche par son titre."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE title = ?", (title,))
    conn.commit()
    conn.close()
