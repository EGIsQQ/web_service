import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
path_db = os.path.join(BASE_DIR, 'movies.db')

class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{path_db}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
