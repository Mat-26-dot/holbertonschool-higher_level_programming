#!/usr/bin/python3
"""This module appends a string at the end of a text file (UTF8) 
and returns the number of characters added"""


def append_write(filename="", text=""):
    """Open the file in append mode with UTF-8 encoding"""
    with open(filename, 'a', encoding='utf-8') as f:
       chars_added = f.write(text)
       return chars_added
        