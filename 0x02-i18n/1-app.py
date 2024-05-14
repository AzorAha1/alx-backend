#!/usr/bin/env python3
"""this is for flask"""

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
