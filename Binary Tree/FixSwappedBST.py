# coding=utf-8
"""Fix Binary Search Tree with two swapped nodes."""

from BinarySearchTree import Node


def fix_tree(tree):
    traversal = tree.inorder_object_traversal()
    vals = [x.key for x in traversal]
    vals.sort()
    for x in range(len(vals)):
        traversal[x].key = vals[x]


if __name__ == "__main__":
    root1 = Node(50)
    root1.insert(30)
    root1.insert(20)
    root1.insert(40)
    root1.insert(70)
    root1.insert(60)
    root1.insert(80)
    tr = root1.inorder_object_traversal()

    tr[2].key, tr[5].key = tr[5].key, tr[2].key
    print(root1.inorder())
    fix_tree(root1)
    print(root1.inorder())
