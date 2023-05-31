"""
"Menus" for selecting cases, sorters and how many tests to run
"""
from . import *


def select_amount_tests() -> int:
    """Allows the user to select how many tests they want to run"""
    amount_tests = 0
    while True:
        try:
            amount_tests = int(input("\nHow many tests should run to get a average time?\n"))
        except ValueError:
            print("Please type a digit equal or more than 1!")

        if amount_tests >= 1:
            break

        print("You must run at least one test.")

    return amount_tests


def select_cases() -> dict:
    """Allows the user to select what cases they want to run"""
    cases = TEST_CASES.keys()
    available_cases = ", ".join(cases)

    selected_cases = ["case1", "case2", "case3", "case4", "case5", "case6", "case7", "case8"]
    description = "\n".join([f"{case}: {desc}" for case, desc in CASES_DESC.items()])

    while True:
        print("\nType the name of a case to add or remove it from the selected cases or:\
              \n1. Remove all cases\
              \n2. Add all cases\
              \n3. Show description of the cases.\
              \n0. Run the selected cases.")
        print(f"Available Cases:\n{available_cases}")
        print(f"Selected Cases:\n{', '.join(selected_cases)}")
        option = input().lower()

        if option in cases:
            if option in selected_cases:
                selected_cases.remove(option)

            else:
                selected_cases.append(option)

        elif option == "1":
            selected_cases = []

        elif option == "2":
            selected_cases = list(cases)

        elif option == "3":
            print(f"Cases decription:\n{description}\n")

        elif option == "0":
            if not selected_cases:
                print("Select at least one case!")
                continue

            selected_cases = {case: TEST_CASES[case] for case in selected_cases}
            return selected_cases

        else:
            print("Option/Case unavailable!")


def select_sorters() -> list:
    """Allows the user to select which sorters to test"""
    sorters = SORTERS.keys()
    available_sorters = ", ".join(sorters)
    selected_sorters = []

    while True:

        print("\nType the name of a sorter to add or remove it from the selected sorters or:\
              \n1. Remove all sorters\
              \n2. Add all sorters\
              \n0. Test the selected sorters.")
        print(f"Available sorters:\n{available_sorters}")
        print(f"Selected sorters:\n{', '.join(selected_sorters)}")
        option = input().lower()

        if option in sorters:
            if option in selected_sorters:
                selected_sorters.remove(option)
            else:
                selected_sorters.append(option)

        elif option == "1":
            selected_sorters = []

        elif option == "2":
            selected_sorters = sorters

        elif option == "0":
            if not selected_sorters:
                return EASTER_EGG
                
            selected_sorters = [SORTERS[selected] for selected in selected_sorters]
            return selected_sorters

        else:
            print("Option/Sorter unavailable!")


def select_save(results: dict, cases: dict, amount_tests: int) -> None:
    """Allows the user to choose how and if he wants to save the results"""
    while True:
        option = input("You want to save the results in:\
                        \n1. In a spreedsheet and in graphs.\
                        \n2. Only in a spreedsheet.\
                        \n3. Only in graphs.\
                        \n4. Don't save the results.\n")

        if option in ["1", "2", "3"]:
            directory = directory_path(cases, amount_tests)

            if option == "1":
                save_dataframes(directory, results)
                save_graphs(directory, results)
                break

            elif option == "2":
                save_dataframes(directory, results)
                break

            elif option == "3":
                save_graphs(directory, results)
                break
        
        elif option == "4":
            break

        else:
            print("Option unavailable!")
