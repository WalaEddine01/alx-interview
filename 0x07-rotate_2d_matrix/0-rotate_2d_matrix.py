#!/usr/bin/python3
"""
this module contains the rotate_2d_matrix method
"""


def rotate_2d_matrix(matrix):
    '''
    the rotate_2d_matrix method
    '''
    tempMat = []
    n = len(matrix)
    for i in range(n):
        tempMat.append([0] * n)
    for i in range(n):
        for j in range(n):
            tempMat[j][n - 1 - i] = matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = tempMat[i][j]
