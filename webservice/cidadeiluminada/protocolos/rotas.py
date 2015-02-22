# coding: UTF-8
from __future__ import absolute_import
import os

from flask import Blueprint, jsonify, request, current_app,\
    send_from_directory, render_template
from werkzeug import secure_filename

from cidadeiluminada.base import db
from cidadeiluminada.protocolos.models import Protocolo

bp = Blueprint('protocolos', __name__, template_folder='templates')


def init_app(app, url_prefix='/protocolos'):
    app.register_blueprint(bp, url_prefix=url_prefix)


def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in \
        current_app.config['ALLOWED_EXTENSIONS']


@bp.route('/')
def index():
    status = ['NOVO', 'INVALIDO', 'PROCESSADO']
    return render_template('protocolos.html', protocolos=Protocolo.query.all(),
                           status=status)


@bp.route('/protocolos.json')
def lista():
    protocolos = Protocolo.query.all()
    return jsonify(payload=protocolos)


@bp.route('/novo/', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        cod_protocolo = request.form['cod_protocolo']
        arquivo = request.files['file']
        if arquivo and _allowed_file(arquivo.filename):
            filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                                      filename))
            protocolo = Protocolo(cod_protocolo=cod_protocolo,
                                  filename=filename)
            db.session.add(protocolo)
            db.session.commit()
    return render_template('novo.html')


@bp.route('/<protocolo_id>/foto/')
def foto(protocolo_id):
    protocolo = Protocolo.query.filter_by(id=protocolo_id).first_or_404()
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               protocolo.filename)


@bp.route('/<protocolo_id>/status/', methods=['POST'])
def status(protocolo_id):
    protocolo = Protocolo.query.filter_by(id=protocolo_id).first_or_404()
    protocolo.status = request.form['status']
    db.session.commit()
    return jsonify({
        'result': 'OK'
    }), 200
