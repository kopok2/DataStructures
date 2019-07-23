"""Queue Python implementation using linked list."""


class Node:
    """Node contains items value and reference to the next item in chain."""
    def __init__(self, value):
        self.value = value
        self.next_item = None


class QueueLinkedList:
    def __init__(self):
        self.front_n = None
        self.rear_n = None

    def enqueue(self, value):
        n = Node(value)
        if self.rear_n:
            self.rear_n.next_item = n
            self.rear_n = n
        else:
            self.rear_n = n
            self.front_n = n

    def dequeue(self):
        n = self.front_n
        self.front_n = self.front_n.next_item
        if not self.front_n:
            self.rear_n = None
        return n.value

    def front(self):
        return self.front_n.value

    def rear(self):
        return self.rear_n.value

    def is_empty(self):
        return self.front_n is None

    def get_items(self):
        items = []
        prev = self.front_n
        while prev.next_item:
            items.append(prev.value)
            prev = prev.next_item
        items.append(prev.value)
        return items
