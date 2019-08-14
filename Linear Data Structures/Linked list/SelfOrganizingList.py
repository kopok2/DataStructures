# coding=utf-8
"""Self organizing list (transpose method) Python implementation."""


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class SelfOrganizingList:
    def __init__(self):
        self.first = None

    def add_node(self, key, val):
        if self.first:
            prev = None
            current = self.first
            while current:
                prev = current
                current = current.next
            prev.next = Node(key, val)
        else:
            self.first = Node(key, val)

    def get_node(self, key):
        prev = None
        prevprev = None
        current = self.first
        while current.key != key:
            prevprev = prev
            prev = current
            current = current.next
        if prevprev:
            prevprev.next = current
            prev.next = current.next
            current.next = prev
        return current.val

    def get_items(self):
        current = self.first
        items = []
        while current:
            items.append(current.val)
            current = current.next
        return items


if __name__ == "__main__":
    sol = SelfOrganizingList()
    for x in range(100):
        sol.add_node(x, x)
    print(sol.get_items())
    for x in range(100):
        sol.get_node(x % 15)
    print(sol.get_items())
    for x in range(100):
        sol.get_node(12)
    print(sol.get_items())
