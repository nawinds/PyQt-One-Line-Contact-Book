"""
views.py

    Provides views to manage the contacts table.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

from .model import ContactsModel


class Window(QMainWindow):
    '''Main Window'''
    def __init__(self, parent=None):
        '''Initializer'''
        super().__init__(parent)
        self.setWindowTitle('Contacts Book')
        self.resize(650, 350)
        # TODO: Add icon to window...
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)

        self.contactsModel = ContactsModel()
        self.setupUI()


    def setupUI(self):
        '''Setup the main window's GUI.'''
        # Create the table view widget:
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        # Create Buttons:
        self.addButton = QPushButton('Add...')
        self.addButton.clicked.connect(self.openAddDialog())
        self.deleteButton = QPushButton('Delete')
        self.clearAllButton = QPushButton('Clear All')

        # Lay Out GUI:
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)


        def openAddDialog(self):
            '''Open the Add Contact dialog.'''
            dialog = AddDialog(self)
            if (dialog.exec() == QDialog.Accepted):
                self.contactsModel.addContact(dialog.data)
                self.table.resizeColumnsToContents()


class AddDialog(QDialog):
    '''Add Contact dialog'''
    def __init__(self, parent=None):
        '''Initializer'''
        super().__init__(parent=parent)
        self.setWindowTitle('Add Contact')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()


    def setupUI(self):
        '''Setup the Add Contact dialog's GUI.'''
        # Create line edits for data fields:
        self.nameField = QLineEdit()
        self.nameField.setObjectName('Name')
        self.emailField = QLineEdit()
        self.emailField.setObjectName('Email')
        self.statusField = QLineEdit()
        self.statusField.setObjectName('Status')

        # Lay out the data fields:
        layout = QFormLayout()
        layout.addRow('Name:', self.nameField)
        layout.addRow('Email:', self.emailField)
        layout.addRow('Status:', self.statusField)
        self.layout.addLayout(layout)
        
        # Add standard buttons to the dialog and connect them:
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)


        def accept(self):
            '''Accept the data provided through the dialog.'''
            self.data = []
            for field in (self.nameField, self.emailField, self.statusField):
                if not field.text():
                    QMessageBox.critical(
                        self,
                        'Error!',
                        f"You must provide an entry's {field.objectName()}",
                    )
                    # Reset data:
                    self.data = None
                    return

                self.data.append(field.text())

            if not self.data:
                return

            super().accept()
