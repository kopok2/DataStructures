# coding=utf-8
"""Binary Search Tree Python implementation."""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.traversal = []
        self.object_traversal = []

    def insert(self, value):
        if value > self.key:
            if self.right:
                self.right.insert(value)
            else:
                self.right = Node(value)
        elif value < self.key:
            if self.left:
                self.left.insert(value)
            else:
                self.left = Node(value)

    def search(self, value):
        if value == self.key:
            return True
        elif value > self.key:
            if self.right:
                return self.right.search(value)
            else:
                return False
        else:
            if self.left:
                return self.left.search(value)
            else:
                return False

    def inorder(self, first=True, root=None):
        if first:
            self.traversal = []
            first = False
        if not root:
            root = self
        if self.left:
            self.left.inorder(first=first, root=root)
        root.traversal.append(self.key)
        if self.right:
            self.right.inorder(first=first, root=root)
        return self.traversal

    def inorder_object_traversal(self, first=True, root=None):
        if first:
            self.object_traversal = []
            first = False
        if not root:
            root = self
        if self.left:
            self.left.inorder_object_traversal(first=first, root=root)
        root.object_traversal.append(self)
        if self.right:
            self.right.inorder_object_traversal(first=first, root=root)
        return self.object_traversal

    def minimum_node(self):
        current = self
        while current.left:
            current = current.left
        return current

    def minimum_and_preceding_node(self):
        current = self
        previous = None
        while current.left:
            previous = current
            current = current.left
        return current, previous

    def find_pred_and_succ(self, value, prv=None):
        if value == self.key:
            return prv, self
        elif value > self.key:
            if self.right:
                return self.right.find_pred_and_succ(value, self)
        else:
            if self.left:
                return self.left.find_pred_and_succ(value, self)

    def kth_smallest(self, k):
        if k:
            if self.left:
                self.left.kth_smallest(k)
                k -= 1
        if k:
            k -= 1
            print(self.key)
        if k:
            if self.right:
                self.right.kth_smallest(k)
                k -= 1


if __name__ == "__main__":
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)
    print("100", root.search(100))
    print("70", root.search(70))
    print(root.inorder())
    print(root.minimum_node().key)
    print([x.key for x in root.minimum_and_preceding_node()])
    print([x.key for x in root.find_pred_and_succ(40)])
    root.kth_smallest(4)
