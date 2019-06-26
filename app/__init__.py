from flask import Flask

from config import config

from app.extensions import DB


def register_extensions(flask_app: Flask) -> None:
    DB.init_app(flask_app)


def create_app(config_name: str) -> Flask:
    flask_app: Flask = Flask(__name__)
    flask_app.config.from_object(config[config_name])
    config[config_name].init_app(flask_app)

    register_extensions(flask_app)

    # Route Blue prints
    from app.main import get_routes_blueprint
    flask_app.register_blueprint(get_routes_blueprint(), url_prefix='')

    return flask_app
