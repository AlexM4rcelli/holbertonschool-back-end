#!/usr/bin/env python3
"""
    Module to variable annotations
"""


from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns:
    Callable[[float], float]: A function that takes a float and returns
    its product with the multiplier.
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    
    return multiplier_function