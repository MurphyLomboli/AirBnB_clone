#!/usr/bin/python3
"""
Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean:
"""
from fabric.api import *
import os

env.hosts = ['54.84.33.47', '107.23.119.223']
env.user = 'ubuntu'


def do_clean(number=0):
    """Delete out-of-date archives

    Args:
        number (int): The number of archives to keep

    If number is 0 or 1, keep only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """

    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    arch = sorted(os.listdir("versions"))
    for i in range(number):
        arch.pop()
    with lcd("versions"):
        for archive in arch:
            local("rm {}".format(archive))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        for i in range(number):
            archives.pop()
        for archive in archives:
            run("rm -rf {}".format(archive))
