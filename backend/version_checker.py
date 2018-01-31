"""
Module for checking the newest version and if a certain version exists.
"""

from requests import get

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
