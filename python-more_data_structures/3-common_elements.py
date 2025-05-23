#!/usr/bin/python3
def common_elements(set_1, set_2):

    common = set() # An empty set called common is created to store elements
    for element in set_1: # The function loops through each element in set_1
        if (element in set_2): # For each element it checks if that element also exist in set_2
            common.add(element) # If the element is found in both sets, it is added to the common set
    return common # After checking all elements, the function returns the set containing all common elements.
