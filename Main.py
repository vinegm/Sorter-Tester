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
    print(f"Vetor{i+1}:\n{test}")
    print("-" * 75)