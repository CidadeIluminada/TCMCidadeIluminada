# coding: UTF-8
from __future__ import absolute_import

from flask.ext.wtf import Form
from wtforms.fields import FileField
from wtforms_sqlalchemy.orm import model_form

from cidadeiluminada.protocolos.models import Protocolo


_ProtocoloForm = model_form(Protocolo, base_class=Form)


class ProtocoloForm(_ProtocoloForm):
    arquivo_protocolo = FileField()
