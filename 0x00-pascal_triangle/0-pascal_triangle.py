#!/usr/bin/python3
"""A pascal triangle"""

def pascal_triangle(n: int = None) -> list[list[int]]:
    """
    create 2D list of elements representing Pascal's triangle for N.
    
    :param n: The height of Pascal's triangle.
    :type n: int
    :return: A list of lists representing Pascal's triangle.
    :rtype: list[list[int]]
    """
    if not n or n <= 0:
        return []

    grid: list[list[int]] = [[1]]

    for i in range(1, n):
        new: list[int] = [1]

        for j in range(1, i):
            new.append(grid[i - 1][j] + grid[i - 1][j - 1])

        new.append(1)
        grid.append(new)

    return grid
