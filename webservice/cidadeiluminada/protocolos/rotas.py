# coding: UTF-8
from __future__ import absolute_import
import os

from flask import Blueprint, jsonify, request, current_app, redirect, url_for,\
    send_from_directory
from werkzeug import secure_filename

from cidadeiluminada.protocolos.models import Protocolo

bp = Blueprint('protocolos', __name__)


def init_app(app, url_prefix='/protocolos'):
    app.register_blueprint(bp, url_prefix=url_prefix)


def _allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in \
        current_app.config['ALLOWED_EXTENSIONS']


@bp.route('/')
def index():
    return 'Hello protocolos'


@bp.route('/protocolos.json')
def lista():
    protocolos = Protocolo.query.all()
    return jsonify(payload=protocolos)


@bp.route('/novo/', methods=['GET', 'POST'])
def novo():
    if request.method == 'POST':
        file_ = request.files['file']
        if file_ and _allowed_file(file_.filename):
            filename = secure_filename(file_.filename)
            file_.save(os.path.join(current_app.config['UPLOAD_FOLDER'],
                                    filename))
            return redirect(url_for('.uploaded_file', filename=filename))
    return '''
    <!doctype html>
    <title>Novo protocolo</title>
    <h1>Novo protocolo</h1>
    <form action="" method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
    </form>
    '''


@bp.route('/files/<filename>/')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
