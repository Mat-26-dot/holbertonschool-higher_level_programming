#!/usr/bin/python3
"""This module provides utilities for
reading and writing JSON files."""


import json


def load_from_json_file(filename):
    """Loads and parses JSON data from a file."""

    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []