#!/usr/bin/env python3
"""
    Module to afunction
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    We use asyncio.run() to execute the coroutine coro and return the result.

    That function runs the passed coroutine, taking care of managing the
    asyncio event loop, finalizing asynchronous generators, and closing
    the executor.

    That function cannot be called when another asyncio event loop is running
    in the same thread.
    """

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n
