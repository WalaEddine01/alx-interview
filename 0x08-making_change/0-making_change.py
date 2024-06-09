#!/usr/bin/python3
"""
This module contains method that solves
Making change problem
"""


def makeChange(coins, total):
    """
    Making change problem method
    """
    i = 0
    coins.sort()
    if total <= 0:
        return 0
    index = len(coins) - 1
    while index >= 0:
        if coins[0] > total:
            return -1
        if coins[index] < total:
            total = total - coins[index]
            i = i + 1
        else:
            index = index - 1

    return i
