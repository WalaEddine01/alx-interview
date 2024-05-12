#!/usr/bin/python3
"""
This Module contains the validUTF8 method
"""


def validUTF8(data):
    """
    validUTF8 Method
    """
    j = 0
    for i in data:
        if j == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                j = 1
            elif i >> 4 == 0b1110:
                j = 2
            elif i >> 3 == 0b11110:
                j = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            j -= 1
    return j == 0
