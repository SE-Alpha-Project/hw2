"""
This module is an implementation of mergeSort that uses multiple helper methods
in rand.py to sort the array that is currently failing
"""

import rand

def merge_sort(arr):

    """
        This function implements the merge sort algorithm recursively.
        It divides the input array into two halves, sorts them separately,
        and then combines them using the recombine function
    """

    if len(arr) <= 1:
        return arr
    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):

    """
        This function is part of the merge sort algorithm. It takes two sorted
        arrays and combines them into a single sorted array. The function
        compares elements from both input arrays and merges them in ascending order.
    """

    left_index = 0
    right_index = 0
    merge_arr = []
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    for i in range(right_index, len(right_arr)):
        merge_arr.append(right_arr[i])

    for i in range(left_index, len(left_arr)):
        merge_arr.append(left_arr[i])

    return merge_arr

input_arr = rand.random_array([None] * 20)
arr_out = merge_sort(input_arr)

print(arr_out)
