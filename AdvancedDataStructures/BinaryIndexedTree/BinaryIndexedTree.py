# coding=utf-8
"""Binary indexed tree(Fenwick tree) Python implementation."""


class BinaryIndexedTree:
    def __init__(self, array):
        self.array = array
        self.bit = [0] * (len(array) + 1)
        for i in range(len(array)):
            self.update_bit(i, self.array[i])

    def update_bit(self, i, v):
        i += 1
        while i <= len(self.array):
            self.bit [i] += v
            i += i & (-i)

    def get_sum(self, i):
        s = 0
        i = i + 1
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s


if __name__ == "__main__":
    array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = BinaryIndexedTree(array)
    for x in range(len(array)):
        print(sum(array[:x + 1]), bit.get_sum(x))
