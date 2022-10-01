import pickle
from users import UsersDatabase
from rooms import RoomsDatabase


class Engine:
    """A class handling everything under the hood

        Takes parsed requests and returns content for response
    """

    def __init__(self, user_lookup: None, room_lookup: None):
        if user_lookup is not None:
            self.users = self.load_users(user_lookup)
        else:
            self.users = UsersDatabase()
        if room_lookup is not None:
            self.rooms = self.load_rooms(room_lookup)
        else:
            self.rooms = RoomsDatabase()

    def load_users(self, user_lookup) -> UsersDatabase:
        return pickle.load(user_lookup)

    def load_rooms(self, room_lookup) -> RoomsDatabase:
        return pickle.load(room_lookup)

    def check_occupants(self, room_id):
        pass

    def add_interest(self, user_id, interest):
        pass

    def remove_interest(self, user_id, interest):
        pass


if __name__ == '__main__':
    pass