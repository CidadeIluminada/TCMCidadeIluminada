# coding: UTF-8
from __future__ import absolute_import

from fabtools import require, files
from fabtools.python import virtualenv

from fabric.api import env, sudo

env.host_string = 'root@45.55.252.189'

CIDADEILUMINADA_WORK_PATH = '~/cidadeiluminada/TCMCidadeIluminada'


def deploy():
    require.git.working_copy('git@github.com:HardDiskD/TCMCidadeIluminada.git',
                             path=CIDADEILUMINADA_WORK_PATH, update=True)
