import unittest
import json


class Fixtures:
    def read_json_file(cls, filename):
        with open(filename) as fp:
            return json.load(fp)

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        if not hasattr(self, 'users'):
            self.users = self.read_json_file('fixtures/user.json')

        if not hasattr(self, 'friendships'):
            self.friendships = self.read_json_file(
                'fixtures/friendship.json'
                )
