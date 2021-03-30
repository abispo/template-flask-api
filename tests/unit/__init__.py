import unittest

from app import create_app, db


class BaseUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self._app = create_app()
        self.app_context = self._app.app_context()
        self.app_context.push()
        db.create_all(app=self._app)
        self._client = self._app.test_client()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all(app=self._app)
        self.app_context.pop()
