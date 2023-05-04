import numpy as np

from Sorters import BubbleSort
from Sorters import InsertionSort
from Sorters import SelectionSort
from Sorters import MergeSort
from Sorters import QuickSort
from Sorters import RadixSort
from Sorters import ShellSort
from Sorters import TreeSort

def sorters():
    """Returns a array of the sorters for testing"""
    sorters = np.array([[BubbleSort.bubble2_sort, BubbleSort.bubble2_sort_counting],
                        [InsertionSort.insert_sort, InsertionSort.insert_sort_otimizado_counting],
                        [QuickSort.quick_sort, QuickSort.quick_sort_for_counting],
                        [MergeSort.merge_sort, MergeSort.merge_sort_counting],
                        [ShellSort.shellSort, ShellSort.shellSort_counting],
                        [SelectionSort.selectionSort, SelectionSort.selectionSort_counting],
                        [RadixSort.index_sort, None],
                        [TreeSort.tree_sort, TreeSort.tree_sort_counting]])
    return sorters
