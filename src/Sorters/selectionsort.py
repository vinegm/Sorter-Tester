"""
    Selection Sorting
Selection sort works by repeatedly finding the smaller or bigger
element from the unsorted part of the array and swapping it with
the first element.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def selection_sort(array: list) -> list:
    """A simple implementation of selection sort"""
    n = len(array)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                
        array[i], array[min_index] = array[min_index], array[i]
    
    return array


def selection_sort_counting(array: list) -> tuple:
    """A selection sort algorithm with counters for swaps and comparisons"""
    comparisons = 0
    swaps = 0

    n = len(array)

    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            comparisons += 1
            if array[j] < array[min_index]:
                min_index = j
        
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]
            swaps += 1

    return array, comparisons, swaps
