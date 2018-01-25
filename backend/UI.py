"""
UI is a parent class to UIs that cli uses.
"""
from abc import abstractmethod

class UI():
    """
    Parent for cli and possible later graphical UI.
    """
    def __init__(self, *args):
        self.running = False
        self.args = args

    @abstractmethod
    def tick(self):
        """
        Called repeatedly until self.running is False
        """
        pass


class Cli(UI):
    """
    Implementation of the UI interface defined above.
    """
    def __init__(self, *args):
        super().__init__(self)
        self.output = ""
        self.action_tree =

    def tick(self):
        print(self.output)

        # Formated user input
        fui = self.format(input(">"))

        self.find_action(fui)

    def find_action(self, fui):
        """
        test
        """
        pass

    def format(self, out):
        """
        Used to format users' inputs in such a form where it can be parsed.
        """
        return out
