#!/usr/bin/python3
""" 2. C is fun! """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ This function Handles the '/' route """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ This function Handles the '/hbnb' route """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ This function Handles the '/c/<text>' route """
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
