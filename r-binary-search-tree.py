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
    def __r_insert(self, current_node: int, value: int) -> Node:
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node


    def r_insert(self, value: int) -> None:
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    # Look up Node
    def __r_contains(self, current_node: int, value: int) -> bool:
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value: int) -> bool:
        return self.__r_contains(self.root, value)

    # Find minimum value
    def min_value(self, current_node: int) -> int:
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    # Delete Node
    def __delete_node(self, current_node: int, value: int) -> Node:
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(current_node.right, sub_tree_min)
        return current_node
    
    def delete_node(self, value: int) -> None:
        self.root = self.__delete_node(self.root, value)
    
my_tree = BinarySearchTree()