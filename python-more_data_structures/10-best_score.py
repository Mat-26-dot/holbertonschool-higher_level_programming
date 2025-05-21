#!/usr/bin/python3
def best_score(a_dictionary):


    if not a_dictionary: 
        return None
    first_key = next(iter(a_dictionary))
    max_key = first_key
    max_value = a_dictionary[first_key]
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key

        
