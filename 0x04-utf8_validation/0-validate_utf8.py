#!/usr/bin/python3
"""a function that determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return true if data contains valid utf-8 characters or false otherwise
       It assume each element in data is 1 byte and only handle the 8 least
       significant bits of each element in data
    """

    remaining_bytes = 0

    for char in data:
        if remaining_bytes > 0 and (char >> 6) == 10:
            remaining_bytes -= 1
        elif (char >> 7) == 0:
            if remaining_bytes > 0:
                return False
            remaining_bytes = max(0, remaining_bytes - 1)
        else:
            return False
    return remaining_bytes == 0
