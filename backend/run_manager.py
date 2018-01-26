"""
Module for the running different server configurations.
"""

import subprocess
from os.path import join, exists
import json

class RunManager():
    """
    Class that does everything this module sets out to do.

    Has functions to start, stop and interact with running servers.
    """
    def __init__(self, binary_folder, save_folder, runfile_folder, conf_folder):
        self.binary_folder = binary_folder
        self.save_folder = save_folder
        self.runfile_folder = runfile_folder
        self.conf_folder = conf_folder

        self.instance = None

    def newest_binary(self):
        """
        returns the newest binary
        """
        pass

    def create(self, name, save, launch_options="", conf=None, binary=None):
        """
        Generates the runfile, which is a type of file used to determine the settins a server has.
        """
        if binary is None:
            binary = self.newest_binary()


        # Create savefile if one doesn't exist
        if exists(join(self.save_folder, save)):
            subprocess_handle = subprocess.Popen([
                join(self.binary_folder, binary, "bin", "x64", "factorio"),
                "--create",
                join(self.save_folder, save)
            ])
            # Wait for the world to generate
            subprocess_handle.wait()
            # Debug output could be extracted here


        # Create runfile
        with open(join(self.runfile_folder, name), "w") as fhandle:
            fhandle.write(
                json.dumps({
                    "save": save,
                    "launch_options": launch_options,
                    "conf": conf,
                    "binary": binary
                })
            )


    def get_runfile(self, fname):
        """
        'unpacks' a runfile
        """
        obj = {}
        with open(join(self.runfile_folder, fname)) as fhandle:
            obj = json.load(fhandle)

        return obj["save"], obj["launch_options"], obj["conf"], obj["binary"]

    def runfile_exists(self, fname):
        """
        Returns true if runfile called fname exists, otherwise false.
        """
        return exists(join(self.runfile_folder, fname))

    def start(self, runfile):
        """
        Starts the desired server.

        TODO: may require threading to work.
        """

        if not self.runfile_exists(runfile):
            return "Runfile doesn't exist"

        save, launch_options, conf, binary = self.get_runfile(runfile)

        # --start-server saves/gotlap.zip --server-settings ../server-settings.json
        # Name of binary
        args = [join(self.binary_folder, binary, "bin", "x64", "factorio")]
        args += ["--start-server", join(self.save_folder, save)]
        args += ["--server-settings", join(self.conf_folder, conf)]
        args += launch_options.split()

        self.instance = subprocess.Popen(args)

    def stop(self):
        """
        If server is running, kill it.
        """

        if self.instance:
            # May need to be bytes, but should be fine.
            self.instance.communicate(input=r'/quit\n')
            self.instance = None
