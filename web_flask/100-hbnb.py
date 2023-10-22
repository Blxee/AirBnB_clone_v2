#!/usr/bin/python3
''' Module for 12. HBNB is alive! task '''
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    ''' This function Handles the "/hbnb" route '''
    template = '100-hbnb.html'
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template(template,
                           states=states,
                           amenities=amenities,
                           places=places)


@app.teardown_appcontext
def clean(exception):
    """ Removes the SQLAlchemy session """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
