# coding=utf-8
"""Cartesian Tree Python implementation."""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)


def build_util(root, arr, parent, left_child, right_child):
    if root == -1:
        return None
    tmp = Node(arr[root])
    tmp.left = build_util(left_child[root], arr, parent, left_child, right_child)
    tmp.right = build_util(right_child[root], arr, parent, left_child, right_child)
    return tmp


def build_tree(arr):
    n = len(arr)
    parent = [0] * n
    left_child = [0] * n
    right_child = [0] * n
    root = 0
    for i in range(1, n):
        last = i - 1
        right_child[i] = -1
        while arr[last] <= arr[i] and last != root:
            last = parent[last]
        if arr[last] <= arr[i]:
            parent[root] = i
            left_child[i] = root
            root = i
        elif right_child[last] == -1:
            right_child[last] = i
            parent[i] = last
            left_child[i] = -1
        else:
            parent[right_child[last]] = i
            left_child[i] = right_child[last]
            right_child[last] = i
            parent[i] = last
    parent[root] = -1
    print(root, arr, parent, left_child, right_child)
    left_child[0] = -1
    right_child[0] = -1
    return build_util(root, arr, parent, left_child, right_child)


if __name__ == "__main__":
    arr = [5, 10, 40, 30, 28]
    root = build_tree(arr)
    inorder(root)
