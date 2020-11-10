import random
from flask_socketio import emit
from .models import Lobby
from flask import request


class GuessGame:
    """ A game where every user guesses a number between 0 and 100 and the nearest one wins"""

    def __init__(self):
        self.goal = random.randint(1, 100)
        self.data = {'name': 'Guess a number'}
        self.lobby = Lobby.get_instance()
        self.choice = {}

    def start_game(self):
        print('start game')
        request.namespace = '/'
        emit('start', {'name': 'Guess Game'}, room=getattr(self.lobby, 'room'))

    def add_choice(self, user, num):
        self.choice[user] = num

    def evaluate(self):
        win_diff = 101
        winner = {}
        for user in self.choice.keys():
            diff = abs(self.goal - int(self.choice[user]))
            if diff <= win_diff:
                win_diff = diff
                winner[user] = self.choice[user]

        return winner

