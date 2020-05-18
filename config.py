from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration variables from .env file."""

    # General Flask Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = environ.get('FLASK_ENV')
    FLASK_APP = 'main.py'
    FLASK_DEBUG = 1

    # Database
    DB_PASSWORD = environ.get('DB_PASSWORD')
    DB_USER = environ.get('DB_USER')
    DB_NAME = environ.get('DB_NAME')
    SQLALCHEMY_DATABASE_URI = "postgresql://"+DB_USER+":"+DB_PASSWORD+"@localhost:5432/"+DB_NAME
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False