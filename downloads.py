import os

from flask import redirect, request, send_file

from app import app

REPORT_DIR = "/srv/reports"


@app.route("/report")
def report():
    name = request.args.get("name", "")
    return send_file(os.path.join(REPORT_DIR, name))


@app.route("/go")
def go():
    return redirect(request.args.get("next", "/"))
