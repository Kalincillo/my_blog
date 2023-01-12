from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config"""
    SECRET_KEY = environ.get('SECRET_KEY')
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class DevConfig:
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True


class ProdConfig:
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


config = {
    'default': Config,
    'development': DevConfig,
    'production': ProdConfig
}
