# coding=utf-8
"""AVL binary tree Python implementation."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        else:
            return node.height

    def balance(self):
        if not self.root:
            return 0
        else:
            return self.get_height(self.root.left_child) - self.get_height(self.root.right_child)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            current = self.root
            prev = current
            while current:
                prev = current
                if current.value < key:
                    current = current.right_child
                else:
                    current = current.left_child
            if prev.value < key:
                prev.right_child = Node(key)
            else:
                prev.left_child = Node(key)
        bl = self.balance()
        if bl > 1 and key < self.root.left_child.value:
            self.root = self.right_rotate(self.root)
        elif bl < - 1 and key > self.root.right_child.value:
            self.root = self.left_rotate(self.root)
        elif bl > 1 and key > self.root.left_child.value:
            self.root.left_child = self.left_rotate(self.root.left_child)
            self.root = self.right_rotate(self.root)
        elif bl < -1 and key < self.root.right_child.value:
            self.root.right_child = self.right_rotate(self.root.right_child)
            self.root = self.left_rotate(self.root)

    def left_rotate(self, node):
        y = node.right_child
        T2 = y.left_child
        y.left_child = node
        node.right_child = T2
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def right_rotate(self, node):
        y = node.left_child
        T3 = y.right_child
        y.right_child = node
        node.left_child = T3
        node.height = 1 + max(self.get_height(node.left_child), self.get_height(node.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        return y

    def visit(self):
        to_visit = [(self.root, -1)]
        while to_visit:
            visiting = to_visit.pop(0)
            if visiting[0]:
                print(visiting[0].value, visiting[1])
                to_visit.append((visiting[0].left_child, visiting[0].value))
                to_visit.append((visiting[0].right_child, visiting[0].value))


if __name__ == "__main__":
    avl_t = AVLTree()
    avl_t.insert(10)
    avl_t.insert(20)
    avl_t.insert(30)
    avl_t.insert(40)
    avl_t.insert(50)
    avl_t.insert(25)
    avl_t.visit()
