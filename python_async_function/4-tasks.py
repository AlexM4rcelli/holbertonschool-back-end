#!/usr/bin/env python3
"""
    Module to afunction
"""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    First we create the awaitables objects or tasks, each task
    corresponds to the execution of the wait_random function.

    Then we use asyncio.as_completed to wait until each task
    is completed.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    return [await task for task in asyncio.as_completed(tasks)]
