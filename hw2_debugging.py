"""
This module is an implementation of mergeSort that uses multiple helper methods
in rand.py to sort the array that is currently failingggg
"""

import rand

def merge_sort(arr):

    """
        This function implements the merge sort algorithm recursively.
        It divides the input array into two halves, sorts them separately,
        and then combines them using the recombine function
    """
    n = len(arr)
    if n <= 1:
        return arr
    half = n//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):

    """
        This function is part of the merge sort algorithm. It takes two sorted
        arrays and combines them into a single sorted array. The function
        compares elements from both input arrays and merges them in ascending order.
    """

    left_index = 0
    right_index = 0
    merged_arr = [None]*(len(left_arr) + len(right_arr))
    index = 0

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merged_arr[index] = left_arr[left_index]
            left_index += 1
        else:
            merged_arr[index] = right_arr[right_index]
            right_index += 1
        index += 1

    while left_index < len(left_arr):
        merged_arr[index] = left_arr[left_index]
        left_index += 1
        index += 1

    while right_index < len(right_arr):
        merged_arr[index] = right_arr[right_index]
        right_index += 1
        index += 1

    return merged_arr

input_arr = rand.random_array([None] * 20)
arr_out = merge_sort(input_arr)

print(arr_out)
