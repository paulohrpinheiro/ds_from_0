import unittest

from . import helper_test

from datascienter import user


class TestUser(unittest.TestCase):
    """Verify structure for data."""

    def setUp(self):
        """Get users array."""
        fixtures = helper_test.Fixtures()
        self.users = user.User()
        [self.users.append(x) for x in fixtures.users]

    def test_users_len(self):
        """Test if users has 10 elements."""
        self.assertEqual(len(self.users), 10)

    def test_loaded_data(self):
        """Test if fixture has all data loaded."""
        users = 'Hero Dunn Sue Chi Thor Clive Hicks Devin Kate Klein'.split()

        for index in range(len(self.users)):
            user = users[index]
            with self.subTest(user=user, user_id=index):
                self.assertEqual(user, self.users[index]['name'])
                self.assertEqual(index, self.users[index]['id'])
