#!/usr/bin/python3
"""Module for add_integer method"""

def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int or float.
        b: second int or float, default value is 98.

    Raises:
        TypeError: if a, b are neither int nor float.

    Returns:
        sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
