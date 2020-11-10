from flask_socketio import send, emit, join_room
from .. import socketio
from .models import Lobby
from .games import GuessGame
from flask import request


@socketio.on('my event', namespace='/')
def print_message(json):
    lobby = Lobby.get_instance()
    join_room(lobby.room)
    print('received message: ' + str(json))


@socketio.on('submit guess')
def submit_guess(json):
    num = json['data']
    print(num)
    lobby = Lobby.get_instance()
    lobby.game.add_choice(request.cookies.get('username'), num)
    # enter it to the game, finally compare it
