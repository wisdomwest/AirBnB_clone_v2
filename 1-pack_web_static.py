#!/usr/bin/python3
#using fabric to generate a tgz file

import os.path
from datetime import datetime
from fabric.api import local


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
