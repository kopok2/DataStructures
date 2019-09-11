# coding=utf-8
"""Two dimensional binary indexed tree Python implementation."""


from BinaryIndexedTree import BinaryIndexedTree


class _2DBinaryIndexedTree:
    def __init__(self, matrix):
        self.matrix = matrix
        self.bits = [BinaryIndexedTree(row) for row in matrix]

    def get_sub_sum(self, x1, y1, x2, y2):
        result = 0
        for y in range(y1, y2 + 1):
            result += self.bits[len(self.matrix) - y - 1].get_sum(x2) - self.bits[len(self.matrix) - y - 1].get_sum(x1 - 1)
        return result


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 3, 8, 1],
              [4, 6, 7, 5],
              [2, 4, 8, 9]]
    _2dbit = _2DBinaryIndexedTree(matrix)
    print(_2dbit.get_sub_sum(1, 1, 3, 2))
    print(_2dbit.get_sub_sum(2, 3, 3, 3))
    print(_2dbit.get_sub_sum(1, 1, 1, 1))
