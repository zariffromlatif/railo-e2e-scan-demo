import os

from flask import abort, redirect, request, send_file

from app import app

REPORT_DIR = "/srv/reports"


@app.route("/report")
def report():
    name = request.args.get("name", "")
    path = os.path.join(REPORT_DIR, name)
    if os.path.commonpath([os.path.realpath(path), os.path.realpath(REPORT_DIR)]) != os.path.realpath(REPORT_DIR):
        abort(404)
    return send_file(path)


@app.route("/go")
def go():
    return redirect(request.args.get("next", "/"))
