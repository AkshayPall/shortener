# author: Akshay Pall

import os
from flask import Flask

# Return app instance
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'shortener.sqlite')
    )

    if test_config is None:
        # load prod config
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # simple hello page for verification
    @app.route('/running')
    def isRunning():
        return 'Running'

    return app
