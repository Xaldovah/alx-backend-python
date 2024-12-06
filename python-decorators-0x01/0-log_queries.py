import sqlite3
import functools
import logging

#### decorator to lof SQL queries

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def log_queries():
    """
    A decorator to log SQL queries executed by the decorated function.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """Extract the query from the arguments"""
            query = kwargs.get('query') if 'query' in kwargs else args[0] if args else None
            if query:
                logging.info(f"Executing SQL query: {query}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
