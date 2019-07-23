"""Deque Python implementation module."""


class Deque:
    def __init__(self):
        self.items = []

    def insert_front(self, value):
        self.items.insert(0, value)

    def insert_last(self, value):
        self.items.append(value)

    def delete_front(self):
        self.items.pop(0)

    def delete_last(self):
        self.items.pop(-1)

    def get_front(self):
        return self.items[0]

    def get_last(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def get_items(self):
        return self.items
