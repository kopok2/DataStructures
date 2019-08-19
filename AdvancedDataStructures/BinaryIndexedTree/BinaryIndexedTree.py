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
            self.bit[i] += v
            i += i & (-i)

    def get_sum(self, i):
        s = 0
        i = i + 1
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s

    def update_range(self, l, r, val):
        for i in range(l, r + 1):
            self.update_bit(i, val)

    def get_element(self, i):
        return self.get_sum(i) - self.get_sum(i - 1)

    def get_range_sum(self, l, r):
        return self.get_sum(r - 1) - self.get_sum(l - 1)


if __name__ == "__main__":
    array = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    bit = BinaryIndexedTree(array)
    for x in range(len(array)):
        print(sum(array[:x + 1]), bit.get_sum(x))
    print([bit.get_element(x) for x in range(len(array))], array)
    print(bit.get_range_sum(0, len(array)), sum(array))
    print(bit.get_range_sum(0, len(array) // 2), sum(array[:len(array) // 2]))
    bit.update_range(0, len(array) - 1, 1)
    print([bit.get_element(x) for x in range(len(array))], array)

