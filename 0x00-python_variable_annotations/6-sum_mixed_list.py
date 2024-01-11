#!/usr/bin/env python3
"""This module func takes list of ints and floats as arg and return a float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): The input list of integers and floats.

        Returns:
            float: The sum of the input list.
    """
    return sum(mxd_lst)
