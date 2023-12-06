#!/usr/bin/python3
#using fabric to generate a tgz file
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
    """generate .tgz archive"""
    date = datetime.utcnow()
    file = "web_static_{}{}{}{}{}{}.tgz".format(date.year,
                                                date.month,
                                                date.day,
                                                date.hour,
                                                date.minute,
                                                date.second)
    
    if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file
