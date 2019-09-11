# coding=utf-8
"""Splay tree Python implementation."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


def right_rotate(node):
    y = node.left_child
    node.left_child = y.right_child
    y.right_child = node
    return y


def left_rotate(node):
    y = node.right_child
    node.right_child = y.left_child
    y.left_child = node
    return y


def splay(node, key):
    if not node:
        return node
    if node.value == key:
        return node
    if node.value > key:
        if not node.left_child:
            return node
        elif node.left_child.value > key:
            node.left_child.left_child = splay(node.left_child.left_child, key)
            node = right_rotate(node)
        elif node.left_child.value < key:
            node.left_child.right_child = splay(node.left_child.right_child, key)
            if node.left_child.right_child:
                node.left_child = left_rotate(node.left_child)
        return node if not node.left_child else right_rotate(node)
    else:
        if not node.right_child:
            return node
        elif node.right_child.value > key:
            node.right_child.left_child = splay(node.right_child.left_child, key)
            if node.right_child.left_child:
                node.right_child = right_rotate(node.right_child)
        elif node.right_child.value < key:
            node.right_child.right_child = splay(node.right_child.right_child, key)
            node = left_rotate(node)
        return node if not node.right_child else left_rotate(node)


def search(root, key):
    return splay(root, key)


def preorder(root):
    if root:
        print(root.value)
        preorder(root.left_child)
        preorder(root.right_child)


def insert(root, key):
    current = root
    prev = current
    while current:
        prev = current
        if current.value < key:
            current = current.right_child
        elif current.value > key:
            current = current.left_child
        else:
            return splay(root, key)
    if prev.value < key:
        prev.right_child = Node(key)
    elif prev.value > key:
        prev.left_child = Node(key)
    return splay(root, key)


if __name__ == "__main__":
    root = Node(100)
    root.left_child = Node(50)
    root.right_child = Node(200)
    root.left_child.left_child = Node(40)
    root.left_child.left_child.left_child = Node(30)
    root.left_child.left_child.left_child.left_child = Node(20)
    root = search(root, 20)
    preorder(root)
    root = Node(100)
    root.left_child = Node(50)
    root.right_child = Node(200)
    root.left_child.left_child = Node(40)
    root.left_child.left_child.left_child = Node(30)
    root.left_child.left_child.left_child.left_child = Node(20)
    root = insert(root, 25)
    preorder(root)
