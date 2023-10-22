#!/usr/bin/python3
''' 9. Cities by states '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list(id=None):
    ''' This function Handles the "/states/<id>" route '''
    template = '9-states.html'
    states = storage.all(State).values()
    if id is None:
        return render_template(template, states=states)
    else:
        for state in states:
            if state.id == id:
                return render_template(template, state=state)
        return render_template(template)


@app.teardown_appcontext
def clean(exception):
    """ Removes the SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
