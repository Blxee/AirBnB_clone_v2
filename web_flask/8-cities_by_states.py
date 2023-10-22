#!/usr/bin/python3
''' 9. Cities by states '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    ''' This function Handles the "/cities_by_states" route '''
    return render_template(
        '8-cities_by_states.html',
        states=storage.all(State).values())


@app.teardown_appcontext
def clean(exception):
    """ Removes the SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
