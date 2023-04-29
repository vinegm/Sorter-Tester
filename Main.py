import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import timeit
import os

import TestCases
from Sorters import Sorters

def calculate_average_time(array_times):
    """Takes a array with times samples and calculates the average of them
    
    Parameters:
    array_times (np.array): Array containing the samples

    Returns:
    average_time: Time in average the algorithm took in microseconds
    """
    sum_times = 0

    # Calculate the sum of the times
    for i in range(array_times.size):
        sum_times += array_times[i]

    # Calculates the average time 1.000.000 to turn the value into a int
    average_time = int((sum_times / array_times.size)*1_000_000)

    return average_time


def test_timing(test_case, sorter, amount_tests):
    """Tests a sorter a given amount of times to get a average time
    
    Parameters:
    test_case (np.array): Array used for the tests
    sorter: Sorter used for the tests
    amount_tests (int): How many tests will be made to get a average time

    Returns:
    average_time: Time the sorter took in average to complete the task
    """
    tests_made = 0
    # Creates an empty array to store the results of every test
    test_times = np.array([])

    while (tests_made < amount_tests):
        # Makes a copy of the test case to not interfere in the next tests
        case = np.copy(test_case)

        # Times the sorter doing its task
        startTimer = timeit.default_timer()
        sorter(case)
        stopTimer = timeit.default_timer()

        test_times = np.append(test_times, (stopTimer - startTimer))

        tests_made += 1

    # Calculates the average time across all the tests
    average_time = calculate_average_time(test_times)

    return average_time


def test_sorter(test_case, sorter, amount_tests):
    """Tests a given sorter
    
    Parameters:
    test_case (array): Test that will be run
    sorter (array): Sorter that will be tested
    amount_tests (int): How many tests will be made to get a average time for sorting

    Returns:
    average_time: Average time of the sorter to complete the task on the given test
    comparisons: How many comparisons the sorter made
    swaps: How many comparisons the sorter swaps
    """
    # Makes a copy of the case, so one test doesnt effect the other
    case = np.copy(test_case)

    # Calculates the average time of the sorter
    average_time = test_timing(case, sorter[0], amount_tests)

    # If doesn't have a sorter for couting comparisons/swaps, sets them to 0
    if sorter[1] == None:
        comparisons = 0
        swaps = 0
        return average_time, comparisons, swaps

    # Tests amount of comparisons and swaps
    sortedArray, comparisons, swaps = sorter[1](case)
    
    return average_time, comparisons, swaps


def test_sorters(test_cases, sorters, amount_tests):
    """Tests the average time, amount of comparisons and swaps for multiple sorters in multiple tests
    
    Parameters:
    test_cases (array) = Array of cases to be tested on
    sorters (array) = Array of sorters to be tested
    amount_tests (int) = Amount of tests that will be run

    Returns:
    cases (array) = Array of data frames for each test case, containing the results for every sorter 
    """
    # Creates a dict for storing the results
    data = {"sorter": [],
            "average time": [],
            "comparisons": [],
            "swaps": []}
    # Creates slots for results equals to the amount of test cases
    cases = [copy.deepcopy(data) for _ in range(len(test_cases))]

    print("-" * 25)
    for i, case in enumerate(test_cases):  # Iterates though every test case
        print(f"\tCase{i+1}:")
        for sorter in sorters:  # Iterates though every sorter

            print(f"Testing {sorter[0].__name__}...")

            # Test the one sorter at a time in a case
            average_time, comparisons, swaps = test_sorter(case, sorter, amount_tests)
            
            # Stores the results
            cases[i]["sorter"].append(sorter[0].__name__)
            cases[i]["average time"].append(average_time)
            cases[i]["comparisons"].append(comparisons)
            cases[i]["swaps"].append(swaps)
        
        # Turns the dict into a data frame
        cases[i] = pd.DataFrame(cases[i])
        print("-" * 25)
    return cases


sorters = np.array([[Sorters.BubbleSort.bubble2_sort, Sorters.BubbleSort.bubble2_sort_counting],
                    [Sorters.InsertionSort.insert_sort, Sorters.InsertionSort.insert_sort_otimizado_counting],
                    [Sorters.QuickSort.quick_sort, Sorters.QuickSort.quick_sort_for_counting],
                    [Sorters.MergeSort.merge_sort, Sorters.MergeSort.merge_sort_counting],
                    [Sorters.ShellSort.shellSort, Sorters.ShellSort.shellSort_counting],
                    [Sorters.SelectionSort.selectionSort, Sorters.SelectionSort.selectionSort_counting],
                    [Sorters.RadixSort.index_sort, None],
                    [Sorters.TreeSort.tree_sort, Sorters.TreeSort.tree_sort_counting]])


test_cases = TestCases.test_cases()  # Gets the test cases
amount_tests = 1  # Sets the amount of tests to be made on each case

# Tests the sorters on the given tests and returns the results in data frames
cases = test_sorters(test_cases, sorters, amount_tests)

# Prints the data frames of each case to the termial
print("-" * 50)
for i in range(len(cases)):
    print(f"Case{i+1}:\
          \n{cases[i]}")
    print("-" * 50)

# Opens a window for each test case with their info
for i, case in enumerate(cases):
    fig, axs = plt.subplots(3, 1, figsize=(5, 5))
    
    axs[0].bar(case["sorter"], case["average time"], color = "y")
    axs[0].set_title(f"Case Test {i+1}")
    axs[0].set_ylabel("Time (microseconds)")
    
    axs[1].bar(case["sorter"], case["comparisons"], color = "b")
    axs[1].set_ylabel("Quantity of Comparisons")

    axs[2].bar(case["sorter"], case["swaps"], color = "g")
    axs[2].set_xlabel("Sorter")
    axs[2].set_ylabel("Quantity of Swaps")
    
    plt.tight_layout()

plt.show()
