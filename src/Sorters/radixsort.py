"""
    Radix Sorting
Radix sorts values by their individual digits,
it processes the elements digit by digit, from
the least significant to the most significant,
placing them in buckets and collecting afterwards.

Time Complexity: O(d*(n+k))
Space Complexity: O(n+k)
"""

def radix_sort(array: list) -> list:

    def _counting_sort(array, exponent):
        """Uses counting sort for every exponent"""
        n = len(array)

        count = [0] * 10
        output = [0] * n

        for i in range(n):
            index = (array[i] // exponent) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (array[i] // exponent) % 10
            output[count[index] - 1] = array[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            array[i] = output[i]

        return array

    max_value = max(array)
    exponent = 1
    while max_value // exponent > 0:
        sorted_array = _counting_sort(array, exponent)
        exponent *= 10

    return sorted_array


# Radix sort doesn't make swaps and comparisons
