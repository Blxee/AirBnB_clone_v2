#!/usr/bin/python3
""" 1. HBNB """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ This function Handles the '/' route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function Handles the '/hbnb' route """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
