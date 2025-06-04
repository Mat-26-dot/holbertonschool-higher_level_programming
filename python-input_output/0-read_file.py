#!/usr/bin/python3
"""
This module contains a function that reads a UTF-8 text file
and prints its contents to standard output.
"""


def read_file(filename=""):
    """function reads a text file (UTF8) and prints to stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
