#!/usr/bin/python3
"""
tHIS MODULE CONTAINS THE minOperations METHED
"""


def minOperations(n: int) -> int:
    """
    this is the minOperations method
    """
    if n <= 0:
        return 0
    op = 0
    num = n
    k = []
    while num > 1:
        if isPrime(int(num)):
            k.append(int(num))
            break
        else:
            for i in range(2, num + 1):
                if num % i == 0:
                    num = int(num / i)
                    k.append(i)
                    break
    return sum(k)


def isPrime(n: int) -> bool:
    """
    Check if the num is prime
    """
    if n == 2 or n == 1:
        return True
    for i in range(1, n):
        if i != 1 and i != n and n % i == 0:
            return False

    return True
