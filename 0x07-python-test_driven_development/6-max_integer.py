#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the integer maximum in a list of integers
        the function returns None if an empty list
    """
    if len(list) == 0:
        return None
    result = list[0]
    c = 1
    while c < len(list):
        if list[c] > result:
            result = list[c]
        c += 1
    return result
