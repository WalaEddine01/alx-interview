#!/usr/bin/python3
"""
this module contains canUnlockAll methode
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.
    """
    unlocked = [0] * len(boxes)
    unlocked[0] = 1
    keys = set(boxes[0])

    keys_to_process = list(keys)

    while keys_to_process:
        current_key = keys_to_process.pop(0)

        if current_key < len(boxes) and not unlocked[current_key]:
            unlocked[current_key] = 1

            for new_key in boxes[current_key]:
                if new_key not in keys:
                    keys.add(new_key)
                    keys_to_process.append(new_key)

    return all(unlocked)
