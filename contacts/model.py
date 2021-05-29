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

        headers = ('_id', 'brand_name', 'email', 'status')
        for colIndex, header in enumerate(headers):
            tableModel.setHeaderData(colIndex, Qt.Horizontal, header)

        return tableModel
