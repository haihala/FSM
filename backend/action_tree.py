"""
This module generates an action tree used by Cli.
An action tree is an object comparable to a graph, where using a pathway runs a function.
"""

from .version_manager import VersionManager
from .run_manager import RunManager

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
        self.version_manager = VersionManager()
        self.run_manager = RunManager()

        self.universal = {
            "go": (["Target mode"], [], self.move_to)
        }
        self.modes = {
            "Main": {
                "install": ([], ["version"], self.version_manager.install),
                "start": (["save"], ["version"], )
            },
            "Play": {
                "stop": (),
                "*": ()
            }
        }
        self.mode = "Main"

    def get_available_actions(self):
        """
        returns a dictionary of strings and functions.
        """
        actions = {}
        actions.update(self.universal)
        actions.update(self.modes[self.mode])
        return actions

    def move_to(self, where):
        """
        Changes to mode without executing transfer function.
        """
