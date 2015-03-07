#coding=UTF-8
from __future__ import absolute_import

from flask import Flask, redirect, url_for
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.assets import Environment

import cidadeiluminada
from cidadeiluminada import auth
from cidadeiluminada.base import db, AppJSONEncoder


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    Environment(app)
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
    return redirect(url_for('protocolos.index'))


@app.context_processor
def menu_items():
    return {
        'menu_items': [
            (u'Protocolos', 'protocolos.index'),
            (u'(ALPHA) Novo protocolo', 'protocolos.novo_pagina'),
            (u'Sair', 'auth.logout'),
        ]
    }


@manager.command
def criar_usuario(username, password, role='admin'):
    auth.create_user(username, password, role)

if __name__ == '__main__':
    manager.run()
