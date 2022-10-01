from random import getrandbits


class UsersDatabase(dict):
    """theoretically, this is a way to interact with a database of users. In practice, this is a dictionary"""

    def __init__(self, *args):
        super.__init__(self, args)

    def generate_id(self):
        """returns a random 16 bit number not already in the database as a key"""
        new_id = getrandbits(32)
        while new_id in self.keys():
            new_id = getrandbits(32)
        return new_id

    def add_user(self, name):
        """adds a room to the database and returns the room's id"""
        new_id = self.generate_id()
        new_user = User(self, new_id, name)
        self[new_id] = new_user
        return new_id


class User:
    """A user of system"""

    def __init__(self, parent, id, name, description, capacity, schedule=[]):
        self.parent = parent
        self.id = id
        self.name = name
        self.schedule = schedule
