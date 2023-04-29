class TreeNode:
    """Main class of the tree, every node holds a value and two branches """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Inserts the values of the array in the binary tree"""
    if root == None:
        return TreeNode(value)  # Returns a node of the tree if the root is None
    
    if value < root.value:
        root.left = insert(root.left, value)  # For a value smaller than this node, we add it to the left branch
    else:
        root.right = insert(root.right, value)  # For a value bigger than this node, we add it to the left branch
    
    return root


def travel(root, sorted):
    """Travels thought the tree collecting the sorted values"""
    if root != None:  # Stops going though the nodes if there are no more nodes
        travel(root.left, sorted)  # Goes though the smaller values
        sorted.append(root.value)  # Appends a node to the sorted array
        travel(root.right, sorted)  # Goes though the bigger values


def tree_sort(array):
    """Creates the binary tree and collects the values from its nodes"""
    root = None  # Starts with a variable None for creation of the first node

    for value in array:
        root = insert(root, value)  # Insert the values from the array into the tree

    sorted = []  # Create a array for collecting the nodes of the tree
    travel(root, sorted)  # Travels though the nodes collecting them
    return sorted


def insert_counting(root, value, comparisons):
    """Inserts the values of the array in the binary tree"""
    if root == None:
        return TreeNode(value)  # Returns a node of the tree if the root is None
    
    comparisons[0] += 1

    if value < root.value:
        root.left = insert_counting(root.left, value, comparisons)  # For a value smaller than this node, we add it to the left branch
    else:
        root.right = insert_counting(root.right, value, comparisons)  # For a value bigger than this node, we add it to the left branch
    
    return root


def tree_sort_counting(array):
    root = None
    comparisons = [0]

    for value in array:
        root = insert_counting(root, value, comparisons)

    sorted = []
    travel(root, sorted)
    return sorted, comparisons[0], 0