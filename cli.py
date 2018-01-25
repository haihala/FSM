"""
The cli module uses the backend UI class to run the user interface.
"""

# Python imports
from sys import argv

# Backend import
from backend.UI import Cli


def main():
    """
    Main function of the cli. Handles user input and text output.
    """
    sarg = argv[1:]
    uic = Cli(sargs)  # User Interface Child, meaning something inheriting from UI()

    while uic.running:
        uic.tick()

if __name__ == '__main__':
    main()
