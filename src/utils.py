import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import time


def calculate_average_time(array_times: list) -> int:
    """Takes a array with times samples and calculates the average of them
    
    Parameters:
    array_times(np.array): Array containing the samples

    Returns:
    average_time(int): Time in average the algorithm took in microseconds
    """
    sum_times = 0

    # Calculate the sum of the times
    for i in array_times:
        sum_times += i

    # Calculates the average time 1.000.000 to turn the value into a int
    average_time = int((sum_times / len(array_times))*1_000_000)

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
        startTimer = time.perf_counter()
        sorter(case)
        stopTimer = time.perf_counter()

        test_times = np.append(test_times, (stopTimer - startTimer))

        tests_made += 1

    # Calculates the average time across all the tests
    average_time = calculate_average_time(test_times)

    return average_time


def test_sorter(test_case: list, sorter, amount_tests: int) -> tuple:
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
    # Makes a copy of the case, so one test doesn't effect the other
    case = np.copy(test_case)

    # Calculates the average time of the sorter
    average_time = test_timing(case, sorter[0], amount_tests)

    # If doesn't have a sorter for counting comparisons/swaps, sets them to 0
    if sorter[1] == None:
        comparisons = 0
        swaps = 0
        return average_time, comparisons, swaps

    # Tests amount of comparisons and swaps
    sorted_array, comparisons, swaps = sorter[1](case)

    if not np.array_equal(sorted_array, sorted(test_case)):
        print(sorted_array)
        raise Exception(f"Sorter Not Working!")
    
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


def show_dataframes(cases):
    """Prints each case on the terminal

    Parameters:
    cases (Array): Array of cases that will be shown on the terminal 
    """
    print("-" * 50)
    for i in range(len(cases)):
        print(f"Case{i+1}:\
                \n{cases[i]}")
        print("-" * 50)


def show_graphs(cases):
    """Makes a window for each case with graphs

    Parameters:
    cases (Array): Array of cases that will be shown in a window each
    """
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
