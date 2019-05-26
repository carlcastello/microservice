from uuid import uuid4
from unittest import TestCase, mock

from app import create_app
from app.domain.microservice_service import MicroserviceService


class MicroserviceApiTest(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    @mock.patch.object(MicroserviceService, 'hello_world')
    def test_post(self, hello_world: mock.MagicMock):
        hello_world.return_value = {}
        response = self.client.get(f'/{str(uuid4())}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(hello_world.called, True)
