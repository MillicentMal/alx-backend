#!/usr/bin/env python3
"""
basic flask app : Hello World
"""
from urllib import request
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ configure babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')


@babel.localeselector
def get_locale():
    """
    returns best match languages
    """
    return request.accept_languages.best_match(['en', 'fr'])


@app.route("/")
def index():
    """
    returns index.html
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
