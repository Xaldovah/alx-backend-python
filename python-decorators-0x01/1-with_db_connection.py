import sqlite3 
import functools

def with_db_connection(func): 
    """
    A decorator to automatically handle opening and closing a database connection.
    Passes the connection object as the first argument to the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Open database connection"""
        conn = sqlite3.connect('users.db')
        try:
            """Pass the connection to the decorated function"""
            return func(conn, *args, **kwargs)
        finally:
            """Ensure the connection is closed"""
            conn.close()
    return wrapper

@with_db_connection 
def get_user_by_id(conn, user_id): 
cursor = conn.cursor() 
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)
