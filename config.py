import platform
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):

    SECRET_KEY = "".join(tuple(platform.uname()._asdict().values()) +
                         platform.python_build())

    BASEDIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                            'sqlite:///' + os.path.join(BASEDIR, 'jp.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False



