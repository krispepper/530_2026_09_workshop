from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = "World"
    return f"<p>Hello, {escape(name)}</p>"

@app.route("/bye")
def goodbye_world():
    name = "Goodbye"
    return f"<p>Goodbye, {escape(name)}</p>"