"""
    Quick Sorting
Quick sort is a popular divide-and-conquer sorting algorithm that efficiently
sorts a list of elements, it selects a pivot element, partitions the list around
the pivot, and recursively sorts the sublists created on either side of the pivot.

Time Complexity: O(n log(n))
Space Complexity: O(n)
"""

def quick_sort(array: list) -> list:
    """A quick sort implementation using a the median-of-Three approach for selecting a pivot"""
    def _quick_sort(array, low, high):
        """Sorts the list using quick sort"""
        if low < high:
            split = _partition(array, low, high)

            _quick_sort(array, low, split - 1)
            _quick_sort(array, split + 1, high)

        return array

    def _partition(array, low, high):
        """Selects the poin where the list will be split"""
        median = _median_of_three(array, low, high)
        pivot = array[median]
        array[median], array[high] = array[high], array[median]

        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i+1], array[high] = array[high], array[i+1]

        return i + 1

    def _median_of_three(array, low, high):
        """Selects the median of the lower, higher and middle of the list
        while ensuring the three are in order"""
        mid = (low + high) // 2

        if array[low] > array[mid]:
            array[low], array[mid] = array[mid], array[low]

        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]

        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]

        return mid

    sortedArray = _quick_sort(array, 0, len(array)-1)

    return sortedArray


def quick_sort_counting(array: list) -> tuple:
    """Version for counting comparisons and swaps the algorithm made"""
    comparisons = 0
    swaps = 0

    def _quick_sort(array, low, high):
        """Sorts the list using quick sort"""
        if low < high:
            split = _partition(array, low, high)

            _quick_sort(array, low, split - 1)
            _quick_sort(array, split + 1, high)

        return array

    def _partition(array, low, high):
        """Selects the poin where the list will be split"""
        nonlocal comparisons, swaps

        median = _median_of_three(array, low, high)
        pivot = array[median]
        array[median], array[high] = array[high], array[median]
        
        i = low - 1
        for j in range(low, high):
            comparisons += 1
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                swaps += 1

        array[i+1], array[high] = array[high], array[i+1]
        swaps += 1

        return i + 1

    def _median_of_three(array, low, high):
        """Selects the median of the lower, higher and middle of the list
        while ensuring the three are in order"""
        nonlocal comparisons, swaps

        mid = (low + high) // 2

        comparisons += 1
        if array[low] > array[mid]:
            array[low], array[mid] = array[mid], array[low]
            swaps += 1

        comparisons += 1
        if array[low] > array[high]:
            array[low], array[high] = array[high], array[low]
            swaps += 1

        comparisons += 1
        if array[mid] > array[high]:
            array[mid], array[high] = array[high], array[mid]
            swaps += 1

        return mid

    sortedArray = _quick_sort(array, 0, len(array)-1)

    return sortedArray, comparisons, swaps
