#!/usr/bin/env python3
"""
This module async func spawns wait_random n times with the specified max_delay
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns wait_random n times with the specified max_delay

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay value.

        Returns:
            List[float]: List of delays in ascending order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
