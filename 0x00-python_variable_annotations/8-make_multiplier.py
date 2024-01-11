#!/usr/bin/env python3
"""This mod function takes a float as an arg and returns a func"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create and return a func that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used in the returned function

        Returns:
        Callable[[float], float]: A func that takes a float and returns the product.
    """
    def multiplier_function(x: float) -> float:
        """takes a float arg and returns the product of that float and the given multiplier"""
        return x * multiplier

    return multiplier_function
