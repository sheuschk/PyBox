from flask import Flask
from config import Config
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app(config_class=Config, debug=False):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    app.debug = debug

    socketio.init_app(app)
    return app
