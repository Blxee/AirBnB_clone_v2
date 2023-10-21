#!/usr/bin/python3
""" 6. Odd or even? """
from flask import Flask, render_template
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


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text=None):
    """ This function Handles the '/python/<text>' route """
    if text is None:
        text = 'is cool'
    return f"Python {escape(text.replace('_', ' '))}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ This function Handles the '/number/<n>' route """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ This function Handles the '/number_template/<n>' route """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ This function Handles the '/number_odd_or_even/<n>' route """
    text = f"{n} is { 'even' if n % 2 == 0 else 'odd' }"
    return render_template("6-number_odd_or_even.html", text=text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
