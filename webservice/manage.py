#coding=UTF-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('settings')

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
