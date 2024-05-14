#!/usr/bin/env python3
"""this is for flask"""


from flask import Flask
from flask import render_template
from flask_babel import Babel

app = Flask(__name__)

babel = Babel(app)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
