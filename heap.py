class MaxHeap:
    """
    Construct a MaxHeap
    """

    # Initialize
    def __init__(self) -> None:
        self.heap = []
    
    # Get left child index
    def _left_child(self, index: int) -> int:
        return 2 * index + 1

    # Get right child index
    def _right_child(self, index: int) -> int:
        return 2 * index + 2
    
    # Get parent index
    def _parent(self, index: int) -> int:
        return (index - 1) // 2

    # Sink down value
    def _sink_down(self, index: int) -> None:
        max_index = index
        while (True):
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]):
                max_index = left_index
            
            if (right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]):
                max_index = right_index
            
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return

    # Swap values
    def _swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # Insert value
    def insert(self, value: int) -> None:
        self.heap.append(value)
        curr = len(self.heap) - 1

        while curr > 0 and self.heap[curr] > self.heap[self._parent(curr)]:
            self._swap(curr, self._parent(curr))
            curr = self._parent(curr)

    # Remove value
    def remove(self) -> int:
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value

my_heap = MaxHeap()