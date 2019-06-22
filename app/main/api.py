from flask_restful import Resource

from .services import Service


class Api(Resource):

    def __init__(self, service: Service):
        self._service: Service = service

    def get(self, user_id: str):
        return self._service.hello_world(user_id)
