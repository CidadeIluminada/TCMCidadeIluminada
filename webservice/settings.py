#coding=UTF-8
import os

DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'dontcare'

SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp')

ALLOWED_EXTENSIONS = set(['png', 'jpg'])
