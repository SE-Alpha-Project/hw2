from hw2_debugging import merge_sort

def test_empty_array():
    assert merge_sort([]) == []

def test_sorted_array():
    assert merge_sort([1, 22, 23, 25, 31, 38, 39, 49, 56, 57, 60, 69, 77, 80, 87, 88, 90, 93, 93, 94]) == [1, 22, 23, 25, 31, 38, 39, 49, 56, 57, 60, 69, 77, 80, 87, 88, 90, 93, 93, 94]

def test_unsorted_array():
    assert merge_sort([74, 16, 30, 11, 52, 8, 36, 71, 95, 13, 85, 66, 42, 33, 90, 88, 50, 54, 100, 100]) == [8, 11, 13, 16, 30, 33, 36, 42, 50, 52, 54, 66, 71, 74, 85, 88, 90, 95, 100, 100]
