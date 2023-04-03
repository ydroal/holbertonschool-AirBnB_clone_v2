#!/usr/bin/python3
'''Module for starting Flask application'''

from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>')
def number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
