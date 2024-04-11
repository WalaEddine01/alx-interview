#!/usr/bin/python3
"""
This module contains the pascal method
"""


def pascal_triangle(n):
    """
    Pascal method
    """
    _list1 = []
    if n <= 0:
        return _list1
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(_list1[i - 1][j - 1] + _list1[i - 1][j])
        if i > 0:
            row.append(1)
        _list1.append(row)

    return _list1
