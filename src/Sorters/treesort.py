"""
    Tree Sorting
Tree sort is a sorting algorithm that works by constructing a binary search
tree from the elements of the input array and then performing an in-order
traversal of the tree to obtain the sorted array sequence.

Time Complexity: O(n log(n))
Space Complexity: O(n)
"""


class TreeNode:
    """Main class of the tree, every node holds a value and two branches """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Inserts the values of the array in the binary tree"""
    if root == None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    
    return root


def travel(root, sorted_array):
    """Travels thought the tree collecting the sorted_array values"""
    if root != None:
        travel(root.left, sorted_array)
        sorted_array.append(root.value)
        travel(root.right, sorted_array)


def tree_sort(array: list) -> list:
    """Creates the binary tree and collects the values from its nodes"""
    root = None

    for value in array:
        root = insert(root, value)

    sorted_array = []
    travel(root, sorted_array)

    return sorted_array


def insert_counting(root, value, comparisons):
    """Inserts the values of the array in the binary tree"""
    if root == None:
        return TreeNode(value)
    
    comparisons[0] += 1
    if value < root.value:
        root.left = insert_counting(root.left, value, comparisons)
    else:
        root.right = insert_counting(root.right, value, comparisons)
    
    return root


def tree_sort_counting(array: list) -> tuple:
    """Creates the binary tree and collects the values from its nodes while counting comparisons"""
    root = None
    comparisons = [0]

    for value in array:
        root = insert_counting(root, value, comparisons)

    sorted_array = []
    travel(root, sorted_array)
    
    return sorted_array, comparisons[0], 0
