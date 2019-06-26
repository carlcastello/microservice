from flask import Blueprint
from flask_restful import Api

from typing import List

from .api import Api as MainApi
from .services import Service
from .errors import ERRORS


def get_routes_blueprint() -> Blueprint:
    routes_bp: Blueprint = Blueprint('main_routes', __name__)

    api: Api = Api(routes_bp, errors=ERRORS)
    api.add_resource(
        MainApi,
        '/<string:user_id>',
        resource_class_kwargs={'service': Service()}
    )

    return routes_bp
