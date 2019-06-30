
from flask_restful import HTTPException
from typing import Dict, Union


ERRORS: Dict[str, Dict[str, Union[int, str]]] = {
    "NoUserException": {
        "status": 404
    }
}


class NoUserException(HTTPException):
    code: int = 404

    def __init__(self, user_id: str):
        super().__init__(f'User with id "{user_id}" does not exit."')