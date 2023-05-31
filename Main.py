from src.menu import *


if __name__ == "__main__":
    selected_cases = select_cases()
    selected_sorters = select_sorters()
    amount_tests = select_amount_tests()

    results = test_sorters(selected_cases, selected_sorters, amount_tests)
    
    save_cases = "\n\n".join([f"{case}: {desc}" for case, desc in selected_cases.items()])
    select_save(results, save_cases, amount_tests)
