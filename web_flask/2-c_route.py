#!/usr/bin/python3
"""
This module starts a Flask web application.

Web application listening on 0.0.0.0, port 5000.
Routes:
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C " followed by the value of the text variable
"""

from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Shows "Hello HBNB!" as the message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Shows "HBNB" as the message.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Shows "C "then followe by the output.
    """
    return "C {}".format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
