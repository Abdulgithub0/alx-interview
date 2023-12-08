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
