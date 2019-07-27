# coding=utf-8
"""Check whether there is a pair of numbers in Binary Search Tree with sum = x."""

from BinarySearchTree import Node


def pair_sum_in_array(array, x):
    """Check whether there is a pair of numbers in sorted array with sum = x."""
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] + array[r] == x:
            return True
        elif array[l] + array[r] < x:
            l += 1
        else:
            r -= 1
    return False


def sum_in_bst(tree, x):
    """Find whether there is a pair of numbers in Binary Search Tree with sum = x."""
    return pair_sum_in_array(tree.inorder(), x)


if __name__ == "__main__":
    root1 = Node(50)
    root1.insert(30)
    root1.insert(20)
    root1.insert(40)
    root1.insert(70)
    root1.insert(60)
    root1.insert(80)
    print(sum_in_bst(root1, 50))
    print(sum_in_bst(root1, 150))
    print(sum_in_bst(root1, 250))
