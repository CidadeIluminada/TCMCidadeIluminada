#coding=UTF-8

from flask import Flask
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

import cidadeiluminada
from cidadeiluminada.base import db, AppJSONEncoder


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('settings')
    app.config.from_pyfile('settings_local.py', silent=True)
    app.json_encoder = AppJSONEncoder
    app.secret_key = app.config.get('SECRET_KEY')
    cidadeiluminada.init_app(app)
    return app

app = create_app()
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())


@app.route('/')
def index():
    return 'Hello world'

if __name__ == '__main__':
    manager.run()
