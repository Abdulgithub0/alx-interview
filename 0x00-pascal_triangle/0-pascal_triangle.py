#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of integers representing
the Pascal’s triangle of n:
    - Returns an empty list if n <= 0
    - You can assume n will always be an integer
"""

def pascal_triangle(n):
    """
    Compute a 2D list of elements representing Pascal's triangle for N.
    
    :param n: The height of Pascal's triangle.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list[list[int]]
    """

    if not n or n <= 0:
        return []

    grid = [[1]]

    for i in range(1, n):
        new = [1]
        for j in range(1, i):
            new.append(grid[i - 1][j] + grid[i - 1][j - 1])
        new.append(1)
        grid.append(new)

    return grid
