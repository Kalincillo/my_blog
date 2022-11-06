from os import environ, path
from dotenv import load_dotenv

TESTING = True
DEBUG = True
FLASK_ENV = 'development'


basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base codnfig"""
    SECRET_KEY = environ.get('SECRET_KEY')
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'

class DevConfig:
    pass

class ProdConfig:
    pass


