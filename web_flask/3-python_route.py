#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    if '_' in text:
        text = text.replace('_', ' ')

    return f'C {text}'


@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    if '_' in text:
        text = text.replace('_', ' ')

    return f'Python {text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
