#!/usr/bin/python3
"""using db with flask to get  states list"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    data = storage.all("State")
    return render_template('8-cities_by_states.html', data=data)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
