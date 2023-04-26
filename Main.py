import numpy as np
from numpy import random as rd
import timeit
import os

import TestCases
import InsertionSort
import SelectionSort
import MergeSort
import QuickSort
import RadixSort
import ShellSort


test_cases = TestCases.test_cases()

print("-" * 75)
for i, test in enumerate(test_cases):
    comparisons = 0
    changes = 0

    sortedArray, comparisons, changes = QuickSort.quick_sort_for_counting(test, 0, len(test)-1, comparisons, changes)

    startTimer = timeit.default_timer()
    sortedArray = QuickSort.quick_sort_for_timing(test, 0, len(test)-1)
    stopTimer = timeit.default_timer()

    print(f"Vetor{i+1}: \
            \nForam feitas {comparisons} comparações e {changes} mudanças.\
            \nFoi ordenado em {(stopTimer - startTimer):.6f} segundos.\
            \nVetor ordenado:\n{sortedArray}")
    
    print("-" * 75)