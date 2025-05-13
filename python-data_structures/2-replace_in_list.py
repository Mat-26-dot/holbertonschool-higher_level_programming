#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx < 0:    # Check idx if is negative
        return my_list

    if idx >= len(my_list):    # Check if idx is out of range
        return my_list

    my_list[idx] = element

    return my_list
