#!/usr/bin/python3
"""
This module starts a Flask web application.

Web application listening on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    (replace underscore _ symbols with a space)
    /python/(<text>): display “Python ”, followed by the value of the text
    variable (replace underscore _ symbols with a space)
    The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Display "Hello HBNB!" message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display "HBNB" message.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Display "C " followed by the value of the text variable.
    """
    return "C {}".format(escape(text.replace('_', ' ')))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Display "Python " followed by the value of the text variable.
    If no text is provided, use the default value "is cool".
    """
    return "Python {}".format(escape(text.replace('_', ' ')))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Display "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
