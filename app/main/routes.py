from . import bp
from flask import render_template, request, redirect, url_for, make_response, Response, jsonify
from .forms import CreateLobby, RegisterUser, StartGame
from .models import User, Lobby
from .games import GuessGame


@bp.route('/', methods=['GET', 'POST'])
def home():
    """home page for the whole game"""
    user = request.cookies.get('username')
    user_lobby = request.cookies.get('lobby')
    if not Lobby.check_existence():
        return redirect(url_for('main.lobby_start'))
    lobby = Lobby.get_instance()
    if lobby.state == 0:
        return redirect(url_for('main.lobby_wait'))
    if user is None or user_lobby != getattr(lobby, 'code'):
        resp = make_response(redirect(url_for('main.join')))
        resp.delete_cookie('username')
        resp.delete_cookie('lobby')
        return resp
    return render_template('home.html', name=user, lobby_name=getattr(lobby, 'name'))


@bp.route('/join', methods=['GET', 'POST'])
def join():
    """A User gets created and joins the lobby"""
    form = RegisterUser()
    username = request.cookies.get('username')
    # Check if the User is already set
    if username is not None:
        return redirect(url_for('main.home'))

    # Add the User to a lobby
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        lobby = Lobby.get_instance()
        if getattr(lobby, 'code') == form.code.data:
            user = User(name=name)
            lobby.add_user(user)
            resp = make_response(redirect(url_for('main.home')))
            resp.set_cookie('username', name)
            resp.set_cookie('lobby', getattr(lobby, 'code'))

            # Update the lobby and the lobby_wait
            return resp
        else:
            return render_template('join.html', form=form, fail='Wrong code')
    return render_template('join.html', form=form)


@bp.route('/lobby/create', methods=['GET', 'POST'])
def lobby_start():
    """ create a lobby, after Creation redirects to the waiting screen for the Users"""
    form = CreateLobby()
    if Lobby.check_existence() is True:
        return redirect(url_for('main.lobby_wait'))
    if request.method == 'POST' and form.validate_on_submit():
        lobby = Lobby.get_instance(name=form.name.data)
        return redirect(url_for('main.lobby_wait'))  # better a redirect

    # delete cookies from old games by initializing the game
    resp = make_response(render_template('lobby_start.html', form=form))
    resp.delete_cookie('username')
    resp.delete_cookie('lobby')
    return resp


@bp.route('/lobby')
def lobby():
    """ The route for the lobby during the whole game """
    if not Lobby.check_existence():
        return redirect(url_for('main.lobby_start'))
    lobby = Lobby.get_instance()
    if lobby.state == 0:
        return redirect(url_for('main.lobby_wait'))
    name = getattr(lobby, 'name')
    return render_template('lobby.html', lobby_name=name)


@bp.route('/lobby/wait', methods=['GET', 'POST'])
def lobby_wait():
    """ Display information, while waiting for Users """
    form = StartGame()
    if not Lobby.check_existence():
        return redirect(url_for('main.lobby_start'))
    lobby = Lobby.get_instance()
    if lobby.state != 0:
        return redirect(url_for('main.lobby'))
    if form.validate_on_submit():
        lobby.state = 1
        # register the games here
        return redirect(url_for('main.lobby'))
    code = getattr(lobby, 'code')
    name = getattr(lobby, 'name')
    return render_template('lobby_wait.html', name=name, code=code, form=form)


@bp.route('/ajax/lobby/users')
def lobby_users():
    """ Displays all Users in the lobby waiting screen"""
    data = {}
    if not Lobby.check_existence():
        return jsonify(data)
    lobby = Lobby.get_instance()
    users = lobby.get_users()
    user_names = []
    for user in users:
        user_names.append(user.get_name())
    data = {'users': user_names}
    return jsonify(data)


@bp.route('/lobby/status/change', methods=['POST'])
def change_status():
    """
    @description:
            Changes the actual game of the lobby. A lobby has always just one game at a time.
    @args:
            - json: param name to create the specific game
                    more params if they are necessary for the game
    """
    game_choice = request
    print(game_choice.form['name'])
    data = {}
    lobby = Lobby.get_instance()

    """ A Factory pattern could be added here, which just needs the name of the game"""

    if game_choice.form['name'] == 'guess':
        lobby.state = 'guess'
        game = GuessGame()
        data = getattr(game, 'data')
        lobby.game = game
        game.start_game()

    return jsonify(data)


@bp.route('/game/evaluate', methods=['GET'])
def game_evaluate():
    lobby = Lobby.get_instance()
    winner = lobby.game.evaluate()
    result = {'game': lobby.game.data,
              'winner': winner,
              'result': lobby.game.goal}
    return jsonify(result)
