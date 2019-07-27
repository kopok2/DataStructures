# coding=utf-8
"""Given two Binary Search Trees, print the elements of both BSTs in sorted form."""

from BinarySearchTree import Node


def merge_bst(bst1, bst2):
    merge = []
    s1 = bst1.inorder().copy()
    s2 = bst2.inorder().copy()
    while s1 and s2:
        if s1[0] <= s2[0]:
            merge.append(s1.pop(0))
        else:
            merge.append(s2.pop(0))
    new_root = Node(merge.pop(0))
    while merge:
        new_root.insert(merge.pop(0))
    return new_root


if __name__ == "__main__":
    root1 = Node(50)
    root1.insert(30)
    root1.insert(20)
    root1.insert(40)
    root1.insert(70)
    root1.insert(60)
    root1.insert(80)
    root2 = Node(150)
    root2.insert(130)
    root2.insert(12)
    root2.insert(30)
    root2.insert(10)
    root2.insert(10)
    root2.insert(10)
    print(merge_bst(root1, root2).inorder())
