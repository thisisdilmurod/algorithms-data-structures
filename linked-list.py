from typing import Optional

class Node:
    """"
    Create a new Node
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class LinkedList:
    """
    Construct a Linked List
    """

    # Initialize
    def __init__(self, value: int) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # Add Node to end
    def append(self, value: int) -> bool:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Pop Node
    def pop(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Add Node to beginning
    def prepend(self, value: int) -> bool:
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Pop first Node
    def pop_first(self) -> Optional[Node]:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    # Get Node
    def get(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    # Set Node
    def set_value(self, index: int, value: int) -> bool:
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False

    # Insert Node
    def insert(self, index: int, value: int) -> bool:
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    # Remove Node
    def remove(self, index: int) -> Optional[Node]:
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    # Reverse Node
    def reverse(self) -> None:
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Print Linked List
    def print_list(self) -> None:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

# Create a new Node with a value of 1
my_linked_list = LinkedList(1)