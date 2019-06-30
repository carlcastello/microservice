from graphene import Schema, ObjectType, Field, String
from graphene_sqlalchemy import SQLAlchemyConnectionField

from typing import Any

from app.extensions import DB
from app.main.models import User

from .user_schema import UserNode, UserConnection


class Query(ObjectType):
    'query { users(user_id="") { first_name }}'
    user: Field = Field(UserNode, user_id=String(required=True))
    'query { users { edges { node { first_name } } }}'
    users: SQLAlchemyConnectionField = SQLAlchemyConnectionField(
        UserConnection)

    def resolve_user(self, info, user_id) -> Any:
        query: User = UserNode.get_query(info)
        return query.get(user_id)


schema: Schema = Schema(
    query=Query,
    types=[UserNode],
    auto_camelcase=False
)
