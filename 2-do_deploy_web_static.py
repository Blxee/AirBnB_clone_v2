#!/usr/bin/python3
''' 1. Compress before sending '''
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['100.25.152.12', '54.167.85.211']
env.user = 'ubuntu'


def do_pack():
    ''' packs web_static/ folder preparing for deployment '''
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    local('mkdir -p versions/')
    path = f'versions/web_static_{date}.tgz'
    archive = local(f'tar -cvzf {path} web_static/')
    if archive.succeeded:
        return path


def do_deploy(archive_path):
    ''' deploy the web_static archive to the servers '''
    if not os.path.exists(archive_path):
        return False
    if put(archive_path, '/tmp/').failed:
        return False
    name = archive_path.rsplit('/', 1)[-1]
    with cd('/tmp/'):
        if sudo(f'tar -xzf {name} web_static').failed:
            return False
        if sudo(f'rm {name}').failed:
            return False
    dir = name.removesuffix('.tgz')
    if sudo(f'mv /tmp/{name} /data/web_static/releases/{dir}').failed:
        return False
    if sudo(f'ln -sf /data/web_static/releases/{dir} /data/web_static/current').failed:
        return False
    return True
