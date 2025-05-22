#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats, casting them to integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(100)
    198
    >>> add_integer(2.5, 3.7)
    5
    >>> add_integer("hi", 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
