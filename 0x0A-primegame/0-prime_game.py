#!/usr/bin/python3
"""
This module contains the method to
solve the probel
"""


def isWinner(x, nums):
    """
    Determine the winner of the game
    """
    if x <= 0 or not nums or x >= 10000:
        return None

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if num >= 10000:
            return None
        numbers = list(range(2, num + 1))
        turn = 0  # maria = 0, ben = 1
        while numbers:
            prime_found = False
            for n in numbers:
                if isPrime(n):
                    prime_found = True
                    numbers = [x for x in numbers if x % n != 0]
                    break
            if not prime_found:
                break
            turn += 1

        if turn % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"


def isPrime(num):
    """
    Check if num is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
