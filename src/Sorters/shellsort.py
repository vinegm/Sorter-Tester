"""
    Shell Sorting
Shell sort is similar to insertion sort, but it starts
by sorting elements that are far apart and progressively
reduces the gap between elements to be compared.

Time Complexity: O(n log(n))
Space Complexity: O(1)
"""

def shell_sort(array: list) -> list:
    n = len(array)

    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        gap //= 2

    return array


def shell_sort_counting(array: list) -> list:
    comparisons = 0
    swaps = 0

    n = len(array)

    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap

                comparisons += 1
                swaps += 1

            if i != j:
                array[j] = temp
                swaps += 1

        gap //= 2

    return array, comparisons, swaps