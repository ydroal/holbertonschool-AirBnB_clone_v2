#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    '''Displays a HTML pagee with a list of all State objects'''

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_storage():
    '''Remove the current SQLAlchemy Session'''

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
