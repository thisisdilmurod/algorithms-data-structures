class Node:
    """
    Create a Node
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Construct a Binary Search Tree
    """

    # Initialize
    def __init__(self) -> None:
        self.root = None

    # Insert Node
    def insert(self, value: int) -> bool:
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    # Look up Node
    def contains(self, value: int) -> bool:
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
my_tree = BinarySearchTree()

