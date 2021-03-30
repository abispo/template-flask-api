from tests.unit import BaseUnitTest
from unittest.mock import patch, MagicMock, Mock


class TestUsersViews(BaseUnitTest):

    @patch('app.domains.users.views.get_users')
    def test_get_users_should_be_1(self, get_user_mock):
        # Arrange
        obj = Mock()
        obj.serialize = MagicMock(return_value={})
        get_user_mock.return_value = [obj]

        # Action
        response = self._client.get('/users')
        data = response.get_json()

        # Assertions
        self.assertEqual(len(data), 1)
        get_user_mock.assert_called_once()
