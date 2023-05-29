"""
    Insertion Sorting
Insertion sort works by repeatedly inserting elements into their
correct positions, it iterates through the array, comparing each
element with its previous elements and swapping them until the
array is sorted.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def insertion_sort(array: list) -> list:
    for i in range(len(array))[1:]:
        key = array[i]

        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array


def insertion_sort_counting(array: list) -> tuple:
    """A version with counters for swaps and comparisons"""
    comparisons = 0
    swaps = 0

    for i in range(len(array))[1:]:
        key = array[i]

        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

            comparisons += 1
            swaps += 1

        array[j + 1] = key
        swaps += 1

    return array, comparisons, swaps
