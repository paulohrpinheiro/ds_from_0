from collections import UserList


class User(UserList):
    """Users data store."""

    def __init__(self, *args):
        """Init data with args or with a empty list."""
        if args is not None:
            self.data = list(args)
        else:
            self.data = list()

        self.friendships = list()

    def make_friend(self, user, friend):
        """Register a new friendship."""
        self.friendships.append({'user': user, 'friend': friend})
        self.friendships.append({'user': friend, 'friend': user})

    def friends(self, user_id):
        """Returns a friends list for a given user."""
        return [x['friend'] for x in self.friendships if x['user'] == user_id]

    def how_many_friends(self):
        """Returns how many friends have each user."""
        friends_by_id = [
            (user['id'], self.friends(user['id']))
            for user in self.data
        ]
        num_friends_by_id = [(x[0], len(x[1])) for x in friends_by_id]
        return sorted(num_friends_by_id, key=lambda x: x[1], reverse=True)
