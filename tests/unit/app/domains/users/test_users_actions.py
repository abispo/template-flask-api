import unittest
from app.domains.users.actions import (
    get_by_id as get_user_by_id, update as update_user,
    create as create_user, get as get_all_users
)

from app.domains.users.models import User
from app.domains.users.actions import create
from tests.unit import BaseUnitTest


class TestUsersActions(BaseUnitTest):
    def test_action_create_should_be_created_new_user(self):
        new_user = create({'name': 'Jose', 'email': 'jose@email.com'})

        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.name, 'Jose')
        self.assertEqual(new_user.email, 'jose@email.com')

