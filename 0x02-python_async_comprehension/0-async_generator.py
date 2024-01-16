#!/usr/bin/env python3
"""
This mod func loops 10 times each time asynchronously waits 1 second
"""

import asyncio
import random


async def async_generator() -> float:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.

    Returns:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)