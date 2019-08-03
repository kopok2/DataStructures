# encoding-utf-8

import unittest
from random import randrange
from HashTable import HashTable


class TestHashTable(unittest.TestCase):
    def test_simple_hash_table(self):
        ht = HashTable()
        array = [(x, 10 - x) for x in range(10)]
        ht.store(array)
        for x in range(10):
            self.assertEqual(ht.get(x), 10 - x)

    def test_hash_table_perfomance(self):
        ht = HashTable()
        tl = 0
        for y in range(1, 2):
            keys = list(set([randrange(500000) for x in range(1, 500000)]))
            values = [randrange(500000) for x in range(1, y)][:len(keys)]
            tl += len(keys)
            array = [(key, value) for key, value in zip(keys, values)]
            ht.store(array)
            for el in array:
                self.assertEqual(ht.get(el[0]), el[1])
        print(tl)


if __name__ == "__main__":
    unittest.main()
