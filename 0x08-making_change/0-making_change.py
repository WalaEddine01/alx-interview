#!/usr/bin/python3
"""
This module contains method that solves
Making change problem
"""


def makeChange(coins, total):
    """
    Making change problem method
    """
    change = total
    c = []
    i = 0
    j = 1
    coins.sort()
    if len(coins) == 0:
        return -1
    if change <= 0:
        return 0
    while j <= len(coins):
        i = 0
        change = total
        index = len(coins) - j
        while index >= 0:
            if change == 0:
                break
            if coins[0] > change and j == 1:
                return -1
            elif coins[0] > change:
                c.append(-1)
                break
            if coins[index] <= change:
                change = change - coins[index]
                i = i + 1
            else:
                index = index - 1
        c.append(i)
        j = j + 1
    c.sort()
    return c[0]
