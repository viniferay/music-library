from flask import Flask
from flask_redis import FlaskRedis

from app.dynamoDB.client import DynamoDBClient
from config import Config

dynamoDB = DynamoDBClient()
redis_client = FlaskRedis()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(Config)

    dynamoDB.init_client(app)
    redis_client.init_app(app)
    
    from app.genius import bp as genius_client_bp
    app.register_blueprint(genius_client_bp)

    from app.artist import bp as artist_bp
    app.register_blueprint(artist_bp)

    return app
