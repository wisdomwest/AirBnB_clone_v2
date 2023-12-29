#!/usr/bin/python3
"""using db with flask to get  states list"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    state = storage.all("State")
    amenity = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
                           state=state, amenity=amenity)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
