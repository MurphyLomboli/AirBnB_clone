#!/usr/bin/python3
"""
Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy:
Prototype: def do_deploy(archive_path):
Returns False if the file at the path archive_path doesn’t exist
You must use this script to deploy it on your servers:
xx-web-01 and xx-web-02
"""

import os
from fabric.api import *

api.env.hosts = ['163945-web-01', '163945-web-02']
env.user = "ubuntu"
env.hosts = ['107.23.119.223', '54.84.33.47']


def do_deploy(archive_path):
    """
    Deploys an archive file to the server

    Args:
        archive_path: path to the archive file to be deployed
        to the server
    Returns:
        True: if successful
        False: if otherwise
    """

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        split_slash = archive_path.split("/")[-1]
        remove_tgz = split_slash.split(".")[0]
        directory = '/data/web_static/releases/'
        run('mkdir -p {}{}'.format(directory, remove_tgz))
        run('tar -xzf /tmp/{0}.tgz -C {1}{0}'.format(remove_tgz, directory))
        run('rm /tmp/{}.tgz'.format(remove_tgz))
        run('mv {0}{1}/web_static/* {0}{1}'.format(directory, remove_tgz))
        run('rm -rf {}{}/web_static'.format(directory, remove_tgz))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}\
                /data/web_static/current'.format(directory, remove_tgz))
        return True
    except Exception as e:
        return False
