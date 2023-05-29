import numpy as np
from numpy import random as rd
import random


# A unordered list with 100 elements
case1 = list(range(1, 101))
random.shuffle(case1)

# A ordered list
case2 = list(range(1, 101))

# A reverse ordered list
case3 = list(range(1, 101))
case3.reverse()

# A list with repeated numbers
case4 = list(range(1, 51))
repeated_numbers = random.sample(case4, 50)
case4 = np.append(case4, repeated_numbers)
random.shuffle(case4)

# An empty list
case5 = np.array([])

# A list with a single element
case6 = np.array([5])

# A list with a element repeated multiple times
case7 = list(range(1, 51))
repeated_number = random.randint(1, 50)
case7 = np.append(case7, ([repeated_number]*50))
random.shuffle(case7)

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


TEST_CASES = [case1, case2, case3, case4, case5, case6, case7, case8, case9, case10, case11, case12]
