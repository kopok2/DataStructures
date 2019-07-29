# encoding-utf-8
"""Fibonacci heap Python implementation."""

from CircularDoublyLinkedList import CircularDoublyLinkedList


class FibNode:
    """Node of tree in Fibonacci Heap."""
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.child = []
        self.marked = False

    def rank(self):
        """Number of child of node."""
        return len(self.child)

    def n(self):
        """Get number of nodes in tree."""
        return sum([x.n() for x in self.child]) + 1

    def print_tree(self, ind=0, last=False):
        """Print tree structure."""
        if not last:
            print("    ├" * ind + ("────" if ind else "    ") + str(self.value))
        else:
            print("    │" * (ind - 1) + "    └" + ("────" if ind else "    ") + str(self.value))
        ind += 1
        for c in self.child:
            c.print_tree(ind=ind, last=c==self.child[-1])


class FibonacciHeap:
    """Fibonacci Heap implementation using circular doubly linked list."""
    def __init__(self, root_value):
        self.trees = CircularDoublyLinkedList(FibNode(root_value))
        self.minimum = self.trees.first
        self.marked_nodes = []

    def marks(self):
        """Get number of marked nodes in heap."""
        return len(self.marked_nodes)

    def trees_count(self):
        """Get number of trees in heap."""
        return len(self.trees.get_objects())

    def rank(self):
        """Get max rank of any node in heap."""
        return max([x.value.rank() for x in self.trees.get_objects()])

    def n(self):
        """Get number of nodes in heap."""
        return sum([x.value.n() for x in self.trees.get_objects()])

    def insert(self, value):
        """Lazily insert new value to heap.

        1. Create new singleton tree.
        2. Add to root list. Update min pointer if necessary.
        """
        new = FibNode(value)
        if value < self.minimum.value:
            self.minimum = new
        self.trees.insert_new_node(new)

    def link_trees(self, tree1, tree2):
        """Make larger root be a child of smaller root."""
        if tree1.value < tree2.value:
            tree1.child.append(tree2)
            tree2.parent = tree1
        else:
            tree2.child.append(tree1)
            tree1.parent = tree2

    def print_heap(self):
        """Print heap."""
        for i, t in enumerate(self.trees.get_objects()):
            print("Tree {0} | rank: {1} | n: {2}".format(i + 1, t.value.rank(), t.value.n()))
            t.value.print_tree()

    def delete_min(self):
        """Delete smallest node from heap.

        1. Delete min. Meld its children into root list. Update min.
        2. Consolidate trees so that no two roots have same rank.
        """
        for c in self.minimum.child:
            c.parent = None
            self.trees.insert_new_node(c)
        self.trees.delete_node_by_value(self.minimum)
        self.minimum = self.trees.first
        for n in self.trees.get_objects():
            if n.value.value < self.minimum.value.value:
                self.minimum = n
        same_ranks = [[] for x in range(self.rank() + 12)]
        while sum([1 if len(x) == 1 else 0 for x in same_ranks]) != self.trees_count():
            for t in self.trees.get_items():
                cc = t.rank()
                if t not in same_ranks[cc]:
                    same_ranks[cc].append(t)
                if len(same_ranks[cc]) > 1:
                    t1 = same_ranks[cc][0]
                    t2 = same_ranks[cc][1]
                    print("Linking {0} and {1}".format(t1.value, t2.value))

                    if t1.value < t2.value:
                        same_ranks[cc] = []
                        self.trees.delete_node_by_value(t2)
                        self.link_trees(t1, t2)

                        ncc = t1.rank()
                        same_ranks[ncc].append(t1)
                    else:
                        same_ranks[cc] = []
                        self.trees.delete_node_by_value(t1)
                        self.link_trees(t1, t2)

                        ncc = t2.rank()
                        same_ranks[ncc].append(t2)


if __name__ == "__main__":
    tree1 = FibNode(7)
    tree1.child.append(FibNode(30))

    tree2 = FibNode(24)
    tree2.child.append(FibNode(26))
    tree2.child.append(FibNode(46))
    tree2.child[0].child.append(FibNode(35))

    tree3 = FibNode(23)

    tree5 = FibNode(3)
    tree5.child.append(FibNode(18))
    tree5.child.append(FibNode(52))
    tree5.child.append(FibNode(41))
    tree5.child[0].child.append(FibNode(39))
    tree5.child[2].child.append(FibNode(44))

    fib_h = FibonacciHeap(17)
    fib_h.trees.insert_new_node(tree1)
    fib_h.trees.insert_new_node(tree2)
    fib_h.trees.insert_new_node(tree3)
    fib_h.trees.insert_new_node(tree5)
    fib_h.minimum = tree5

    basic_test = False

    if basic_test:
        fib_h.print_heap()
        print("n", fib_h.n())
        print("rank", fib_h.rank())
        print("trees", fib_h.trees_count())
        print("marks", fib_h.marks())

        fib_h.insert(21)
        fib_h.print_heap()

        fib_h.link_trees(tree5, tree2)
        fib_h.print_heap()
    else:
        fib_h.delete_min()
        fib_h.print_heap()

