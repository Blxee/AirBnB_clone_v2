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
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        release = "/data/web_static/releases/{}".format(filename.split(".")[0])
        run("mkdir -p {}".format(release))
        run("tar -xzf /tmp/{} -C {}".format(filename, release))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}".format(release, release))
        run("rm -rf {}/web_static".format(release))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release))

        return True
    except:
        return False
