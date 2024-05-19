#!/usr/bin/env python3
"""this is for flask"""

from flask import Flask, render_template, request, g

from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """_summary_

    Returns:
        _type_: _description_
    """
    login_as = request.args.get('login_as')
    if login_as in users:
        return users[int(login_as)]
    else:
        None

app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def index3():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
