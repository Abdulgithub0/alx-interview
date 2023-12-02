#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
    - Returns an empty list if n <= 0
    - You can assume n will be always an integer
"""


def pascal_triangle(n: int = None) -> list[list[int]]:
    """compute a 2D list of elements representing pascal triangle for N height"""

    if ( not n or n <= 0): return []
    grid: list[list[int]] = [[1], [1, 1]]

    for i in range(2, n):
        new: list[int] = [1]
        for j in range(1, i):
            new.append(grid[i - 1][j] + grid[i - 1][j - 1])
        new.append(1)
        grid.append(new)
    return grid
