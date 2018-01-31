"""
This module generates an action tree used by Cli.
An action tree is an object comparable to a graph, where using a pathway runs a function.
"""

from .version_manager import VersionManager
from .run_manager import RunManager
from .config import FOLDERS, setup

class ActionTree():
    """
    This is the actual Action tree object that cli navigates.
    """

    def __init__(self):
        binary_folder, save_folder, runfile_folder, conf_folder, temp_folder = FOLDERS
        self.version_manager = VersionManager(binary_folder, temp_folder)
        self.run_manager = RunManager(binary_folder, save_folder, runfile_folder, conf_folder)

        self.modes = {
            "Main": {
                "install": (self.version_manager.install, [], ["version"]),
                "start": (self.run_manager.start, ["runfile"], []),
                "create": (self.run_manager.create, ["name", "save"], ["conf", "launch_options", "binary"]),
                "setup": (setup, [], [])
            },
            "Play": {}  # In play mode, everything is passed to the server process.
        }
        self.mode = "Main"

    def call(self, fui):
        """
        Picks and chooses which function to call given Formated User Input.
        """
        if fui[0] in self.modes[self.mode]:
            return self.modes[self.mode][fui[0]][0](*fui[1:])
        return "Not a command. Try 'help'"
