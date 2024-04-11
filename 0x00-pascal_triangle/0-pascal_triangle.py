#!/usr/bin/python3
"""

"""
def pascal_triangle(n):
    """
    """
    _list1 = []
    if n <= 0:
        return _list1
    for i in range(n):
        _list1.append([1])
        j = 0
        for j in range(i):
            if i == j + 1 and i != 0:
                _list1[i].append(1)
            elif i == j:
                 _list1[i].append(1)
            else:
                print(i, j)
                _list1[i].append(_list1[i - 1][j - 1] + _list1[i - 1][j])
                for row in _list1:
                    print("[{}]".format(",".join([str(x) for x in row])))

    return _list1
