# coding: UTF-8
from __future__ import absolute_import

from datetime import datetime

from flask.json import JSONEncoder
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class JSONSerializationMixin(object):
    """docstring for JSONSerializationMixin"""
    def serialize(self):
        return {k: v for k, v in self.__dict__.items()
                if k is not '_sa_instance_state'}


class AppJSONEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, JSONSerializationMixin):
            return o.serialize()
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S')
        return super(AppJSONEncoder, self).default(o)


def init_app(app):
    db.init_app(app)
