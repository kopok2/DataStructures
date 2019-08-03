# coding=utf-8
"""Linked List union and intersection using hash table."""

from HashTable import HashTable


def intersect(l1, l2):
    ht = HashTable()
    ht.store(l1)
    return [l for l in l2 if ht.get(l[0])]


def union(l1, l2):
    ht = HashTable()
    ht.store(l1)
    result = set(l1)
    for l in l2:
        if not ht.get(l[0]):
            result.add(l)
    return list(result)


if __name__ == "__main__":
    ar1 = [(x, x) for x in [1, 2, 3, 4, 5, 6]]
    ar2 = [(x, x) for x in [3, 4, 5, 6, 7, 8]]
    print(intersect(ar1, ar2))
    print(union(ar1, ar2))
