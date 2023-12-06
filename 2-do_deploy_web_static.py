#!/usr/bin/python3
# using fabric to generate a tgz file

import os.path
from datetime import datetime
from fabric.api import local

env.hosts = ["54.237.79.93", "34.207.63.6"]


def do_pack():
    """generate .tgz archive"""
    date = datetime.utcnow()
    date_format = date.strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date_format)
    try:
        if not os.path.isdir("versions"):
            os.makedirs("versions")
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception as e:
        return None


def do_deploy(file_path):
    """deploy to servers"""
    if not os.path.isfile(file_path):
        return False
    path = file_path.split("/")[-1]
    name = path.split(".")[0]
    try:
        put(file_path, "/tmp/{}".format(path))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(path, name))
        run("rm /tmp/{}".format(path))
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current"
        ).format(name)
        return True
    except Exception as e:
        return False
