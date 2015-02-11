# coding: UTF-8
from __future__ import absolute_import

from datetime import datetime

from flask.ext.sqlalchemy import Model
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime


class Protocolo(Model):

    id = Column(Integer, primary_key=True)
    cod_protocolo = Column(String(255))

    timestamp = Column(DateTime, default=datetime.now)
