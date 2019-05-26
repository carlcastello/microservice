from flask import Flask


def create_app(config_name: str) -> Flask:
    flask_app = Flask(__name__)

    from app.roots import get_routes_blueprint
    flask_app.register_blueprint(get_routes_blueprint())

    return flask_app
