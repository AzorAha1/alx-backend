#!/usr/bin/env python3
"""this is for flask"""

from flask import Flask, render_template, request

from flask_babel import Babel


class Config:
    """Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(app)


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """locale selector to determine preferred language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index3():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
