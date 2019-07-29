# encoding-utf-8
"""Circular Doubly Linked List Python implementation."""


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class CircularDoublyLinkedList:
    def __init__(self, root_value):
        self.first = DoubleNode(root_value)
        self.first.next = self.first
        self.first.previous = self.first

    def insert_new_node(self, value):
        new = DoubleNode(value)
        last = self.first.previous
        self.first.previous = new
        last.next = new
        new.previous = last
        new.next = self.first

    def delete_node(self, node):
        current = self.first
        while current != node:
            current = current.next
        pre = current.previous
        nex = current.next
        pre.next = nex
        nex.previous = pre
        if node == self.first:
            self.first = nex

    def delete_node_by_value(self, value):
        current = self.first
        while current.value != value:
            current = current.next
        pre = current.previous
        nex = current.next
        pre.next = nex
        nex.previous = pre
        if value == self.first.value:
            self.first = nex

    def merge_cdlls(self, cdll):
        pre1 = self.first.previous
        nex2 = cdll.first.next
        self.first.previous = cdll.first
        cdll.first.next = self.first
        pre1.next = nex2
        nex2.previous = pre1

    def get_items(self):
        items = [self.first.value]
        current = self.first.next
        while current != self.first:
            items.append(current.value)
            current = current.next
        return items

    def get_objects(self):
        objects = [self.first]
        current = self.first.next
        while current != self.first:
            objects.append(current)
            current = current.next
        return objects
