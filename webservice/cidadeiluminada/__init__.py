# coding: UTF-8
from __future__ import absolute_import

from cidadeiluminada import base, protocolos


def init_app(app):
    base.init_app(app)
    protocolos.init_app(app)
