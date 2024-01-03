#!/usr/bin/env python3
"""
without from typing import List
    def sum_list(input_list: list[float]) -> float:
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.
    float: The sum of the input list.
    """
    return sum(input_list)
