from flask import Flask

from app.dynamoDB.client import DynamoDBClient
from config import Config

dynamoDB = DynamoDBClient()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(Config)

    dynamoDB.init_client(app)

    from app.genius import bp as genius_client_bp
    app.register_blueprint(genius_client_bp)

    from app.artist import bp as artist_bp
    app.register_blueprint(artist_bp)

    return app
