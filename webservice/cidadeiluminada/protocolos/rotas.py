# coding: UTF-8
from __future__ import absolute_import
import os

from flask import Blueprint, jsonify, request, current_app,\
    send_from_directory, render_template
from flask.ext.login import login_required
from werkzeug import secure_filename

from cidadeiluminada.base import db
from cidadeiluminada.services import postmon
from cidadeiluminada.protocolos.models import Protocolo
from cidadeiluminada.protocolos.forms import ProtocoloForm

bp = Blueprint('protocolos', __name__, template_folder='templates',
               static_folder='static')


def init_app(app, url_prefix='/protocolos'):
    app.register_blueprint(bp, url_prefix=url_prefix)


def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in \
        current_app.config['ALLOWED_EXTENSIONS']


@bp.route('/')
@login_required
def index():
    return render_template('protocolos.html')


@bp.route('/protocolo.json')
def buscar_cod_protocolo():
    cod_protocolo = request.args['cod_protocolo']
    protocolo = Protocolo.query.filter_by(cod_protocolo=cod_protocolo).first()
    return jsonify(payload=protocolo)


@bp.route('/protocolos.json')
@login_required
def lista():
    protocolos = Protocolo.query.order_by(Protocolo.id).all()
    return jsonify(payload=protocolos)


@bp.route('/novo/', methods=['POST'])
def novo():
    form = ProtocoloForm()
    import ipdb; ipdb.set_trace();
    cod_protocolo = request.form['cod_protocolo']
    arquivo = request.files['file']
    cep = request.form['cep']
    estado = request.form.get('estado')
    cidade = request.form.get('cidade')
    bairro = request.form.get('bairro')
    logradouro = request.form.get('logradouro')
    numero = request.form.get('numero')
    if _allowed_file(arquivo.filename):
        filename = secure_filename(arquivo.filename)
        arquivo.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                                  filename))
        protocolo = Protocolo(cod_protocolo=cod_protocolo, cep=cep,
                              logradouro=logradouro, filename=filename,
                              bairro=bairro, numero=numero, cidade=cidade,
                              estado=estado)
        if not protocolo.has_full_address():
            endereco = postmon.get_by_cep(protocolo.cep)
            protocolo.estado = endereco['estado']
            protocolo.cidade = endereco['cidade']
            protocolo.bairro = endereco['bairro']
            protocolo.logradouro = endereco['logradouro']
        db.session.add(protocolo)
        db.session.commit()
        return jsonify({'status': 'OK'}), 200
    else:
        return jsonify({'status': 'ERROR'}), 400


@bp.route('/novo/form/')
@login_required
def novo_pagina():
    return render_template('novo.html')


@bp.route('/<protocolo_id>/foto/')
@login_required
def foto(protocolo_id):
    protocolo = Protocolo.query.filter_by(id=protocolo_id).first_or_404()
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               protocolo.filename)


@bp.route('/<protocolo_id>/status/', methods=['POST'])
@login_required
def status(protocolo_id):
    protocolo = Protocolo.query.filter_by(id=protocolo_id).first_or_404()
    protocolo.status = request.json['status']
    db.session.commit()
    return jsonify({
        'result': 'OK'
    }), 200
