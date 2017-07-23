import unittest

from . import helper_test

from datascienter import user


class TestFriendship(unittest.TestCase):
    """Verify friendship fixture data."""

    def setUp(self):
        """Get friendships array."""
        fixtures = helper_test.Fixtures()
        self.users = user.User()
        for friendship in fixtures.friendships:
            self.users.make_friend(friendship['user'], friendship['friend'])

    def test_friendships_type(self):
        """Test if friendships is a python list."""
        self.assertTrue(type(self.users.friendships) is list)

    def test_friendships_len(self):
        """Test if friendships has 12*2 elements."""
        self.assertEqual(len(self.users.friendships), 24)

    def test_loaded_data(self):
        """Test if fixture has all data loaded."""
        users = (0, 0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8)
        friends = (1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9)

        friendships = []
        for i in range(len(users)):
            friendships.append({'user': users[i], 'friend': friends[i]})
            friendships.append({'user': friends[i], 'friend': users[i]})

        self.assertEqual(self.users.friendships, friendships)
