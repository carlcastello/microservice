from flask import Blueprint
from flask_restful import Api as FlaskApi

from typing import List

from .api import Api
from .services import Service
from .errors import ERRORS


def get_routes_blueprint() -> Blueprint:
    routes_bp: Blueprint = Blueprint('main_routes', __name__)

    flask_api: FlaskApi = FlaskApi(routes_bp, errors=ERRORS)
    flask_api.add_resource(
        Api,
        '/<string:user_id>',
        resource_class_kwargs={'service': Service()}
    )

    return routes_bp
