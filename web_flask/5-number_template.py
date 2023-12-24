#!/usr/bin/python3
"""Using templates"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    txt = text.replace('_', ' ')
    return f"C { txt }"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    txt = text.replace('_', ' ')
    return f"Python { txt }"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{ n } is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', data=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
