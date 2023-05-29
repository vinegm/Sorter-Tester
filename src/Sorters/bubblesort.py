"""
    Bubble Sorting
Bubble sort is a simple sorting algorithm that repeatedly steps through a list,
compares adjacent elements, and swaps them if they are in the wrong order.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def bubble_sort(array: list) -> list:
    """A revised version of bubble sort"""
    n = len(array)

    is_swaping = True
    while is_swaping: 
        is_swaping = False

        for i in range(n-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]

                is_swaping = True

        n -= 1

    return array


def bubble_sort_counting(array: list) -> tuple:
    """Version for counting comparisons and swaps the algorithm made"""
    comparisons = 0
    swaps = 0

    n = len(array)

    is_swaping = True
    while is_swaping:
        is_swaping = False

        for i in range(n-1):
            comparisons += 1
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swaps +=1

                is_swaping = True

        n -= 1

    return array, comparisons, swaps
