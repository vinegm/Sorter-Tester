from src import *


if __name__ == "__main__":
    results = test_sorters(TEST_CASES, [SORTERS[3], SORTERS[7]], 1)

    directory = directory_path(results)

    save_dataframes(directory, results)

    save_graphs(directory, results)
