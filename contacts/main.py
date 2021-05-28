"""
main.py

    Provides the contacts application.

"""
import sys

from PyQt5.QtWidgets import QApplication

from .views import Window


def main():
    '''Contacts main function.'''

    # Create the application:
    app = QApplication(sys.argv)

    # Create the main window:
    window = Window()
    window.show()

    # Run the event loop:
    sys.exit(app.exec())
