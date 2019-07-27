# coding=utf-8
"""Min Binary Heap Python implementation."""


class MinBinaryHeap:
    """Min Binary Heap class."""
    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Get index of parent of node i."""
        return (i - 1) // 2

    def left_child(self, i):
        """Get index of left child of node i."""
        return 2 * i + 1

    def right_child(self, i):
        """Get index of right child of node i."""
        return 2 * i + 2

    def insert_key(self, k):
        """Insert key to heap."""
        self.heap.append(k)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def decrease_key(self, i, new_k):
        """Decrease node i to value new_k."""
        self.heap[i] = new_k
        while i != 0 and self.heap[self.parent(i)] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        """Remove minimal element from heap."""
        if not len(self.heap):
            return -1
        elif len(self.heap) == 1:
            return self.heap.pop(0)
        else:
            root = self.heap[0]
            self.heap[0] = self.heap.pop(-1)
            self.heapify(0)
            return root

    def heapify(self, i):
        """Heapify a subtree with root at index i."""
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def delete_key(self, i):
        """Delete key i."""
        self.decrease_key(i, self.heap[0] - 1)
        self.extract_min()

    def get_min(self):
        """Get smallest element in heap."""
        return self.heap[0]


if __name__ == "__main__":
    mbh = MinBinaryHeap()
    mbh.insert_key(3)
    mbh.insert_key(2)
    mbh.delete_key(1)
    mbh.insert_key(15)
    mbh.insert_key(5)
    mbh.insert_key(4)
    mbh.insert_key(45)
    print(mbh.extract_min())
    print(mbh.get_min())
    mbh.decrease_key(2, 1)
    print(mbh.get_min())
