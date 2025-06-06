#!/usr/bin/python3
"""This module provides utilities for
reading and writing JSON files."""


import json


def load_from_json_file(filename):
    """Loads and parses JSON data from a file."""

    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[JSONDecodeError] {e}")
    except FileNotFoundError as e:
        print(f"[FileNotFoundError] {e}")
    except PermissionError as e:
        print(f"[PermissionError] {e}")
