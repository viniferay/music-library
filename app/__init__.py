from flask import Flask


def create_app(config_name='development'):
    app = Flask(__name__)

    from app.genius import bp as genius_client_bp
    app.register_blueprint(genius_client_bp)

    return app
