import hashlib
import subprocess

from flask import Flask, request, redirect, render_template_string
import shlex
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]


@app.route("/")
def index():
    return "ok"


@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    return render_template_string("<h1>Hello " + name + "</h1>")


@app.route("/go")
def go():
    target = request.args.get("next", "/")
    return redirect(target)


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    return subprocess.check_output(shlex.split("ping -c 1 " + host), shell=False)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__":
    app.run(debug=False)

# SECURITY: Hardened session cookie settings added by Railo.
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# trigger: re-scan probe
