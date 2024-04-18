#!/usr/bin/python3
"""
this module contains canUnlockAll methode
"""


def canUnlockAll(boxes):
    '''
    canUnlockAll methode
    '''
    open = True
    testOpen = []
    keys = []
    keysImpo = []
    for i in range(len(boxes)):
        testOpen.append(0)
    testOpen[0] = 1
    for a in boxes[0]:
        keys.append(a)
        keysImpo.append(a)
    for a in keys:
        if a < len(testOpen):
            testOpen[a] = 1
    keys = []
    for box_index in range(len(boxes)):
        if box_index == 0:
            continue
        if testOpen[box_index] == 1:
            for key in boxes[box_index]:
                keys.append(key)
                keysImpo.append(key)
            for key in keys:
                testOpen[key] = 1
        else:
            try:
                idx = keysImpo[box_index]
                for key in boxes[idx]:
                    keys.append(key)
                    for key in keys:
                        testOpen[key] = 1
            except Exception:
                return False

        keys = []
    return open
