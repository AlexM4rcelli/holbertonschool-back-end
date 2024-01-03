#!/usr/bin/env python3
"""
    def sum_mixed_list(mxd_list: list[int | float]) -> float:
"""
from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing elements of type int or float.
    
    Returns:
    int: The sum of the input list.
    """
    return sum(mxd_list)
