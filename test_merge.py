from hw2_debugging import merge_sort

def test_empty_array():
    assert merge_sort([]) == []

def test_sorted_array():
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_unsorted_array():
    assert merge_sort([5, 1, 4, 2, 3]) == [1, 2, 3, 4, 5]
