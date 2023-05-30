import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy
import time
from pathlib import Path


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


def test_timing(test_case: list, sorter, amount_tests: int) -> int:
    """Tests a sorter a given amount of times to get a average time
    
    Parameters:
    test_case(list/np.array): Array used for the tests
    sorter: Sorter used for the tests
    amount_tests(int): How many tests will be made to get a average time

    Returns:
    average_time(int): Time the sorter took in average to complete the task
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
    test_case(array): Test that will be run
    sorter(list): Sorter that will be tested
    amount_tests(int): How many tests will be made to get a average time for sorting

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


def test_sorters(test_cases: dict, sorters, amount_tests: list) -> list:
    """Tests the average time, amount of comparisons and swaps for multiple sorters in multiple tests
    
    Parameters:
    test_cases(list) = list of cases to be tested on
    sorters(list) = List of sorters to be tested
    amount_tests(int) = Amount of tests that will be run

    Returns:
    cases(list) = List of data frames for each test case, containing the results for every sorter 
    """
    # Creates a dict for storing the results
    data = {"sorter": [],
            "average time": [],
            "comparisons": [],
            "swaps": []}
    results = {}

    print("-" * 25)
    for case_name, case in test_cases.items():
        print(f"{case_name}:")
        case_results = copy.deepcopy(data)
        for sorter in sorters:

            print(f"Testing {sorter[0].__name__}...")

            # Test the one sorter at a time in a case
            average_time, comparisons, swaps = test_sorter(case, sorter, amount_tests)
            
            # Stores the results
            case_results["sorter"].append(sorter[0].__name__)
            case_results["average time"].append(average_time)
            case_results["comparisons"].append(comparisons)
            case_results["swaps"].append(swaps)
        
        # Turns the dict into a data frame
        results[case_name] = pd.DataFrame(case_results)
        print("-" * 25)

    return results


def directory_path(cases: list) -> Path:
    """Returns a file path based on the cases and tests that ran"""
    # WIP only returns a dir called "results", if it already exist it gives it a new name like "results (#)"
    results_dir = Path("results")

    directory = results_dir / "test"

    i = 0
    while directory.exists():
        i += 1
        directory = results_dir / f"test {i}"
        

    directory.mkdir(parents=True)

    return directory


def save_dataframes(directory: Path, cases: dict) -> None:
    """Saves the results to a excel

    Parameters:
    directory(Path): Where the results will be saved
    cases(dict): Dict of cases that will be saved in a excel
    """
    with pd.ExcelWriter(f"{directory}/Results.xlsx") as writer:
        for case, results in cases.items():
            results.to_excel(writer, sheet_name = case, index = False)


def save_graphs(directory: Path, cases: dict) -> None:
    """Saves a png for each case

    Parameters:
    cases(dict): Dict of cases that will be saved
    """
    for case, results in cases.items():
        fig, axs = plt.subplots(3, 1, figsize=(5, 5))
        
        axs[0].bar(results["sorter"], results["average time"], color = "y")
        axs[0].set_title(case)
        axs[0].set_ylabel("Time (microseconds)")
        
        axs[1].bar(results["sorter"], results["comparisons"], color = "b")
        axs[1].set_ylabel("Comparisons")
    
        axs[2].bar(results["sorter"], results["swaps"], color = "g")
        axs[2].set_xlabel("Sorter")
        axs[2].set_ylabel("Swaps")
        
        plt.tight_layout()
    
        plt.savefig(f"{directory}/{case}.png")
