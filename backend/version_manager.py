"""
Module for the management of different server and maybe some day mod versions.
"""
from os.path import exists, join
from os import mkdir
from shutil import rmtree, move
import tarfile

from requests import get

from version_checker import newest

class VersionManager():
    """
    Class that does everything this module sets out to do.

    Basically, this class handles the file I/O required.
    Download manager will probably be a thing later, this will probably
    have a download manager member.
    """

    def __init__(self, binary_folder, temp_folder):
        self.binary_folder = binary_folder
        self.temp_folder = temp_folder

    def install(self, version=None):
        """
        If not installed, will install the specified version of the factorio server.

        Version must exist, if version is None, the newest will be installed.
        """
        if version is None:
            version = newest()

        # Check if installed already
        if exists(join(self.binary_folder, version)):
            return "Version {} already installed".format(version)

        self.download(version)
        self.unpack(version)
        move(join(self.temp_folder, version), join(self.binary_folder, version))

    def download(self, version):
        """
        Downloads the given version of factorio binary and treats.
        """
        # Clear tmp
        rmtree(self.temp_folder, ignore_errors=True)
        mkdir(self.temp_folder)

        # Download new
        response = get("https://www.factorio.com/get-download/{}/headless/linux64".format(version), stream=True)
        handle = open(join(self.temp_folder, "linux64.tar.xf"), "wb")
        for chunk in response.iter_content(chunk_size=512):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)

    def unpack(self, version):
        """
        Extracts given tarball to the binary folder
        """
        tarball = tarfile.open(join(self.temp_folder, "linux64.tar.xf"))
        tarball.extractall(path=join(self.temp_folder, version))

        tarball.close()

def newest_installed_binary():
    """
    Returns newest installed binary
    """
    pass
