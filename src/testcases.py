import numpy as np
from numpy import random as rd
import random


# A very small list
case0 = np.arange(1, 11)
rd.shuffle(case0)

# A unordered list with 100 elements
case1 = np.arange(1, 101)
rd.shuffle(case1)

# A ordered list with 100 elementes
case2 = np.arange(1, 101)

# A reverse ordered list with 100 elements
case3 = np.arange(1, 101)
case3 = case3[::-1]

# A unordered list with 100 elements, 50 being repeated
case4 = np.arange(1, 51)
repeated_numbers = rd.choice(case4, size = 50)
case4 = np.append(case4, repeated_numbers)
rd.shuffle(case4)

# An empty list
case5 = np.array([])

# A list with a single element
case6 = np.array([5])

# A unordered list with 100 elements, one of them repeated 50 times
case7 = np.arange(1, 51)
repeated_number = random.randint(1, 50)
case7 = np.append(case7, ([repeated_number]*50))
rd.shuffle(case7)

# A unordered list with 1_000 elements
case8 = rd.randint(0, 1_000, 500)

# A unordered list with 10_000 elements
case9 = rd.randint(0, 10_000, 1_000)

# A unordered list with 50_000 elements
case10 = rd.randint(0, 50_000, 10_000)

# A unordered list with 100_000 elements
case11 = rd.randint(0, 100_000, 50_000)

# A unordered list with 200_000 elements
case12 = rd.randint(0, 200_000, 100_000)


TEST_CASES = {"case0": case0,
              "case1": case1,
              "case2": case2,
              "case3": case3,
              "case4": case4,
              "case5": case5,
              "case6": case6,
              "case7": case7,
              "case8": case8,
              "case9": case9,
              "case10": case10,
              "case11": case11,
              "case12": case12}

CASES_DESC = {"case0": "A unordered list with 10 elements",
              "case1": "A unordered list with 100 elements",
              "case2": "A ordered list with 100 elementes",
              "case3": "A reverse ordered list with 100 elements",
              "case4": "A unordered list with 100 elements, 50 being repeated",
              "case5": "An empty list",
              "case6": "A list with a single element",
              "case7": "A unordered list with 100 elements, one of them repeated 50 times",
              "case8": "A unordered list with 1,000 elements",
              "case9": "A unordered list with 10,000 elements",
              "case10": "A unordered list with 50.000 elements",
              "case11": "A unordered list with 100.000 elements",
              "case12": "A unordered list with 200.000 elements"}