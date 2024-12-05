import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator function to fetch rows in batches from the user_data table."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your@password",
            database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")
        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
               break
            yield batch
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()


def batch_processing(batch_size):
    """Processes each batch to filter users over the age of 25."""
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            print(user)
