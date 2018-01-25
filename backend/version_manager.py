"""
Module for the management of different server and maybe some day mod versions.
"""
class VersionManager():
    """
    Class that does everything this module sets out to do.

    Basically, this class handles the file I/O required.
    Download manager will probably be a thing later, this will probably
    have a download manager member.
    """
    def __init__(self):
        pass

    def install(self, version=None):
        """
        If not installed, will install the specified version of the factorio server.

        Version must exist, if version is None, the newest will be installed.
        """
        pass
