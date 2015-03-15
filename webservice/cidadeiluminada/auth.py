# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, request, abort, redirect, url_for, \
    render_template, session, current_app, flash
from flask.ext.login import UserMixin, make_secure_token, LoginManager, \
    current_user, login_user, logout_user
from flask.ext.principal import Principal, Identity, AnonymousIdentity, \
    identity_changed, identity_loaded, RoleNeed, UserNeed, Permission
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required

from cidadeiluminada.base import db, JSONSerializationMixin

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

admin_permission = Permission(RoleNeed('admin'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(username=user_id).first()


@login_manager.unauthorized_handler
def handle_unauthorized():
    if request.method == 'POST':
        abort(403)
    elif request.method == 'GET':
        return redirect(url_for('auth.login', next=request.path))

bp = Blueprint('auth', __name__, template_folder='templates',
               static_folder='static')


class LoginForm(Form):
    username = TextField('Username', [Required()])
    password = PasswordField('Password', [Required()])
    remember_me = BooleanField('Lembrar de mim')

    def __init__(self, **kwargs):
        Form.__init__(self, **kwargs)
        self.user = None

    def validate(self):
        if Form.validate(self):
            username = self.username.data
            password = self.password.data
            self.user = User.check_auth(username, password)
        return self.user is not None


@bp.route("/cadastro/")
def cadastro():
    return render_template("cadastro.html")


@bp.route("/login/", methods=["GET", "POST"])
def login():
    username = request.args.get('username')
    form = LoginForm(username=username)
    if form.validate_on_submit():
        user = form.user
        login_user(user, remember=form.remember_me.data)
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(user.id))
        return redirect(request.args.get('next') or url_for("index"))
    elif request.method == 'POST':
        flash(u'Usuário ou senha inválidos.', 'login_failed')
    return render_template("login.html", form=form)


@bp.route("/logout/")
def logout():
    for key in ('identity.name', 'identity.auth_type'):
        session.pop(key, None)
    identity_changed.send(current_app._get_current_object(),
                          identity=AnonymousIdentity())
    logout_user()
    return redirect(request.args.get('next') or url_for('index'))


def create_user(username, password, role=None):
    if not role:
        role = 'admin'
    _role = Role.query.filter_by(role=role).first()
    if not _role:
        _role = Role(role=role)
        db.session.add(_role)
        db.session.commit()
    user = User(username=username, password=password, role=_role)
    db.session.add(user)
    db.session.commit()
    return user


def init_app(app, url_prefix='/auth'):
    app.register_blueprint(bp, url_prefix=url_prefix)
    Principal(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        identity.user = current_user
        if not current_user.is_anonymous():
            identity.provides.add(UserNeed(current_user.id))
            if hasattr(current_user, 'role'):
                identity.provides.add(RoleNeed(current_user.role))

    login_manager.init_app(app)


class User(db.Model, UserMixin, JSONSerializationMixin):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(255), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)

    role_id = db.Column(Integer, ForeignKey('role.id'))
    role = relationship('Role')

    @db.validates('password')
    def token_password(self, key, value):
        return make_secure_token(value)

    def get_id(self):
        return self.username

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    @classmethod
    def check_auth(cls, username, password):
        password = make_secure_token(password)
        return cls.query.filter_by(username=username, password=password) \
            .first()


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(String(255), unique=True)

    def __repr__(self):
        return self.role
