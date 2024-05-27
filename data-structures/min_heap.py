class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _heapify_up(self, index):
        parent_index = self._parent(index)
        if index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        smallest = index
        left = self._left_child(index)
        right = self._right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            raise IndexError("extract_min from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

min_heap = MinHeap()
min_heap.insert(10)
min_heap.insert(5)
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(8)

print("Min-Heap:", min_heap)
print("Extract Min:", min_heap.extract_min())
print("Min-Heap after extraction:", min_heap)
print("Peek:", min_heap.peek())
