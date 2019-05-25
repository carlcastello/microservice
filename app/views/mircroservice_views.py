from flask_restful import Resource


class Microservice(Resource):

    def get(self, user_id: str):
        return f'Hello world! {user_id}'
