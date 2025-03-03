#!/usr/bin/python3
''' 8. List of states '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' This function Handles the "/states_list" route '''
    return render_template(
        '7-states_list.html',
        states=sorted(storage.all(State).values(), key=lambda s: s.name))


@app.teardown_appcontext
def clean(exception):
    """ Removes the SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
