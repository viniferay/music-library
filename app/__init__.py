from flask import Flask
from flask_caching import Cache

from app.dynamoDB.client import DynamoDBClient
from config import Config

dynamoDB = DynamoDBClient()
cache = Cache(config={'CACHE_TYPE': 'redis'})


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(Config)

    cache.init_app(app)
    dynamoDB.init_client(app)

    from app.genius import bp as genius_client_bp
    app.register_blueprint(genius_client_bp)

    from app.artist import bp as artist_bp
    app.register_blueprint(artist_bp)

    return app
