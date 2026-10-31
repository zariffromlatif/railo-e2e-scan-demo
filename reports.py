import os
import sqlite3

from flask import request

from app import app


@app.route("/user")
def user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("users.db")
    row = conn.execute("SELECT name FROM users WHERE id = ?", (user_id,)).fetchone()
    return {"name": row[0] if row else None}


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    os.system(f"ping -c 1 {host}")
    return {"ok": True}
