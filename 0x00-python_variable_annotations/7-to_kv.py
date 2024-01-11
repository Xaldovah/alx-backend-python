#!/usr/bin/env python3
"""This mod func takes a str and an int or float as args and return a tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int or float to a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input int or float.

        Returns:
            Tuple[str, float]: A tuple contain the str k and the square of v.
    """
    return (k, v ** 2)
