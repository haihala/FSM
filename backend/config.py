"""
File for a few configurable values, since it's a python file scripting is a thing.
"""
from os.path import dirname, join, split as psplit

PARENT_DIR = join(psplit(dirname(__file__))[0])
FOLDERS = [join(PARENT_DIR, s) for s in ["binaries", "saves", "runfiles", "conf"]]
