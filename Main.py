from src import *


if __name__ == "__main__":
    results = test_sorter(TEST_CASES[8], SORTERS[1], 5)

    print(f"The sorter took {results[0]} microseconds")
    print(f"Comparisons: {results[1]}")
    print(f"swaps: {results[2]}")
