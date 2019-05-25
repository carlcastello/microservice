from flask_restful import Resource

from app.domain.microservice_service import MicroserviceService


class MicroserviceApi(Resource):

    def __init__(self, microservice_service: MicroserviceService):
        self._microservice_service: MicroserviceService = microservice_service

    def get(self, user_id: str):
        return self._microservice_service.hello_world(user_id)
