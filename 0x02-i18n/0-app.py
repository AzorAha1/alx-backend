#!/usr/bin/env python3
"""this is for flask"""


from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
