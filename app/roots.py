from flask_restful import Api
from flask import Blueprint

from typing import List

from app.views.mircroservice_views import Microservice
from app.exceptions import ERRORS


def get_routes_blueprint() -> Blueprint:
    routes_bp = Blueprint('api', __name__)
    api = Api(routes_bp, errors=ERRORS)

    api.add_resource(
        Microservice,
        '/<str:user_id>',
    )

    return api
