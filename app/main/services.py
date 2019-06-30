from .models import User

from .errors import NoUserException


class Service:

    def __init__(self):
        pass

    def hello_world(self, user_id: str):
        user: User = User.query.get(user_id)
        if user is None:
            raise NoUserException(user_id)
        return f'hello {user.first_name} {user.last_name}'
