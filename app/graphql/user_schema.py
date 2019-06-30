
from graphene import Connection
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.main.models import User


class UserNode(SQLAlchemyObjectType):
    class Meta:
        model = User


class UserConnection(Connection):
    class Meta:
        node = UserNode
