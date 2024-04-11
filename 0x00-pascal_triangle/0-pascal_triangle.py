#!/usr/bin/python3
def pascal_triangle(n):
    _list1 = []
    if n <= 0:
        return _list1
    for i in range(n):
        _list1.append([1])
        for j in range(n):
            if i == j + 1 and i != 0:
                _list1[i].append(1)
                break
            elif i == 0:
                break
            else:
                _list1[i].append(_list1[i - 1][j - 1] + _list1[i - 1][j])
    return _list1
