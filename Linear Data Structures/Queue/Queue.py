"""Simple queue Python implementation module."""


class Queue:
    def __init__(self):
        self.items = []

    def get_items(self):
        return self.items

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def front(self):
        return self.items[0]

    def rear(self):
        return self.items[-1]
