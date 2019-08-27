# coding=utf-8
"""B-Tree Python implementation."""


class Node:
    def __init__(self, t, is_leaf):
        self.keys = [0] * (2 * t - 1)
        self.t = t
        self.child = [None] * (2 * t)
        self.is_leaf = is_leaf
        self.n = 0

    def traverse(self):
        i = 0
        while i < self.n:
            if not self.is_leaf:
                self.child[i].traverse()
            print(self.keys[i])
            i += 1
        if not self.is_leaf:
            self.child[i].traverse()

    def search(self, key):
        i = 0
        while i < self.n and key > self.keys[i]:
            i += 1
        if self.keys[i] == key:
            return self
        elif self.is_leaf:
            return None
        else:
            return self.child[i].search(key)

    def insert_non_full(self, key):
        i = self.n - 1
        if self.is_leaf:
            while i >= 0 and self.keys[i] > key:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = key
            self.n += 1
        else:
            while i >= 0 and self.keys[i] > key:
                i -= 1
            if self.child[i + 1].n == 2 * self.t - 1:
                self.split_child(i + 1, self.child[i + 1])
                if self.keys[i + 1] < key:
                    i += 1
            self.child[i + 1].insert_non_full(key)

    def split_child(self, i, y):
        z = Node(y.t, y.is_leaf)
        z.n = self.t - 1
        for j in range(self.t - 1):
            z.keys[j] = y.keys[j + self.t]
        if not y.is_leaf:
            for j in range(self.t):
                z.child[j] = y.child[j + self.t]
        y.n = self.t - 1
        for j in range(self.n, i, -1):
            self.child[j + 1] = self.child[j]
        self.child[i + 1] = z
        for j in range(self.n - 1, i, -1):
            self.keys[j + 1] = self.keys[j]
        self.keys[i] = y.keys[self.t - 1]
        self.n += 1

    def find_key(self, key):
        idx = 0
        while idx < self.n and self.keys[idx] < key:
            idx += 1
        return idx

    def remove(self, key):
        idx = self.find_key(key)
        if idx < self.n  and self.keys[idx] == key:
            if self.is_leaf:
                self.remove_from_leaf(idx)
            else:
                self.remove_from_non_leaf(idx)
        else:
            if self.is_leaf:
                print("Key not in tree.")
                return None
            flag = idx == self.n
            if self.child[idx].n < self.t:
                self.fill(idx)
            if flag and idx > self.n:
                self.child[idx - 1].remove(key)
            else:
                self.child[idx].remove(key)

    def remove_from_leaf(self, idx):
        for i in range(idx + 1, self.n):
            self.keys[i - 1] = self.keys[i]
        self.n -= 1

    def remove_from_non_leaf(self, idx):
        k = self.keys[idx]
        if self.child[idx].n >= self.t:
            pred = self.get_pred(idx)
            self.keys[idx] = pred
            self.child[idx].remove(pred)
        elif self.child[idx + 1].n >= self.t:
            succ = self.get_succ(idx)
            self.keys[idx] = succ
            self.child[idx + 1].remove(succ)
        else:
            self.merge(idx)
            self.child[idx].remove(k)

    def get_pred(self, idx):
        cur = self.child[idx + 1]
        while not cur.is_leaf:
            cur = cur.child[0]
        return cur.keys[0]

    def get_succ(self, idx):
        cur = self.child[idx + 1]
        while not cur.is_leaf:
            cur = cur.child[0]
        return cur.keys[0]

    def fill(self, idx):
        if idx:
            if self.child[idx - 1].n >= self.t:
                self.borrow_from_prev(idx)
            return None
        if idx != self.n and self.child[idx + 1].n >= self.t:
            self.borrow_from_next(idx)
        else:
            if idx != self.n:
                self.merge(idx)
            else:
                self.merge(idx - 1)

    def borrow_from_prev(self, idx):
        child = self.child[idx]
        sibling = self.child[idx - 1]
        for i in range(child.n - 1, -1, -1):
            child.keys[i + 1] = child.keys[i]
        if not child.is_leaf:
            for i in range(child.n, -1, -1):
                child.child[i + 1] = child.child[i]
        child.keys[0] = self.keys[idx - 1]
        if not child.is_leaf:
            child.child[0] = sibling.child[sibling.n]
        self.keys[idx - 1] = sibling.keys[sibling.n - 1]
        child.n += 1
        sibling.n -= 1

    def borrow_from_next(self, idx):
        child = self.child[idx]
        sibling = self.child[idx + 1]
        child.keys[child.n] = self.keys[idx]
        if not child.is_leaf:
            child.child[child.n + 1] = sibling.chlid[0]
        self.keys[idx] = sibling.keys[0]
        for i in range(1, sibling.n):
            sibling.keys[i - 1] = sibling.keys[i]
        if not sibling.is_leaf:
            for i in range(1, sibling.n + 1):
                sibling.child[i - 1] = sibling.child[i]
        child.n += 1
        sibling.n -= 1

    def merge(self, idx):
        child = self.child[idx]
        sibling = self.child[idx + 1]
        child.keys[self.t - 1] = self.keys[idx]
        for i in range(sibling.n):
            child.keys[i + self.t] = sibling.keys[i]
        if not child.is_leaf:
            for i in range(sibling.n + 1):
                child.child[i + self.t] = sibling.child[i]
        for i in range(idx + 1, self.n):
            self.keys[i - 1] = self.keys[i]
        for i in range(idx + 2, self.n + 1):
            self.child[i - 1] = self.child[i]
        child.n += sibling.n + 1
        self.n -= 1




class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def traverse(self):
        if self.root:
            self.root.traverse()

    def search(self, key):
        return None if not self.root else self.root.search(key)

    def insert(self, key):
        if not self.root:
            self.root = Node(self.t, True)
            self.root.keys[0] = key
            self.root.n = 1
        else:
            if self.root.n == 2 * self.t - 1:
                s = Node(self.t, False)
                s.child[0] = self.root
                s.split_child(0, self.root)
                i = 0
                if s.keys[0] < key:
                    i += 1
                s.child[i].insert_non_full(key)
                self.root = s
            else:
                self.root.insert_non_full(key)

    def remove(self, key):
        if not self.root:
            print("The tree is empty.")
        else:
            self.root.remove(key)
            if not self.root.n:
                if self.root.is_leaf:
                    self.root = None
                else:
                    self.root = self.root.child[0]


if __name__ == "__main__":
    bt = BTree(3)
    bt.insert(10)
    bt.insert(20)
    bt.insert(5)
    bt.insert(6)
    bt.insert(12)
    bt.insert(30)
    bt.insert(7)
    bt.insert(17)
    bt.traverse()
    print(bt.search(6))
    print(bt.search(15))

    t = BTree(3)
    t.insert(1)
    t.insert(3)
    t.insert(7)
    t.insert(10)
    t.insert(11)
    t.insert(13)
    t.insert(14)
    t.insert(15)
    t.insert(18)
    t.insert(16)
    t.insert(19)
    t.insert(24)
    t.insert(25)
    t.insert(26)
    t.insert(21)
    t.insert(4)
    t.insert(5)
    t.insert(20)
    t.insert(22)
    t.insert(2)
    t.insert(17)
    t.insert(12)
    t.insert(6)

    t.traverse()
    t.remove(6)
    t.traverse()
    t.remove(13)
    t.traverse()
    t.remove(7)
    t.traverse()
    t.remove(4)
    t.traverse()
    t.remove(2)
    t.traverse()
    t.remove(16)
    t.traverse()
