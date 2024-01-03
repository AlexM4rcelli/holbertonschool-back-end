#!/usr/bin/env python3
"""
    Module to afunction
"""


def floor(num: float) -> int:
    """
    Returns the floor of a float.

    Returns:
    int: The floor of the input float.
    """
    
    return int(num) if num >= 0 else int(num) - 1
