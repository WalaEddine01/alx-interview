#!/usr/bin/python3
"""
tHIS MODULE CONTAINS THE minOperations METHED
"""


def minOperations(n: int) -> int:
    """
    this is the minOperations method
    """
    op = 0
    num = n
    while True:
        if isPrime(int(num)):
            op = (op * 2) + int(num)
            return op
        else:
            op = op + 1
            num = int(num / 2)


def isPrime(n: int) -> bool:
    """
    Check if the num is prime
    """
    if n == 2 or n == 1:
        return True
    for i in range(1, n):
        if i != 1 and i != n and n % 2 == 0:
            return False

    return True
