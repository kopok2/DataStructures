# coding=utf-8
"""Sparse set Python implementation."""


class SparseSet:
    def __init__(self, max_value, capacity):
        self.max_value = max_value
        self.capacity = capacity
        self.sparse = [-1] * (max_value + 1)
        self.dense = [-1] * capacity
        self.n = 0

    def clear(self):
        """Clear set."""
        self.n = 0

    def search(self, x):
        """Determine whether x is in set."""
        result = -1
        if x < self.max_value:
            if self.sparse[x] < self.n and self.dense[self.sparse[x]] == x:
                result = self.sparse[x]
        return result

    def add(self, x):
        """Add x to set."""
        if x < self.max_value and self.n < self.capacity and self.search(x) == -1:
            self.dense[self.n] = x
            self.sparse[x] = self.n
            self.n += 1

    def remove(self, x):
        """Remove x from set."""
        if self.search(x) != -1:
            self.dense[self.sparse[x]], self.sparse[self.dense[self.n - 1]] = self.dense[self.n - 1], self.sparse[x]
            self.n -= 1

    def __str__(self):
        return str(self.dense)

    def intersection(self, other):
        """Find common elements of both sets."""
        i_cap = min(self.n, other.n)
        i_max_val = max(self.max_value, other.max_value)
        result = SparseSet(i_max_val, i_cap)
        if self.n < other.n:
            for i in range(self.n):
                if other.search(self.dense[i]) != -1:
                    result.add(self.dense[i])
        else:
            for i in range(other.n):
                if self.search(other.dense[i]) != -1:
                    result.add(other.dense[i])
        return result

    def union(self, other):
        """Find elements present in any of both sets."""
        u_cap = self.n + other.n
        u_max_val = max(self.max_value, other.max_value)
        result = SparseSet(u_max_val, u_cap)
        for i in range(self.n):
            result.add(self.dense[i])
        for i in range(other.n):
            result.add(other.dense[i])
        return result


if __name__ == "__main__":
    ss = SparseSet(100, 5)
    ss.add(5)
    ss.add(3)
    ss.add(9)
    ss.add(10)
    print(ss)
    print(ss.search(3))
    print(ss.search(21))
    ss.remove(9)
    print(ss)
    ss2 = SparseSet(1000, 6)
    ss2.add(4)
    ss2.add(3)
    ss2.add(7)
    ss2.add(200)
    print(ss2)
    print(ss2.intersection(ss))
    print(ss2.union(ss))
