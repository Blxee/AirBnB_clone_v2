#!/usr/bin/python3
""" 1. Compress before sending """
from fabric.api import *
from datetime import datetime


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions/")
    path = f"versions/web_static_{date}.tgz"
    archive = local(f"tar -cvzf {path} web_static/")
    if archive.succeeded:
        return path
