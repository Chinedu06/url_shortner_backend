import os
from datetime import timedelta

BASE_DIR=os.path.dirname(os.path.realpath(__file__))


class Config:
    SECRET_KEY='HDHAjabIHAIHKSBIy9ahhioij9J'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    JWT_ACCESS_TOKEN_EXPIRES=timedelta(hours=24)
    JWT_REFRESH_TOKEN_EXPIRES=timedelta(days=1)
    JWT_SECRET_KEY='ksjs8wuUuHujsjjsjjsmsmw'



class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR, 'db.sqlite3' )


class ProductionConfig(Config):
    FLASK_ENV = 'production'

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_DATABASE_URI='sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS=False


config_dict = {
    'dev': DevelopmentConfig ,
    'pro' : ProductionConfig ,
    'test': TestingConfig
}

# import os

# from flask import app


# # Determine the folder of the top-level directory of this project
# BASEDIR = os.path.abspath(os.path.dirname(__file__))

# # app.Config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///file_name.db'

# class Config(object):
#     FLASK_ENV = 'development'
#     DEBUG = False
#     TESTING = False
#     SECRET_KEY = os.getenv('SECRET_KEY', default='BAD_SECRET_KEY')
#     # Since SQLAlchemy 1.4.x has removed support for the 'postgres://' URI scheme,
#     # update the URI to the postgres database to use the supported 'postgresql://' scheme
#     if os.getenv('DATABASE_URL'):
#         SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL').replace("postgres://", "postgresql://", 1)
#     else:
#         SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASEDIR, 'instance', 'app.db')}"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     # Logging
#     LOG_WITH_GUNICORN = os.getenv('LOG_WITH_GUNICORN', default=False)


# class ProductionConfig(Config):
#     FLASK_ENV = 'production'


# class DevelopmentConfig(Config):
#     DEBUG = True


# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
#                                         default=f"sqlite:///{os.path.join(BASEDIR, 'instance', 'test.db')}")
#     WTF_CSRF_ENABLED = False

# config_dict = {
#     'dev': DevelopmentConfig ,
#     'pro' : ProductionConfig ,
#     'test': TestingConfig
# }
