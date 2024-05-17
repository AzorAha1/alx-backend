#!/usr/bin/env python3
"""this is for flask"""

from flask import Flask, render_template, request

from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


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
