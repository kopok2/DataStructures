# coding=utf-8
"""Skip list variable layer Python implementation."""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "v: {0} n: {1}".format(self.val, id(self.next))


class SkipNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.deeper = None

    def __repr__(self):
        return "v: {0} n: {1} d: {2}".format(self.val, id(self.next), id(self.deeper))


if __name__ == "__main__":
    nodes = [Node(x) for x in range(100)]
    nodes1 = [SkipNode(x * 10) for x in range(10)]
    nodes2 = [SkipNode(x * 50) for x in range(2)]
    for x in range(2):
        nodes2[x].deeper = nodes1[x * 5]
    for x in range(1):
        nodes2[x].next = nodes2[x + 1]
    for x in range(10):
        nodes1[x].deeper = nodes[x * 10]
    for x in range(9):
        nodes1[x].next = nodes1[x + 1]
    for x in range(99):
        nodes[x].next = nodes[x + 1]
    print(nodes, nodes1, nodes2)
    traversal = []
    find = 67
    current = nodes2[0]
    previous = None
    while current:
        if current.val >= find:
            break
        traversal.append(current.val)
        previous = current
        current = current.next

    current = previous.deeper
    while current:
        if current.val >= find:
            break
        traversal.append(current.val)
        previous = current
        current = current.next

    current = previous.deeper
    while current.val < find:
        if current.val >= find:
            break
        traversal.append(current.val)
        previous = current
        current = current.next
    traversal.append(current.val)
    print(current.val)
    print(traversal)
