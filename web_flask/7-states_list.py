#!/usr/bin/python3
"""
    starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def stately():
    return render_template("7-states_list.html", db=storage.all(State))


@app.teardown_appcontext
def some_method(content):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
