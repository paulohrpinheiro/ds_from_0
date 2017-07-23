import unittest
import json


class Fixtures:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        with open('fixtures/user.json') as fp:
            self.users = json.load(fp)

        with open('fixtures/friendship.json') as fp:
            self.friendships = json.load(fp)
