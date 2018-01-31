"""
File for a few configurable values, since it's a python file scripting is a thing.
"""
from os.path import exists, dirname, join, split as psplit
from os import mkdir

PARENT_DIR = join(psplit(dirname(__file__))[0])
FOLDERS = [join(PARENT_DIR, s) for s in ["binaries", "saves", "runfiles", "conf", "tmp"]]

def setup():
    """
    When 'installing' this is ran.

    Creates all the folders required later on.
    """
    for folder in FOLDERS:
        # Make all folders that don't exist and are required
        if not exists(folder):
            mkdir(folder)

    return "Setup done"
