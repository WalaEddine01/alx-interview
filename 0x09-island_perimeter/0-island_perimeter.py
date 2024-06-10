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
    for i in range(v):
        for j in range(h):
            if grid[i][j] == 1:
                if i > 0:
                    if grid[i - 1][j] != 1:
                        grid[i - 1][j] = grid[i - 1][j] + 2
                if j > 0:
                    if grid[i][j - 1] != 1:
                        grid[i][j - 1] = grid[i][j - 1] + 2
                if j < len(grid[0]) - 1:
                    if grid[i][j + 1] != 1:
                        grid[i][j + 1] = 2 + grid[i][j + 1]
                if i < len(grid) - 1:
                    if grid[i + 1][j] != 1:
                        grid[i + 1][j] = 2 + grid[i + 1][j]
    s = 0
    for i in grid:
        for j in i:
            if j != 1:
                s = s + j

    return int(s / 2)
