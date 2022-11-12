from os import environ, path
from dotenv import load_dotenv

TESTING = True
DEBUG = True
FLASK_ENV = 'development'

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config"""
    SECRET_KEY = environ.get('SECRET_KEY')
    # SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True



class ProdConfig:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
