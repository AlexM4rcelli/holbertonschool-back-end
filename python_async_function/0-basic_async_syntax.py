#!/usr/bin/env python3
"""
    Module to afunction
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
