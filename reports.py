import re
import sqlite3
import subprocess

from flask import request

from app import app


@app.route("/user")
def user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("users.db")
    row = conn.execute(f"SELECT name FROM users WHERE id = '{user_id}'").fetchone()
    return {"name": row[0] if row else None}


@app.route("/ping")
def ping():
    host = request.args.get("host", "")
    if not re.fullmatch(r"[A-Za-z0-9.\-:]+", host):
        return {"ok": False}, 400
    subprocess.run(["ping", "-c", "1", host], check=False)
    return {"ok": True}
