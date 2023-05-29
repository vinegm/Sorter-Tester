"""
    Bogo Sorting
Bogosort is a highly inefficient sorting algorithm that
randomly shuffles an array and checks if it is sorted by
pure chance

Time Complexity: O((n+1)!)
Space Complexity: O(n)
"""
import random


def bogo_sort(array: list) -> list:

    def is_sorted(array: list) -> bool:
        """Check if the list is sorted"""
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False

        return True

    while not is_sorted(array):
        random.shuffle(array)

    return array


def bogo_sort_counting(array: list) -> list:
    comparisons = 0
    shuffles = 0

    def is_sorted(array: list) -> bool:
        """Check if the list is sorted"""
        nonlocal comparisons
        for i in range(len(array) - 1):
            comparisons += 1
            if array[i] > array[i + 1]:
                return False

        return True

    while not is_sorted(array):
        random.shuffle(array)
        shuffles += 1

    return array, comparisons, shuffles
