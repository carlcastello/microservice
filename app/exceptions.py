from flask_restful import HTTPException
from typing import Dict, Union

ERRORS: Dict[str, Dict[str, Union[int, str]]] = {
    "NoIdException": {
        "message": "Id is required",
        "status": 400
    }
}


class NoIdException(HTTPException):
    code: int = 400
