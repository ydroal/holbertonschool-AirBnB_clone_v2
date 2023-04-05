#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    '''Displays a HTML page with a list of states and their cities'''

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def close_storage():
    '''Closes the storage after each request'''

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
