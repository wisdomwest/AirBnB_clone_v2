#!/usr/bin/python3
"""using db with flask to get  states list"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    state = storage.all("State")
    amenity = storage.all("Amenity")
    place = storage.all("Place")
    return render_template("100-hbnb.html",
                           state=state, amenity=amenity, place=place)


@app.teardown_appcontext
def close_storage(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
