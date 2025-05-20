#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new_dict = {}   # created new value to store empty list
    for key in a_dictionary:    # iterate through original
        value = a_dictionary[key]   # multiply each value by
        new_dict[key] = value 
    return new_dict
