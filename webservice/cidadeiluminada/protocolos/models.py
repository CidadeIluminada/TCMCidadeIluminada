# coding: UTF-8
from __future__ import absolute_import

from datetime import datetime

from sqlalchemy import Model, Column
from sqlalchemy.types import Integer, String, Datetime


class Protocolo(Model):

    id = Column(Integer, primary_key=True)
    cod_protocolo = Column(String(255))

    timestamp = Column(Datetime, default=datetime.now)
