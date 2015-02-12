# coding: UTF-8
from __future__ import absolute_import

from flask import Blueprint, jsonify

from cidadeiluminada.protocolos.models import Protocolo

bp = Blueprint('protocolos', __name__)


def init_app(app, url_prefix='/protocolos'):
    app.register_blueprint(bp, url_prefix=url_prefix)


@bp.route('/')
def index():
    return 'Hello protocolos'


@bp.route('/protocolos.json')
def lista():
    protocolos = Protocolo.query.all()
    return jsonify(payload=protocolos)


@bp.route('/novo/', methods=['POST'])
def novo():
    pass
