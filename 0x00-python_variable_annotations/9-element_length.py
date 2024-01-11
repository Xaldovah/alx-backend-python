#!/usr/bin/env python3
"""This module func to Calc the length of each elem in the input iterable"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input iterable.

    Args:
        lst (Iterable[Sequence]): The input iterable containing sequences.

        Returns:
            List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
            an element from the input iterable and its corresponding length.
    """
    return [(i, len(i)) for i in lst]

