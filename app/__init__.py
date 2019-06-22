from flask import Flask
from config import config


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)
    flask_app.config.from_object(config[config_name])
    config[config_name].init_app(flask_app)

    from app.main.routes import get_routes_blueprint
    flask_app.register_blueprint(get_routes_blueprint(), url_prefix='')

    return flask_app
