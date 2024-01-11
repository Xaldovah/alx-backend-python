#!/usr/bin/env python3
"""A module to demonstrate type checking using mypy."""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    Zoom in on the elements of a tuple.

    Args:
        lst (Tuple): The input tuple.
        factor (int, optional): The zoom factor. Defaults to 2.

        Returns:
            Tuple: contains the elems of input tuple zoomed in based on factor
    """
    zoomed_in: List = [
            item for item in lst
            for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)


zoom_2x = zoom_array(array)


zoom_3x = zoom_array(array, 3)
