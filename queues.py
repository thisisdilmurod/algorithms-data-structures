from typing import Optional

class Node:
    """
    Create a Node
    """
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class Queue:
    """
    Construct a Queue
    """

    # Initialize
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    # Enqueue Node
    def enqueue(self, value: int) -> None:
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    # Dequeue Node
    def dequeue(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    # Print Nodes
    def print_queue(self) -> None:
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
my_queue = Queue(1)