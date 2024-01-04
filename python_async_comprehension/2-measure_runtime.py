#!/usr/bin/env python3
"""
    Module to afunction
"""
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time, asyncio

async def measure_runtime() -> float:
    start_time = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time.time()

    return end_time - start_time