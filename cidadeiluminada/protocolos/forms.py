# coding: UTF-8
from __future__ import absolute_import

from flask import current_app
from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms.validators import Required
from wtforms_sqlalchemy.orm import model_form

from cidadeiluminada.protocolos.models import Protocolo

_protocolos_fields_args = {
    'cod_protocolo': {
        'validators': [Required()],
    },
    'cep': {
        'validators': [Required()],
    }
}

_ProtocoloForm = model_form(Protocolo, field_args=_protocolos_fields_args,
                            base_class=Form, exclude=['timestamp'])


class ProtocoloForm(_ProtocoloForm):
    arquivo_protocolo = FileField(validators=[Required()])

    def validate_arquivo_protocolo(self, field):
        filename = field.data.filename
        return '.' in filename and filename.rsplit('.', 1)[1] in \
            current_app.config['ALLOWED_EXTENSIONS']
