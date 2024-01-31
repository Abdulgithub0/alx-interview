#!/usr/bin/python3
"""a function that determines if a given data
    set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """Return true if data contains
       valid utf-8 characters or false otherwise
       It assume each element in data is 1 byte and only handle the 8 least
       significant bits of each element in data
    """

    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            elif byte >> 7 != 0:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
