#!/usr/bin/python3


# file to delete outdated archives.
from fabric.api import *
import os


# Define the list of web server hosts
env.hosts = ["54.160.85.72", "35.175.132.106"]


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """

    number = 1 if int(number) == 0 else int(number)
    # Clean remote archives on the web server
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

    # Clean local archives
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
