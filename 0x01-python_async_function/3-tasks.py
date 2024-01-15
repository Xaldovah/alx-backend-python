#!/usr/bin/env python3
"""
This func takes an int max_delay and returns an asyncio.Task
"""

import asyncio
from typing import Union

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Function that takes an integer max_delay and returns an asyncio.Task.

    Args:
        max_delay (int): The maximum delay value.

        Returns:
            asyncio.Task: The asyncio Task.
    """
    return asyncio.create_task(wait_random(max_delay))
