from flask import Flask


def create_app(config_name='development'):
    app = Flask(__name__)

    return app
