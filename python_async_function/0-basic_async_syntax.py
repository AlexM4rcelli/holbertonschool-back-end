#!/usr/bin/env python3
"""
    Module to afunction
"""


import random, asyncio

async def wait_random(max_delay: int | float = 10) -> float:
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time