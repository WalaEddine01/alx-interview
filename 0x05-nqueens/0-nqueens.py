#!/usr/bin/python3
"""
This module contains the method that solvs the
n queens problem
"""
from sys import argv


def nqueens(n):
    """
    The nqueens method
    """
    solutions = []
    solve(n, 0, [], solutions)
    return solutions


def solve(n, row, queens, solutions):
    """
    The solve method
    """
    if row == n:
        solutions.append(queens[:])
        return

    for col in range(n):
        if is_valid(queens, row, col):
            queens.append((row, col))
            solve(n, row + 1, queens, solutions)
            queens.pop()


def is_valid(queens, row, col):
    """
    The is_valid method
    """
    for r, c in queens:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isnumeric():
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = nqueens(N)
    for solution in solutions:
        print([solution])
