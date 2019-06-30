from flask import Blueprint
from flask_restful import Api as FlaskApi
from flask_graphql import GraphQLView

from .schema import schema


def get_routes_blueprint() -> Blueprint:
    routes_bp: Blueprint = Blueprint('graphql_routes', __name__)

    flask_api: FlaskApi = FlaskApi(routes_bp)
    flask_api.add_resource(
        GraphQLView,
        '',
        resource_class_kwargs={
            'schema': schema,
            'graphiql': True
        }
    )

    return routes_bp
