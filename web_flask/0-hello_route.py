#!/usr/bin/python3
"""Create a web application display 'Hello HBNB!'"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    return "Hello HBNB!"
