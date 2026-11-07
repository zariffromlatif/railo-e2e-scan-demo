import os
import sqlite3

DB_PASSWORD = os.environ["DB_PASSWORD"]


def find_user(cursor, user_id):
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    return cursor.fetchone()


def export_users(out_path):
    os.system(f"sqlite3 users.db .dump > {out_path}")


def connect(path="users.db"):
    return sqlite3.connect(path)
