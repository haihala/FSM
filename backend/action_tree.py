"""
This module generates an action tree used by Cli.
An action tree is an object comparable to a graph, where using a pathway runs a function.
"""

from .version_manager import VersionManager
from .run_manager import RunManager
from .config import FOLDERS

class ActionTree():
    """
    This is the actual Action tree object that cli navigates.
    """

    class Action():
        """
        Node, that cannot be entered.
        """
        def __init__(self, action=None, name=""):
            self.action = action
            self.name = name

    def __init__(self):
        binary_folder, save_folder, runfile_folder, conf_folder = FOLDERS
        self.version_manager = VersionManager(binary_folder)
        self.run_manager = RunManager(binary_folder, save_folder, runfile_folder, conf_folder)

        self.modes = {
            "Main": {
                "install": ([], ["version"], self.version_manager.install),
                "start": (["runfile"], [], self.run_manager.start),
                "create": (["name", "save"], ["conf", "launch_options", "binary"], self.run_manager.create)
            },
            "Play": {}  # In play mode, everything is passed to the server process.
        }
        self.mode = "Main"

