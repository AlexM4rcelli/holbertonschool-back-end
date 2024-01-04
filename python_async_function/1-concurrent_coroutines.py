#!/usr/bin/env python3
"""
    Module to afunction
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    First we create the awaitables objects or tasks, each task
    corresponds to the execution of the wait_random function.

    Then we use asyncio.as_completed to wait until each task
    is completed.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
