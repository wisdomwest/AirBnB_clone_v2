#!/usr/bin/python3
"""using db with flask to get  states list"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    data = storage.all("State")
    return render_template('7-states_list.html', data=data)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
