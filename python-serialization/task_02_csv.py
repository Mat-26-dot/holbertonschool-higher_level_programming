#!/usr/bin/env python3
 
import csv 
import json

def convert_csv_to_json(csv_filename):

    try:
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)
        
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)
    except Exception:
        return True
