#!/usr/bin/env python3
"""this is for flask"""

from flask import render_template, request
from flask_babel import Babel
app = __import__('0-app').app
babel = Babel(app)


@babel.localeselector
def get_locale():
    """locale selector to determine preferred language"""
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index2():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
