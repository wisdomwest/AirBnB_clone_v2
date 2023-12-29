#!/usr/bin/python3
"""using db with flask to get  states list"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    data = storage.all("State")
    return render_template('9-states.html', data=data)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    data = storage.all("State").values()
    for data in data:
        if data.id == id:
            return render_template("9-states.html", data=data)
    return render_template("9-states.html")

@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
