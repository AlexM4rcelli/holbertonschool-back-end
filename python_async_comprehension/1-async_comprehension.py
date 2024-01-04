#!/usr/bin/env python3
"""
    Module to afunction
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collect 10 random numbers using an async comprehensing over 
    async_generator, then return the 10 random numbers.
    """
    result = []
    async for coroutine in async_generator():
        result.append(coroutine)
    return result
