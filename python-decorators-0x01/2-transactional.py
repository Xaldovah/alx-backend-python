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

def transactional(func):
    """
    A decorator to manage database transactions.
    Commits the transaction if the function completes successfully,
    otherwise rolls back the transaction on error.
    """
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            """Execute the wrapped function"""
            result = func(conn, *args, **kwargs)
            """Commit the transaction on success"""
            conn.commit()
            return result
        except Exception as e:
            """Rollback the transaction on failure"""
            conn.rollback()
            raise e
    return wrapper

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
