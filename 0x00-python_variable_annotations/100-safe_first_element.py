#!/usr/bin/env python3
"""This mod func return either first elem of seq or None if seq is empty"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element of a sequence.

    Args:
        lst (Sequence[Any]): The input sequence.

    Returns:
        Union[Any, None]: The first elem of the seq, or None if seq is empty
    """
    if lst:
        return lst[0]
    else:
        return None
