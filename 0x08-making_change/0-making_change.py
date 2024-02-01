#!/usr/bin/python3
"""Solution to the problem
"""


def makeChange(coins, total):
    """return fewest number of changes (in coins) needed for given total
    """
    if total <= 0:
        return 0

    counter = 0
    index = len(coins) - 1
    coins = sorted(coins)
    while (True):
        if (total == coins[index]):
            return counter + 1
        if (total / coins[index]) > 1:
            total -= coins[index]
            counter += 1
        elif index >= 1:
            index -= 1
        else:
            if total == 0:
                return counter
            return -1
