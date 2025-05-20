#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    
    result = set()  # Create an empty set to hold the result
    
    for elements in set_1:  # Loop through elements in set_1
        if elements not in set_2:   # If elem not in set_2, add to result
            result.add(elements)

    for elements in set_2:  # Loop through elements in set_2
        if elements not in set_1:   # If elem not in set_1, add to result
            result.add(elements)
    return result   # Return the result set
