#coding=UTF-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask import render_template_string
from flask.ext import menu

import cidadeiluminada
from cidadeiluminada.base import db, AppJSONEncoder


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    Bootstrap(app)
    menu.Menu(app=app)
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

def tmpl_show_menu():
    return render_template_string(
        """
        {%- for item in current_menu.children %}
            {% if item.active %}*{% endif %}{{ item.text }}
        {% endfor -%}
        """)

@app.route('/protocolos')
@menu.register_menu(app, 'Home', 'Home')
def index():
    return tmpl_show_menu()

@app.route('/protocolos/novo')
@menu.register_menu(app, '.first', 'Novo', order=0)
def first():
    return tmpl_show_menu()

@app.route('/protocolos/protocolos.json')
@menu.register_menu(app, '.second', 'Listar', order=1)
def second():
    return tmpl_show_menu()

if __name__ == '__main__':
    manager.run()
