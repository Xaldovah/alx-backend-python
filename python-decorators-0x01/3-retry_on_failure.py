import time
import sqlite3
import functools

def with_db_connection(func):
    """
    A decorator to automatically handle opening and closing a database connection.
    Passes the connection object as the first argument to the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open database connection
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection to the decorated function
            return func(conn, *args, **kwargs)
        finally:
            # Ensure the connection is closed
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=2):
    """
    A decorator to retry a function if it raises an exception.
    Retries up to `retries` times with a delay of `delay` seconds between attempts.
    """
    def decorator(func):
        @functools.wrapper(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            """Raise the last exception after exhausting retries"""
            raise last_exception
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

# Attempt to fetch users with automatic retry on failure
try:
    users = fetch_users_with_retry()
    print(users)
except Exception as e:
    print(f"Failed to fetch users after retries: {e}")
