import mysql.connector


def stream_users():
    """Generator function to fetch rows one by one from the user_data table."""
    try:
        connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="@Denny23617",
                database="ALX_prodev"
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data")
        
        for row in cursor:
            yield row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
