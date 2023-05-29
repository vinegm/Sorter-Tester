""""
    Merge Sorting
Merge sort works by cuting the array in half until we have
multiple arrays of 1 element, and then we _merge them in a
sorted manner.

Time Complexity: O(n log(n))
Space Complexity: O(n)
"""

def merge_sort(array: list) -> list:
    """A implementation of recursive merge sort"""        
    def _merge_sort(array: list) -> list:
        """Separates the list into two halves"""
        if len(array) <= 1:
            return array
        
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        left_half = _merge_sort(left_half)
        right_half = _merge_sort(right_half)
        
        return _merge(left_half, right_half)

    def _merge(left_half: list, right_half: list) -> list:
        """Merges the two halves in a sorted manner"""
        merged = []

        left_index = 0
        right_index = 0
        
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
            else:
                merged.append(right_half[right_index])
                right_index += 1
        
        merged.extend(left_half[left_index:])
        merged.extend(right_half[right_index:])
        
        return merged
    
    sorted_array = _merge_sort(array)

    return sorted_array


def merge_sort_counting(array: list) -> tuple:
    """A versions with counters for comparisons and swaps"""
    comparisons = 0
    swaps = 0
        
    def _merge_sort(array: list) -> list:
        """Separates the list into two halves"""
        if len(array) <= 1:
            return array
        
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        
        left_half = _merge_sort(left_half)
        right_half = _merge_sort(right_half)
        
        return _merge(left_half, right_half)

    def _merge(left_half: list, right_half: list) -> list:
        """Merges the two halves in a sorted manner"""
        nonlocal comparisons, swaps

        merged = []

        left_index = 0
        right_index = 0
        
        while left_index < len(left_half) and right_index < len(right_half):
            comparisons += 1

            if left_half[left_index] <= right_half[right_index]:
                merged.append(left_half[left_index])
                left_index += 1
                swaps += 1

            else:
                merged.append(right_half[right_index])
                right_index += 1
                swaps += 1
        
        merged.extend(left_half[left_index:])
        merged.extend(right_half[right_index:])
        
        return merged
    
    sorted_array = _merge_sort(array)

    return sorted_array, comparisons, swaps
