# coding: UTF-8
from __future__ import absolute_import

from flask.ext.login import UserMixin
from sqlalchemy import Integer, String

from cidadeiluminada.base import db, JSONSerializationMixin


class User(db.Model, UserMixin, JSONSerializationMixin):
    id = db.Column(Integer, primary_key=True)
    username = db.Column(String(255), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)

    pass
