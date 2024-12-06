import time
import sqlite3 
import functools


query_cache = {}

def with_db_connection(func):
    """
    A decorator to automatically handle opening and closing a database connection.
    Passes the connection object as the first argument to the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
    return wrapper

def cache_query(func):
    """
    A decorator to cache the results of database queries.
    Caches results based on the SQL query string to avoid redundant calls.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Extract query string from arguments"""
        query = kwargs.get('query') if 'query' in kwargs else args[1] if len(args) > 1 else None
        if query in query_cache:
            print(f"Cache hit for query: {query}")
            return query_cache[query]
        print(f"Cache miss for query: {query}")
        """Execute the query and cache the result"""
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
