#!/usr/bin/env python3
"""
This async func measures the total execution time for wait_n(n, max_delay)
"""

import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay value.
        fn (Callable): The function to measure the runtime.

    Returns:
        float: The average time taken for each execution.
    """
    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(wait_n(n, max_delay))
    total_time = time.time() - start_time
    return total_time / n
