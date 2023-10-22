#!/usr/bin/python3
''' 11. HBNB filters '''
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_list():
    ''' This function Handles the "/states/<id>" route '''
    template = '10-hbnb_filters.html'
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(template, states=states, amenities=amenities)


@app.teardown_appcontext
def clean(exception):
    """ Removes the SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
