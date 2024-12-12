import sqlite3


class DatabaseConnection:
    def __init__(self, db_name):
        """
        Initialize the DatabaseConnection context manager.
        :param db_name: The name of the database file to connect to.
        """
        self.db_name = db_name
        self.connection = None
        self.cursor = None


    def __enter__(self):
        """
        Enter the runtime context, establish a connection and return the cursor.
        """
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    
    def __exit__(self):
        """
        Exit the runtime context, close the connection, and handle exceptions if needed.
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()

        return exc_type is None
