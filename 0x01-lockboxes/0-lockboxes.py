#!/usr/bin/python3
'''A module for working with lockboxes.
'''

def canUnlockAll(boxes):
    """Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    """
    opened_boxes = set([0])
    
    # Initialize a list to keep track of the keys that have been obtained
    obtained_keys = boxes[0]
    
    # Iterate over the obtained keys and try to open new boxes
    while obtained_keys:
        # Remove a key from the obtained keys list
        key = obtained_keys.pop(0)
        
        if key < len(boxes) and key not in opened_boxes:
            opened_boxes.add(key)
            
            obtained_keys.extend(boxes[key])
        return len(opened_boxes) == len(boxes)
