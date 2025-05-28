#!/usr/bin/python3
"""Class that inherits fro mym list"""


class MyList(list):
    """Defines a list"""

    def print_sorted(self):
        print(sorted(self))
