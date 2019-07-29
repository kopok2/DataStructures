# encoding-utf-8
"""Hash table with separate chaining Python implementation."""


class HashTable:
    def __init__(self):
        self.size = 0
        self.table = []

    def hash_function(self, key):
        return key % self.size

    def store(self, array):
        self.size = len(array)
        self.table = [[] for x in range(self.size)]
        for key in array:
            self.table[self.hash_function(key[0])].append(key)

    def get(self, key):
        chain = self.table[self.hash_function(key)]
        for x in chain:
            if x[0] == key:
                return x[1]


if __name__ == "__main__":
    ht = HashTable()
    ht.store([(x ** 2, str(x ** 2)) for x in range(100)])
    print(ht.table)
    print(ht.get(100))
