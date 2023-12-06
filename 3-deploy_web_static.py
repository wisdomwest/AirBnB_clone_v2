#!/usr/bin/python3
# using fabric to generate a tgz file

import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.237.79.93", "34.207.63.6"]


def do_pack():
    """generate .tgz archive"""
    date = datetime.utcnow()
    date_format = date.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date_format)
    try:
        if not os.path.isdir("versions"):
            os.makedirs("versions")
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None


def do_deploy(archive_path):
    """deploy to servers"""
    if not os.path.isfile(archive_path):
        return False
    path = archive_path.split("/")[-1]
    name = path.split(".")[0]
    try:
        put(archive_path, "/tmp/{}".format(path))
        run("mkdir -p /data/web_static/releases/{}/".
            format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(path, name))
        run("rm /tmp/{}".format(path))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(name))
        return True
    except Exception as e:
        return False


def deploy():
    """combine all this together"""
    path = do_pack()
    if path is None:
        return False
    x = do_deploy(path)
    return x
