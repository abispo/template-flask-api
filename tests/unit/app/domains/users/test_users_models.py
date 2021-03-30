import unittest

from app.domains.users.models import User
from database.repository import save
from tests.unit import BaseUnitTest


class TestUsersModels(BaseUnitTest):
    def test_user_model_should_be_serialized(self):
        user = save(User(name='Jose', email='jose@email.com'))
        json = user.serialize()

        self.assertEqual(json['id'], 1)
        self.assertEqual(json['name'], 'Jose')
        self.assertEqual(json['email'], 'jose@email.com')
