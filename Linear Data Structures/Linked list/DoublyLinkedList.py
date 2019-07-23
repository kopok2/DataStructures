"""Simple python doubly linked list implementation."""


class DoubleNode:
    """Node contains items value and reference to the next item in chain."""
    def __init__(self, value, previous):
        self.value = value
        self.next_item = None
        self.previous_item = previous

    def get_next(self):
        return self.next_item


class DoublyLinkedList:
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
            prev.next_item = DoubleNode(value, prev)
        else:
            self.first = DoubleNode(value, None)

    def get_items(self):
        """Get list with all items in chain."""
        items = []
        item = self.first
        while item:
            items.append(item.value)
            item = item.get_next()
        return items

    def add_to_front(self, value):
        """Add new node to the front of the list."""
        second = self.first
        self.first = DoubleNode(value, None)
        self.first.next_item = second
        second.previous_item = self.first

    def insert_after(self, node, value):
        """Insert new node after given node."""
        last = self.first
        prev = self.first
        while last != node:
            prev = last
            last = last.get_next()
            if last is None:
                raise LookupError("Given node could not be found in linked list.")
        prev = last
        next_item = prev.get_next()
        prev.next_item = DoubleNode(value, prev)
        prev.next_item.next_item = next_item
        next_item.previous_item = prev.next_item

    def insert_at_index(self, index, value):
        """Insert new node at given index."""
        i = 0
        last = self.first
        try:
            while i != index - 1:
                last = last.get_next()
                i += 1
        except AttributeError:
            raise LookupError("Could not reach given index in linked list.")
        next_item = last.get_next()
        last.next_item = DoubleNode(value, last)
        last.next_item.next_item = next_item
        next_item.previous_item = last.next_item

    def delete_at_index(self, index):
        """Delete item with given index."""
        i = 0
        last = self.first
        prev = self.first
        try:
            while i != index:
                prev = last
                last = last.get_next()
                i += 1
        except AttributeError:
            raise LookupError("Could not reach given index in linked list.")
        next_item = last.get_next()
        prev.next_item = next_item
        next_item.previous_item = prev

    def __len__(self):
        """Calculate linked list length."""
        i = 0
        last = self.first
        while last:
            i += 1
            last = last.get_next()
        return i

    def swap_nodes(self, node_1, node_2):
        """Swap given nodes in linked list."""
        prev_1 = None
        next_1 = None
        prev_2 = None
        next_2 = None
        first_found = False
        second_found = False
        try:
            prev = None
            last = self.first
            while not (first_found and second_found):
                if last is node_1:
                    first_found = True
                    next_1 = last.get_next()
                    prev_1 = prev
                if last is node_2:
                    second_found = True
                    next_2 = last.get_next()
                    prev_2 = prev
                prev = last
                last = last.get_next()
            if prev_1:
                prev_1.next_item = node_2
                node_2.next_item = next_1
            else:
                self.first = node_2
                node_2.next_item = next_1
            if prev_2:
                prev_2.next_item = node_1
                node_1.next_item = next_2
            else:
                self.first = node_1
                node_1.next_item = next_2
        except AttributeError:
            LookupError("Could not found given nodes in linked list.")

    def reverse(self):
        """Reverse linked list."""
        prev = None
        curr = self.first
        while curr:
            next_item = curr.get_next()
            curr.next_item = prev
            if prev:
                prev.previous_item = curr
            prev = curr
            curr = next_item
        self.first = prev
