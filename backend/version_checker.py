"""
Module for checking the newest version and if a certain version exists.
"""

from os.path import join, split as psplit
from glob import glob
from requests import get

from .config import FOLDERS

def newest(experimental=False):
    """
    returns version number of the newest version of the server.
    """
    if experimental:
        url = "https://www.factorio.com/download-headless/experimental"
    else:
        url = "https://www.factorio.com/download-headless"

    resp = get(url)
    SS = "/get-download/"  # Search String
    text = resp.text[resp.text.find(SS)+len(SS):]  # Find start point
    return text[:text.find("/")]  # Find end point

def newest_installed_binary():
    """
    Returns the version number of the newest installed server.
    """
    glob_result = glob(join(FOLDERS[0], "*"))
    if glob_result:
        # Find newest
        glob_result = [psplit(i)[1] for i in glob_result]
        glob_result = [[int(j) for j in i.split(".")] for i in glob_result]
        sorted(glob_result)
        return ".".join(str(i) for i in glob_result[0])
    return None
