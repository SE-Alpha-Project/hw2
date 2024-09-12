"""
This module provides functions to generate random numbers.

It includes:
- `random_array(arr)`: Add numbers the given list with random integers between 1 and 100.
"""

import random

def random_array(arr):
    """
    Populates the provided array with random integers between 1 and 100.

    Parameters:
    arr (list): A list to be filled with random integers.

    Returns:
    list: The list filled with random integers.
    """
    for ind, _ in enumerate(arr):
        shuffled_num = random.randint(1, 100)
        arr[ind] = shuffled_num
    return arr
