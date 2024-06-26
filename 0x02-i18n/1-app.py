#!/usr/bin/env python3
"""this is for flask"""

from flask import render_template
from flask_babel import Babel
app = __import__('0-app').app
babel = Babel(app)


class Config:
    """Config class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index1():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
