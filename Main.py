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


def flip_state(*args):
    """Flips the state of one or multiple booleans
    
    Parameters:
    *args (bool): Boolean or booleans that will be flipped
    
    Retuns:
    fliped_states (array): Array of the flipped booleans
    """
    fliped_states = []
    for bool in args:
        bool = not bool
        fliped_states.append(bool)
    return fliped_states


def choose_cases():
    test_cases = TestCases.test_cases()
    tests_run = [True for _ in range(len(test_cases))]
    while True:
        print(tests_run)
        flip = int(input(f"\nChoose which cases to run?\
                         \n1. An unordered list with numbers 1 to 100. {tests_run[0]}\
                         \n2. An ascending ordered list with numbers 1 to 100. {tests_run[1]}\
                         \n3. A descending ordered list with numbers 100 to 1. {tests_run[2]}\
                         \n4. A list with 100 numbers, 1 to 50, every number appers twice. {tests_run[3]}\
                         \n5. An empty list. {tests_run[4]}\
                         \n6. A list with a single number. {tests_run[5]}\
                         \n7. A list with 100 numbers, 1 to 50, one number appers 50 times. {tests_run[6]}\
                         \n8. An unordered list with 1.000 numbers, randomly picked between 1 and 10.000. {tests_run[7]}\
                         \n0. Run the chosen tests."))
        if flip == 0:
            break
        elif flip > 8:
            print("This test doesn't exist.")
        else:
            temp = flip_state(tests_run[flip-1])
            tests_run[flip-1] = temp[0]
    
    run_cases = []
    for i, run in enumerate(tests_run):
        if run == True:
            run_cases.append(test_cases[i])
    print(run_cases)
    return run_cases


if __name__ == "__main__":

    while True:
        select_tests = input("\nDo you want to run the standard tests cases?\
                            \n1. Yes, run the already stablished tests cases.\
                            \n2. I want to edit what tests will be run.\n")
        if select_tests == "1":
            test_cases = TestCases.test_cases()  # Gets the test cases
            break
        elif select_tests == "2":
            test_cases = choose_cases()  # Ask the user what tests to run
            break
        else:
            print("Option unavailable.")

    sorters = Sorters.sorters()
    print(sorters)

    while True:
        amount_tests = int(input("\nHow many tests should be made to get an average time?\n"))
        if amount_tests > 0:
            break
        print("Amount of tests must be more than 0.")

    in_console = input("\nDo you want the tests results to be printed to the console?\
                       \n1. Yes\
                       \n2. No\n")
    
    in_graph = input("\nDo you want the tests results to shown in graphs?\
                     \n1. Yes\
                     \n2. No\n")
    
    # Tests the sorters on the given tests and returns the results in data frames
    cases = test_sorters(test_cases, sorters, amount_tests)

    if in_console == "1":
        show_dataframes(cases)
    if in_graph == "1":
        show_graphs(cases)
