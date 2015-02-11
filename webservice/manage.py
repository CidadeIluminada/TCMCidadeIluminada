#coding=UTF-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from cidadeiluminada import base
from cidadeiluminada import protocolos


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('settings')
    app.config.from_pyfile('settings_local.py', silent=True)
    app.secret_key = app.config.get('SECRET_KEY')
    base.init_app(app)
    return app

db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    manager.run()
