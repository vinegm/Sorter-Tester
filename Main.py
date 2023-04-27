import numpy as np
import timeit
import os

import TestCases
import InsertionSort
import SelectionSort
import MergeSort
import QuickSort
import RadixSort
import ShellSort


def calculate_average_time(array_of_times):
    """Takes a array with times samples and calculates the average of them
    
    Parameters:
    array_of_times (np.array): Array containing the samples

    Returns:
    average_time: Time in average the algorithm took
    """
    sum_of_times = 0

    for i in range(array_of_times.size):
        sum_of_times += array_of_times[i]

    average_time = sum_of_times / array_of_times.size

    return average_time

def test_timing(array, sorter, amount_of_tests):
    """Tests a sorter a given amout of times to get a average time
    
    Parameters:
    array (np.array): Array used for the tests
    sorter: Sorter used for the tests
    amount_of_tests (int): How many tests will be made to get a average time

    Returns:
    average_time: Time the sorter took in average to complete the task
    """
    tests_made = 0
    test_times = np.array([])

    while (tests_made < amount_of_tests):
        test_array = np.copy(array)

        startTimer = timeit.default_timer()
        sorter(test_array)  # QuickSort.quick_sort_for_timing(test_array, 0, len(test_array)-1)  # Sorter, por enquanto só funciona um
        stopTimer = timeit.default_timer()

        test_times = np.append(test_times, (stopTimer - startTimer))

        tests_made += 1

    average_time = calculate_average_time(test_times)

    return average_time

def test_sorter(test_case, sorter, amout_of_tests):
    average_time = test_timing(test_case, sorter[0], amout_of_tests)
    sortedArray, comparisons, swaps = sorter[1](test)
    print(f"{sorter[0].__name__}:\
            \nMade {comparisons} comparisons and {swaps} swaps;\
            \nAverage time: {average_time:.6f}\
            \nSorted array:\n{sortedArray}")
    return 

sorters = np.array([[QuickSort.quick_sort, QuickSort.quick_sort_for_counting],
                    [SelectionSort.selectionSort, SelectionSort.selectionSort_counting]])

test_cases = TestCases.test_cases()
amount_of_tests = 250

print("-" * 50)
for i, test in enumerate(test_cases):
    print(f"Vetor{i+1}: {test}")
    print("-" * 50)
    for sorter in sorters:
        test_sorter(test, sorter, amount_of_tests)
        print("-" * 50)