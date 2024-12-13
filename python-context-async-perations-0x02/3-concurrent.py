#!/usr/bin/env python3
"""
Concurrent asynchronous database queries using aiosqlite and asyncio.gather.
"""

import aiosqlite
import asyncio


async def async_fetch_users(db_path: str):
    """
    Fetch all users from the database.
    """
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute("SELECT * FROM users")
        rows = await cursor.fetchall()
        await cursor.close()
    return rows


async def async_fetch_older_users(db_path: str):
    """
    Fetch users older than 40 from the database.
    """
    async with aiosqlite.connect(db_path) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        rows = await cursor.fetchall()
        await cursor.close()
    return rows


async def fetch_concurrently():
    """
    Run both queries concurrently and print results.
    """
    db_path = "users.db"
    results = await asyncio.gather(
        async_fetch_users(db_path),
        async_fetch_older_users(db_path)
    )

    print("All Users:")
    for row in results[0]:
        print(row)

    print("\nUsers Older than 40:")
    for row in results[1]:
        print(row)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
