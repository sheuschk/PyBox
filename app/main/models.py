import uuid


class User:
    """ A model to save the data for a User"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User name= {self.name} "

    def get_name(self):
        return self.name


class Lobby:
    """Lobby class, which manges the whole game
    https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
    """

    __instance = None

    @staticmethod
    def get_instance(name='Test'):
        if Lobby.__instance is None:
            Lobby(name)
        return Lobby.__instance

    @staticmethod
    def check_existence():
        if Lobby.__instance is None:
            return None
        else:
            return True

    def __init__(self, name):
        self.name = name
        self.code = uuid.uuid4().hex[0:4]
        self.room = name
        self.users = []
        self.state = 0
        self.game = None

        if Lobby.__instance is not None:
            raise Exception('Simon says: This class is a Singleton')
        else:
            Lobby.__instance = self

    def __str__(self):
        return f"Lobby: {repr(Lobby.get_instance())}, name= {self.name}, code = {self.code} "

    def add_user(self, user: User):
        self.users.append(user)
        return self.users

    def get_users(self):
        return self.users

