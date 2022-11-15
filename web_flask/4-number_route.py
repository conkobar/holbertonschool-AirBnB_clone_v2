#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def cisfun(text):
    return "C {}".format(
        text.replace("_", " ")
    )


@app.route('/python/')
@app.route('/python/<text>')
def simpleisbest(text="is cool"):
    return "Python {}".format(
        text.replace("_", " ")
    )


@app.route('/number/<int:n>')
def numbz(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
