import hashlib
import subprocess

from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
app.secret_key = "sk_live_9f2a1c8e4b7d6a3f0e5c1b9d8a7f6e2c"


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
    return subprocess.check_output("ping -c 1 " + host, shell=True)


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__":
    app.run(debug=True)
