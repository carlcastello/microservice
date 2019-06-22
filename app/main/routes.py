from flask import Blueprint
from flask_restful import Api

from typing import List

# from app.api.microservice_api import MicroserviceApi
# from app.domain.microservice_service import MicroserviceService
from .api import Api as MainApi
from .services import Service
from .errors import ERRORS


# def get_microservice_domain() -> MicroserviceService:
#     return MicroserviceService()


# def get_routes_blueprint() -> Blueprint:
#     routes_bp = Blueprint('Api', __name__)
#     api = Api(routes_bp, errors=ERRORS)

#     microservice_service: MicroserviceService = get_microservice_domain()

#     api.add_resource(
#         MicroserviceApi,
#         '/<string:user_id>',
#         resource_class_kwargs={'microservice_service': microservice_service}
#     )

#     return routes_bp


def get_routes_blueprint() -> Blueprint:
    routes_bp: Blueprint = Blueprint('main', __name__)

    api: Api = Api(routes_bp, errors=ERRORS)
    api.add_resource(
        MainApi,
        '/<string:user_id>',
        resource_class_kwargs={'service': Service()}
    )

    return routes_bp
