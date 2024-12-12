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

    
    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context, close the connection, and handle exceptions if needed.
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()

        return exc_type is None


if __name__ == "__main__":
    db_name = "example.db"
    with DatabaseConnection(db_name) as cursor:
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        """)
        cursor.execute("INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie')")

    with DatabaseConnection(db_name) as cursor:
        cursor.execute("SELECT * FROM users")
        results = cursor.fetchall()
        for row in results:
            print(row)
