from typing import Optional

class Node:
    """
    Create a Node
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class Stack:
    """
    Construct a Stack
    """

    # Initialize
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    # Push Node
    def push(self, value: int) -> None:
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    # Pop Node
    def pop(self) -> Optional[Node]:
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

    # Print Nodes
    def print_stack(self) -> None:
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_stack = Stack(1)