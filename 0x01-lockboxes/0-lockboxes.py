#!/usr/bin/python3
"""Solution to the lockboxes problem"""


def canUnlockAll(boxes):
    """Determine if all boxes can be opened."""
    # I used 'set' to duplication of keys and also speed up of lookup time
    keys_store = set()
    to_be_open_boxes = set()

    # there is always a key to open box 0
    to_be_open_boxes.add(0)

    while to_be_open_boxes:
        current_box = to_be_open_boxes.pop()
        # boundary check
        if 0 <= current_box < len(boxes):
            if current_box not in keys_store:
                keys_store.add(current_box)
                for key in boxes[current_box]:
                    if key not in keys_store:
                        to_be_open_boxes.add(key)
    return len(keys_store) == len(boxes)

#print(canUnlockAll([ [10, 3, 8, 9, 6, 5, 8, 1], [8, 5, 3, 7, 1, 8, 6], [5, 1, 9, 1], [], [6, 6, 9, 4, 3, 2, 3, 8, 5], [9, 4], [4, 2, 5, 1, 1, 6, 4, 5, 6], [9, 5, 8, 8], [6, 2, 8, 6] ]))
