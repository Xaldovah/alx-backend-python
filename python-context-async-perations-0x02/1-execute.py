import  sqlite3


class ExecuteQuery:
    def __init__(self, db_name, query, parameters=None):
        """
        Initialize the ExecuteQuery context manager.
        :param db_name: The database file name to connect to.
        :param query: The SQL query to execute.
        :param parameters: Parameters for the SQL query (default is None).Initialize the ExecuteQuery context manager.
        :param db_name: The database file name to connect to.
        :param query: The SQL query to execute.
        :param parameters: Parameters for the SQL query (default is None).
        """
        self.db_name = db_name
        self.query = query
        self.parameters = parameters or []
        self.connection = None
        self.cursor = None
        self.results = None


    def __enter__(self):
        """
        Enter the runtime context, establish the connection, execute the query, and return results.
        """
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(self.query, self.parameters)
            self.results = self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            self.results = []
        return self.results


    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context and close the database connection.
        """
        if self.connection:
            self.connection.commit()
            self.connection.close()
        return False


if __name__ == "__main__":
    db_name = "example.db"

    # Drop the existing table to avoid schema conflicts
    with ExecuteQuery(db_name, "DROP TABLE IF EXISTS users") as _:
        pass

    # Create the users table with the correct schema
    with ExecuteQuery(db_name, """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """) as _:
        pass

    # Insert sample data into the users table
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ["Alice", 30]) as _:
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ["Bob", 22]) as _:
        pass
    with ExecuteQuery(db_name, "INSERT INTO users (name, age) VALUES (?, ?)", ["Charlie", 40]) as _:
        pass

    # Query users older than 25
    query = "SELECT * FROM users WHERE age > ?"
    parameter = [25]
    with ExecuteQuery(db_name, query, parameter) as results:
        print("Users older than 25:")
        for row in results:
            print(row)
