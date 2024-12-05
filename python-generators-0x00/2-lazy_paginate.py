import seed

def paginate_users(page_size, offset):
    """Fetches a single page of users with the given page size and offset."""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows

def lazy_pagination(page_size):
    """Generator that lazily fetches paginated data."""
    offset = 0
    while True:
        # Fetch the next page
        page = paginate_users(page_size, offset)
        if not page:  # Stop if no more rows are returned
            break
        yield page  # Yield the current page
        offset += page_size  # Increment the offset for the next page
