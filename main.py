import pickle
from users import UsersDatabase
from rooms import RoomsDatabase


class Engine:
    """A class handling everything under the hood

        Takes parsed requests and returns content for response
    """

    def __init__(self, user_lookup=None, room_lookup=None):
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
        """processes request of who is currently in a given room

        :param room_id: the room being checked
        :return: an array of usernames for all users who are registered to any event
        """
        pass

    def add_interest(self, user_id: int, interest: str):
        """

        :param user_id: the user who is being given another interest
        :param interest: the interest
        :return: None
        """
        pass

    def remove_interest(self, user_id, interest):
        pass

    def create_event(self, creating_user, room, desired_start: str, desired_end: str):
        """processes a request to create an event

        :param creating_user: the user who created the request.
        :param room: ID of the desired room
        :param desired_start: start time of the event as a string
        :param desired_end: end time of the event as a string"""
        pass


if __name__ == '__main__':
    engine = Engine()
