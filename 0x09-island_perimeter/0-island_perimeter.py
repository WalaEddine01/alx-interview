#!/usr/bin/python3
"""
This module for island problem
"""


def island_perimeter(grid):
    """
    island perimeter method
    """
    v = len(grid)
    h = len(grid[0])
    s = 0
    for i in range(v):
        for j in range(h):
            if grid[i][j] == 1:
                s += 4

                if i > 0 and grid[i - 1][j] == 1:
                    s -= 2

                if j > 0 and grid[i][j - 1] == 1:
                    s -= 2

    return s
