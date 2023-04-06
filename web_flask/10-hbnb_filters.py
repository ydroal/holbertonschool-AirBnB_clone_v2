#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def states():
    '''Displays a HTML pagee with a list of all State objects'''

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)

    return render_template(
        '10-hbnb_filters.html',
        states=sorted_states,
        amenities=sorted_amenities
        )


@app.teardown_appcontext
def close_storage():
    '''Closes the storage after each request'''

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
