# coding: UTF-8
from __future__ import absolute_import
import os

from flask import Blueprint, jsonify, request, current_app, redirect, url_for,\
    send_from_directory, render_template, render_template_string
from werkzeug import secure_filename

from cidadeiluminada.base import db
from cidadeiluminada.protocolos.models import Protocolo

bp = Blueprint('protocolos', __name__)


def init_app(app, url_prefix='/protocolos'):
    app.register_blueprint(bp, url_prefix=url_prefix)


def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in \
        current_app.config['ALLOWED_EXTENSIONS']


@bp.route('/')
def index():
    template = '''
    {%  for protocolo in protocolos %}
        {{ protocolo.id }} <br>
        {{ protocolo.cod_protocolo }} <br>
        {{ protocolo.timestamp }} <br>
        <a href={{ url_for('.foto', protocolo=protocolo.id) }}> Arquivo</a>
        <hr>
    {%  endfor %}
    '''
    return render_template_string(template, protocolos=Protocolo.query.all())


@bp.route('/protocolos.json')
def lista():
    protocolos = Protocolo.query.all()
    return jsonify(payload=protocolos)


@bp.route('/novo/', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        cod_protocolo = request.form['cod_protocolo']
        print cod_protocolo
        arquivo = request.files['file']
        if arquivo and _allowed_file(arquivo.filename):
            filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                                      filename))
            protocolo = Protocolo(cod_protocolo=cod_protocolo,
                                  filename=filename)
            db.session.add(protocolo)
            db.session.commit()
            #return redirect(url_for('.index'))
    return '''
    <!doctype html>
    <title>Novo protocolo</title>
    <h1>Novo protocolo</h1>
    <form action="" method=post enctype=multipart/form-data>
        <input type=text name=cod_protocolo><br>
        <input type=file name=file><br>
        <input type=submit value=Upload>
    </form>
    '''


@bp.route('/<protocolo_id>/foto/')
def foto(protocolo_id):
    protocolo = Protocolo.query.filter_by(id=protocolo_id).first_or_404()
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],
                               protocolo.filename)
