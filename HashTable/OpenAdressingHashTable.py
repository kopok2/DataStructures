# encoding-utf-8
"""Open adressing hash table Python implementation."""


class OAHashTable:
    def __init__(self):
        self.size = 0
        self.table = []

    def hash_function(self, key):
        return key % self.size

    def store(self, array):
        self.size = len(array)
        self.table = [None for x in range(self.size * 2)]
        for el in array:
            x = self.hash_function(el[0])
            while self.table[x]:
                x += 1
            self.table[x] = el

    def get(self, key):
        x = self.hash_function(key)
        while self.table[x]:
            if self.table[x][0] == key:
                return self.table[x][1]
            else:
                x += 1
