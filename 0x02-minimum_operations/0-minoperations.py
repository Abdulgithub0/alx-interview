#!/usr/bin/python3
""" Solution to the minimum operation problem """


def minOperations(n):
    """compute the minimum operations needed to balance len(H) === n.
    Modeling the problem using linear equation of two variables
    By using the slope-intercept formula y = mx + b
    (6, 9), (4, 4) and (7, 12)  coordinates are possible solutions
    """
    # check for any number <= x intercept: [n, 4)
    if n <= 3:
        if n <= 1:
            return 0
        return n
    # change in y / change in x
    slope = int((12 - 9) / (7 - 6))
    # find b = y - mx
    y_intercept = 9 - 3 * 6
    # so for any given dependent n, there is:
    return int((n - y_intercept) / slope)
