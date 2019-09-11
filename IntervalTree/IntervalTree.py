# coding=utf-8
"""Interval Tree Python implementation."""


class Node:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.max = high
        self.left = None
        self.right = None


def insert(root, low, high):
    if not root:
        return Node(low, high)
    l = root.low
    if low < l:
        root.left = insert(root.left, low, high)
    else:
        root.right = insert(root.right, low, high)
    if root.max < high:
        root.max = high
    return root


def overlaps(l1, h1, l2, h2):
    return l1 <= h2 and l2 <= h1


def overlap_search(root, low, high):
    if not root:
        return None
    if overlaps(root.low, root.high, low, high):
        return root.low, root.high
    if root.left:
        if root.left.max >= low:
            return overlap_search(root.left, low, high)
    return overlap_search(root.right, i)


def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print(root.low, root.high, root.max)
    inorder(root.right)


if __name__ == "__main__":
    intervals = [(15, 20), (10, 30), (17, 19), (5, 20), (12, 15), (30, 40)]
    root = None
    for inter in intervals:
        root = insert(root, *inter)
    inorder(root)
    x = (6, 7)
    print(overlap_search(root, *x))
