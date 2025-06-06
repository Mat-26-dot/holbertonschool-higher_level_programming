#!/usr/bin/python3
"""adds all arguments to a Python list,
and then save them to a file"""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""Correctly import the functions from your modules"""
filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except Exception:
    item = []

item.extend(sys.argv[1:])

save_to_json_file(items, filename)
