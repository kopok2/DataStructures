# coding=utf-8
"""Given array find pair with sum x."""

from HashTable import HashTable


def find_pair(array, x):
    ht = HashTable()
    ht.store(array)
    result = []
    for i in array:
        if ht.get(x - i[1]):
            result.append((i[1], x - i[1]))
    return result


if __name__ == "__main__":
    array = [(x, x) for x in [1, 4, 45, 6, 10, 8]]
    x = 16
    print(find_pair(array, x))
