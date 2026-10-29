import sqlite3

DB_PASSWORD = "railo-demo-Pa55word"


def find_user(cursor, user_id):
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchone()


def connect(path="users.db"):
    return sqlite3.connect(path)
