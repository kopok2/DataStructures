# coding=utf-8
"""Treap (Randomized Binary Search Tree) Python implementation."""

import random


class Node:
    def __init__(self, value):
        self.value = value
        self.priority = random.randrange(1, 100)
        self.left = None
        self.right = None


def right_rotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    return x


def left_rotate(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    return y


def search(root, key):
    if not root:
        return root
    elif root.value == key:
        return root
    elif root.value < key:
        return search(root.right, key)
    else:
        return search(root.left, key)


def insert(root, key):
    if not root:
        return Node(key)
    elif key <= root.value:
        root.left = insert(root.left, key)
        if root.left.priority > root.priority:
            root = right_rotate(root)
    else:
        root.right = insert(root.right, key)
        if root.right.priority > root.priority:
            root = left_rotate(root)
    return root


def delete_node(root, key):
    if not root:
        return root
    elif key < root.value:
        root.left = delete_node(root.left, key)
    elif key > root.value:
        root.right = delete_node(root.right, key)
    elif not root.left:
        root = root.right
    elif not root.right:
        root = root.left
    elif root.left.priority < root.right.priority:
        root = left_rotate(root)
        root.left = delete_node(root.left, key)
    else:
        root = right_rotate(root)
        root.right = delete_node(root.right, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, root.priority)
        if root.left:
            print("Left child: {0}".format(root.left.value))
        if root.right:
            print("Right child: {0}".format(root.right.value))
        inorder(root.right)


if __name__ == "__main__":
    root = insert(None, 50)
    print(root)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 80)
    root = insert(root, 60)
    inorder(root)
    root = delete_node(root, 20)
    inorder(root)
    root = delete_node(root, 30)
    inorder(root)
    root = delete_node(root, 50)
    inorder(root)
    res = search(root, 50)
    print("YES" if res else "NO")
