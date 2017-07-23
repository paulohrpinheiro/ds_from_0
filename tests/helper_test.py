import json


class Fixtures:
    """System fixtures."""

    def read_json_file(cls, filename):
        """Read a JSON fixture file and returns all data."""
        with open(filename) as fp:
            return json.load(fp)

    def __new__(cls):
        """Implement singleton class."""
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        """Loads and makes available all fixtures."""
        if not hasattr(self, 'users'):
            self.users = self.read_json_file('fixtures/user.json')

        if not hasattr(self, 'friendships'):
            self.friendships = self.read_json_file(
                'fixtures/friendship.json'
                )
