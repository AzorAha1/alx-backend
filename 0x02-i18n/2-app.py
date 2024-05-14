#!/usr/bin/env python3
"""this is for flask"""

from flask import request
from flask_babel import Babel
app = __import__('0-app').app
babel = Babel(app)


@babel.localeselector
def get_locale():
    """locale selector to determine preferred language"""
    request.accept_languages.best_match(app.config['LANGUAGES'])
