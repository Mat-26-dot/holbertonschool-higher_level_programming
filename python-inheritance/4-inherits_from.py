#!/usr/bin/python3
"""object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited
    from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
