from random import getrandbits


class RoomsDatabase(dict):
    """theoretically, this is a way to interact with a database of rooms. In practice, this is a dictionary"""

    def __init__(self, *args):
        super.__init__(self, args)

    def generate_id(self):
        """returns a random 16 bit number not already in the database as a key"""
        new_id = getrandbits(8)
        while new_id in self.keys():
            new_id = getrandbits(8)
        return new_id

    def add_room(self, name, description, capacity, schedule):
        """adds a room to the database and returns the room's id"""
        new_id = self.generate_id()
        new_room = Room(self, new_id, name, description, capacity, schedule)
        self[new_id] = new_room
        return new_id


class Room:
    """A room where events can take place"""

    def __init__(self, parent, id, name, description, capacity, schedule=[], img=None):
        self.parent = parent
        self.id = id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.schedule = schedule
        self.img = img
