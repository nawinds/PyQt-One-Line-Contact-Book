"""
main.py

    Provides the contacts application.

"""
import sys

from PyQt5.QtWidgets import QApplication

from .database import createConnection
from .views import Window


def main():
    '''Contacts main function.'''

    # Create the application:
    app = QApplication(sys.argv)
    
    # Connect to the database before creating any window:
    if not createConnection("contracts.sqlite"):
        sys.exit(1)

    # Create the main window:
    window = Window()
    window.show()

    # Run the event loop:
    sys.exit(app.exec())
