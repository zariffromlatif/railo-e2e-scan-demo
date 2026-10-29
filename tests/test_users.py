import os
import sqlite3

os.environ.setdefault("DB_PASSWORD", "test-only")

import users  # noqa: E402


def test_find_user_returns_the_row():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id TEXT, name TEXT)")
    conn.execute("INSERT INTO users VALUES ('u1', 'Ada')")
    assert users.find_user(conn.cursor(), "u1") == ("u1", "Ada")


def test_connect_opens_the_database(tmp_path):
    conn = users.connect(str(tmp_path / "users.db"))
    assert conn.execute("SELECT 1").fetchone() == (1,)
