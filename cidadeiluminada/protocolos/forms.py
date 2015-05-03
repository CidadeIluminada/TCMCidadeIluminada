# coding: UTF-8
from __future__ import absolute_import
import os

from flask import current_app
from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms.validators import ValidationError, Required, Email, Length, \
    Optional
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
        'validators': [Email(), Optional()],
        'label': u'E-mail',
    },
    'nome': {
        'label': u'Nome',
        'validators': [Optional()]
    },
    'estado': {
        'validators': [Length(min=2, max=2)],
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
}

_ProtocoloForm = model_form(Protocolo, field_args=_protocolos_fields_args,
                            base_class=Form, exclude=['timestamp'])


class ProtocoloForm(_ProtocoloForm):
    arquivo_protocolo = FileField(validators=[Required()])

    def validate_arquivo_protocolo(self, field):
        filename = field.data.filename
        allowed_filename = os.path.splitext(filename) in \
            current_app.config['ALLOWED_EXTENSIONS']
        if not allowed_filename:
            raise ValidationError(u'Arquivo inválido')
