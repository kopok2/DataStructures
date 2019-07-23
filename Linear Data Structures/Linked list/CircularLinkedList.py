from LinkedList import LinkedList, Node


class CircularLinkedList(LinkedList):
    def append(self, value):
        """Append new node with given value to the end of chain."""
        last = self.first
        prev = self.first
        if self.first:
            while last.get_next() != self.first:
                prev = last
                last = last.get_next()
        if last:
            last.next_item = Node(value)
            last.next_item.next_item = self.first
        else:
            self.first = Node(value)
            self.first.next_item = self.first

    def get_items(self):
        """Get list with all items in chain."""
        items = [self.first.value]
        item = self.first
        item = item.get_next()
        while item != self.first:
            items.append(item.value)
            item = item.get_next()
        return items

    def add_to_front(self, value):
        """Add new node to the front of the list."""
        second = self.first
        self.first = Node(value)
        self.first.next_item = second
        item = second
        while item.get_next() != second:
            item = item.get_next()
        item.next_item = self.first

    def __len__(self):
        """Calculate linked list length."""
        i = 0
        last = self.first
        while last.next_item != self.first:
            i += 1
            last = last.get_next()
        return i + 1

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
