from .bogosort import *
from .treesort import *
from .mergesort import *
from .quicksort import *
from .radixsort import *
from .shellsort import *
from .bubblesort import *
from .insertionsort import *
from .selectionsort import *


# BOGO SORT IS NOT A OPTION
SORTERS = {"selection_sort": [selection_sort, selection_sort_counting],
           "bubble_sort": [bubble_sort, bubble_sort_counting],
           "insertion_sort": [insertion_sort, insertion_sort_counting],
           "quick_sort": [quick_sort, quick_sort_counting],
           "merge_sort": [merge_sort, merge_sort_counting],
           "radix_sort": [radix_sort, None],
           "shell_sort": [shell_sort, shell_sort_counting],
           "tree_sort": [tree_sort, tree_sort_counting]}

EASTER_EGG = [[bogo_sort, None]]
