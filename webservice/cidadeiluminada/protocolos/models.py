# coding: UTF-8
from __future__ import absolute_import

from datetime import datetime

from sqlalchemy import Column
from sqlalchemy.types import Integer, String, DateTime

from cidadeiluminada.base import db


class Protocolo(db.Model):

    id = Column(Integer, primary_key=True)
    cod_protocolo = Column(String(255))

    timestamp = Column(DateTime, default=datetime.now)

    filename = Column(String(255))
