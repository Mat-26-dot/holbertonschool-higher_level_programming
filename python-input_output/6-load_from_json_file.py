#!/usr/bin/python3

import json

def load_from_json_file(filename):

    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []



        