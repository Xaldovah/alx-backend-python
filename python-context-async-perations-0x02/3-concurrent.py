import asyncio
import aiosqlite


async def async_fetch_users(db_name):
    """
    Fetch all users from the database asynchronously.
    :param db_name: Name of the SQLite database.
    :return: List of all users.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
    return users


async def async_fetch_older_users(db_name, age_threshold):
    """
    Fetch users older than a specific age asynchronously.
    :param db_name: Name of the SQLite database.
    :param age_threshold: Age threshold for filtering users.
    :return: List of users older than the specified age.
    """
    async with aiosqlite.connect(db_name) as db:
        async with db.execute("SELECT * FROM users WHERE age > ?", (age_threshold,)) as cursor:
            older_users = await cursor.fetchall()
    return older_users


async def fetch_concurrently(db_name):
    """
    Run both fetch operations concurrently.
    :param db_name: Name of the SQLite database.
    """
    all_users_task = async_fetch_users(db_name)
    older_users_task = async_fetch_older_users(db_name, 40)

    # Run both tasks concurrently
    all_users, older_users = await asyncio.gather(all_users_task, older_users_task)

    # Print results
    print("All Users:")
    for user in all_users:
        print(user)

    print("\nUsers Older than 40:")
    for user in older_users:
        print(user)


if __name__ == "__main__":
    db_name = "example.db"

    async def setup_database():
        """
        Set up the database and insert sample data.
        """
        async with aiosqlite.connect(db_name) as db:
            await db.execute("DROP TABLE IF EXISTS users")
            await db.execute("""
                CREATE TABLE users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
            """)
            await db.executemany(
                "INSERT INTO users (name, age) VALUES (?, ?)",
                [("Alice", 30), ("Bob", 22), ("Charlie", 40), ("Diana", 45)]
            )
            await db.commit()

    # Set up the database and run the concurrent fetch
    asyncio.run(setup_database())
    asyncio.run(fetch_concurrently(db_name))
