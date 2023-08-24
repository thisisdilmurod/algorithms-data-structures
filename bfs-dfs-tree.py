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
    
    # Implement a Breadth-First-Search algorithm
    def bfs(self) -> list[int]:
        curr_node = self.root
        queue = []
        results = []
        queue.append(curr_node)
        
        while len(queue) > 0:
            curr_node = queue.pop(0)
            results.append(curr_node.value)
            if curr_node.left is not None:
                queue.append(curr_node.left)
            if curr_node.right is not None:
                queue.append(curr_node.right)
        return results

    # Implement a Depth-First-Search PreOrder algorithm
    def dfs_pre_order(self) -> list[int]:
        results = []
        def traverse(curr_node: Node) -> None:
            results.append(curr_node.value)
            if curr_node.left is not None:
                traverse(curr_node.left)
            if curr_node.right is not None:
                traverse(curr_node.right)
        traverse(self.root)
        return results # [47, 21, 18, 27, 76, 52, 82]

    # Implement a Depth-First-Search PostOrder algorithm
    def dfs_post_order(self) -> list[int]:
        results = []
        def traverse(curr_node: Node) -> None:
            if curr_node.left is not None:
                traverse(curr_node.left)
            if curr_node.right is not None:
                traverse(curr_node.right)
            results.append(curr_node.value)
        traverse(self.root)
        return results # [18, 27, 21, 52, 82, 76, 47]

    # Implement a Depth-First-Search InOrder algorithm
    def dfs_in_order(self) -> list[int]:
        results = []
        def traverse(curr_node: Node) -> None:
            if curr_node.left is not None:
                traverse(curr_node.left)
            results.append(curr_node.value)
            if curr_node.right is not None:
                traverse(curr_node.right)
        traverse(self.root)
        return results # [18, 21, 27, 47, 52, 76, 82]

    
my_tree = BinarySearchTree() # [47, 21, 76, 18, 27, 52, 82]