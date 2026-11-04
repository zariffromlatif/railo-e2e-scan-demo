import os
from urllib.parse import urlsplit

from flask import redirect, request, send_file

from app import app

REPORT_DIR = "/srv/reports"


def is_safe_redirect(url):
    """A path on this site: no scheme, no host, not protocol-relative, no leading whitespace."""
    if not url or url != url.strip():
        return False
    if url.startswith(("//", "/\\", "\\")):
        return False
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return False
    return url.startswith("/")


@app.route("/report")
def report():
    name = request.args.get("name", "")
    return send_file(os.path.join(REPORT_DIR, name))


@app.route("/go")
def go():
    target = request.args.get("next", "/")
    if not target.startswith("/") or not is_safe_redirect(target):
        target = "/"
    return redirect(target)
