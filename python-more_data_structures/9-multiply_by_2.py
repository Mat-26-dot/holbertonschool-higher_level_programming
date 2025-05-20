#!/usr/bin/python3
def multiply_by_2(a_dictionary):

    new_dict = {}
    for key in a_dictionary: # iterate through original dict
        value = a_dictionary[key]  # multiply each value by 2 and add to the new dictionary
        new_value = value *2
        new_dict[key] = new_value 
    return new_dict