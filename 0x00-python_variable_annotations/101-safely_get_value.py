#!/usr/bin/env python3
"""This mod fun return either value assoc with key or default val of type T"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[
            T, None] = None) -> Union[Any, T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping): The input dictionary.
        key (Any): The key to look up in the dictionary.
        default (Union[T, None], optional):
            The default val to return if key is not present. Defaults to None.
        Returns:
            Union[Any, T]:
                The value assoc with key if present, otherwise the default val
    """
    if key in dct:
        return dct[key]
    else:
        return default
