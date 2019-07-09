"""Simple python linked list implementation."""


class Node:
    """Node contains items value and reference to the next item in chain."""
    def __init__(self, value):
        self.value = value
        self.next_item = None

    def get_next(self):
        return self.next_item


class LinkedList:
    """Linked list holds reference to the first item in chain and it provides basic list manipulation methods."""
    def __init__(self):
        self.first = None

    def append(self, value):
        """Append new node with given value to the end of chain."""
        last = self.first
        prev = self.first
        while last:
            prev = last
            last = last.get_next()
        if prev:
            prev.next_item = Node(value)
        else:
            self.first = Node(value)

    def get_items(self):
        """Get list with all items in chain."""
        items = []
        item = self.first
        while item:
            items.append(item.value)
            item = item.get_next()
        return items
