"""
model.py

    Provides a model to manage the contacts table.
"""
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel


class ContactsModel:

    def __init__(self):
        self.model = self._createModel()


    @staticmethod
    def _createModel():
        '''Creates and sets up the model.'''
        tableModel = QSqlTableModel()
        tableModel.setTable('contacts')
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = ('_id', 'brand_name', 'email')
        for colIndex, header in enumerate(headers):
            tableModel.setHeaderData(colIndex, Qt.Horizontal, header)
        return tableModel


    def addContact(self, data):
        '''Adds a contact to the database.'''
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for colIndex, field in enumerate(data):
            self.model.setData(self.model.index(rows, colIndex + 1), field)
        self.model.submitAll()
        self.model.select()


    def deleteContact(self, row):
        '''Removes a contact from the databse.'''
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()


    def clearContacts(self):
        '''Removes all contact from the database.'''
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.removeRows(0, self.model.rowCount())
        self.model.submitAll()
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()