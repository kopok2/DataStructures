"""Binary Tree Python implementation."""


class BinaryNode:
    def __init__(self, value, level):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.level = level

    def add_left_child(self, value):
        self.left_child = BinaryNode(value, self.level + 1)

    def add_right_child(self, value):
        self.right_child = BinaryNode(value, self.level + 1)


class BinaryTree:
    def __init__(self):
        self.root = BinaryNode(1, 1)

    def __str__(self):
        levels = 1
        nodes = [[self.root]]
        to_visit = [self.root.left_child, self.root.right_child]
        while to_visit:
            visiting = to_visit.pop(0)
            if visiting:
                if visiting.level > levels:
                    levels = visiting.level
                    nodes.append([])
                nodes[visiting.level - 1].append(visiting)
                to_visit.append(visiting.left_child)
                to_visit.append(visiting.right_child)
        result = ""
        for l in nodes:
            result += "{0}\n".format(" ".join([str(x.value) for x in l]))
        return result

    def breadth_first_traversal(self):
        traversal = []
        to_visit = [self.root]
        while to_visit:
            visiting = to_visit.pop(0)
            if visiting:
                traversal.append(visiting)
                to_visit.append(visiting.left_child)
                to_visit.append(visiting.right_child)
        return traversal

    def height(self):
        return max([x.level for x in self.breadth_first_traversal()])

    def left_subtree(self):
        l_sbtree = BinaryTree()
        l_sbtree.root = self.root.left_child
        return l_sbtree

    def right_subtree(self):
        r_sbtree = BinaryTree()
        r_sbtree.root = self.root.right_child
        return r_sbtree

    def diameter(self):
        if self.root.right_child and self.root.right_child:
            return max(self.left_subtree().diameter(), self.right_subtree().diameter(), -1 + self.right_subtree().height() + self.left_subtree().height())
        else:
            return 1


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root.add_left_child(2)
    bt.root.add_right_child(3)
    bt.root.left_child.add_left_child(4)
    bt.root.left_child.add_right_child(5)
    print(bt)
    print(" ".join([str(x.value) for x in bt.breadth_first_traversal()]))
    print(bt.height())
    print(bt.diameter())
