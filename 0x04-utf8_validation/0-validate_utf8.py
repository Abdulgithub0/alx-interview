#!/usr/bin/python3
"""a function that determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return true if data contains
       valid utf-8 characters or false otherwise
       It assume each character in data parameter is 1 byte(like ASCII)
    """
    for char in data:
        if char >> 7 == 0:
            continue
        else:
            return False
    return True
