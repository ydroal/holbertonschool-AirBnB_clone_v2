#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    '''Displays a HTML pagee with a list of all State objects'''

    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>')
def states_id(id):
    '''
    Displays a HTML page with the list of City objects linked to the State
    '''

    states = storage.all(State).values()
    state = None

    for s in states:
        if s.id == id:
            state = s
            break

    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def close_storage():
    '''Closes the storage after each request'''

    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
