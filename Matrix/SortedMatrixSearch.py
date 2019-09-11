# coding=utf-8
"""Search in matrix sorted column wise and row wise."""


def search(matrix, key):
    y = 0
    x = len(matrix[0]) - 1
    while x >= 0 and y < len(matrix):
        if key > matrix[y][x]:
            y += 1
        elif key < matrix[y][x]:
            x -= 1
        else:
            return y, x
    return None


if __name__ == '__main__':
    matrix = [[10, 20, 30, 40],
              [15, 25, 35, 45],
              [27, 29, 37, 48],
              [32, 33, 39, 50]]
    print(search(matrix, 29))
    print(search(matrix, 100))
    print(search(matrix, 33))
    print(search(matrix, 10))
