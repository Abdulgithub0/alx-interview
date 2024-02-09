#!/usr/bin/python3
"""Solution
"""

def island_perimeter(grid):
    """return perimeter of the island form by the 1 in grid
    """
    length = 0

    for water in grid:
        for land in water:
            if land == 1:
                length += land
                break
    return length * 4
