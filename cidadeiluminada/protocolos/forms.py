# coding: UTF-8
from __future__ import absolute_import

from flask import current_app
from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms.validators import Required, Email
from wtforms_sqlalchemy.orm import model_form

from cidadeiluminada.protocolos.models import Protocolo

_protocolos_fields_args = {
    'cod_protocolo': {
        'validators': [Required()],
        'label': u'Código Protocolo',
    },
    'cep': {
        'validators': [Required()],
        'label': u'CEP',
    },
    'email': {
        'validators': [Email()],
        'label': u'E-mail',
    },
    'estado': {
        'label': u'UF',
    },
    'cidade': {
        'label': u'Cidade',
    },
    'bairro': {
        'label': u'Bairro',
    },
    'logradouro': {
        'label': u'Logradouro',
    },
    'numero': {
        'label': u'Número',
    },
    'nome': {
        'label': u'Nome',
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
