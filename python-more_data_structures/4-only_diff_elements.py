#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    result = set()
    for elements in set_1:
        if elements not in set_2:
            result.add(elements)

    for elements in set_2:
        if elements not in set_1:
            result.add(elements)
    return result
