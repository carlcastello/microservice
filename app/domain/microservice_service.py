from typing import Dict


class MicroserviceService:

    def __init__(self):
        pass

    def hello_world(self, user_id: str) -> str:
        print(f'Hello world! {user_id}')
        return f'Hello world! {user_id}'
