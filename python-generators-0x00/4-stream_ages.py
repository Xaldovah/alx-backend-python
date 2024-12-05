import seed

def stream_user_ages():
    """Generator function to yield user ages one by one."""
    try:
        # Connect to the database
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)

        # Query user ages
        cursor.execute("SELECT age FROM user_data")
        for row in cursor:
            yield row['age']  # Yield each age one by one
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()

def calculate_average_age():
    """Calculates the average age of users using the generator."""
    total_age = 0
    count = 0

    # Iterate through the generator to compute the sum and count
    for age in stream_user_ages():
        total_age += age
        count += 1

    # Calculate and print the average
    if count > 0:
        average_age = total_age / count
        print(f"Average age of users: {average_age:.2f}")
    else:
        print("No users found to calculate average age.")
