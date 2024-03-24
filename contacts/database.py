"""
database.py

    Provides our database connection.
"""
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def _createContactsTable():
    '''Create the contacts table in the database.'''
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                name VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL
            )
        """
    )


def createConnection(dbName):
    '''Creates and opens a database connection.'''
    conn = QSqlDatabase.addDatabase("QSQLITE")
    conn.setDatabaseName(dbName)

    if not conn.open():
        QMessageBox.warning(
            None,
            'Contacts',
            f"Database Error: {conn.lastError().text()}",
        )
        return False

    _createContactsTable()
    return True