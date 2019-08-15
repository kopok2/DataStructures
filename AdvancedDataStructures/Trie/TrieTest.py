# coding=utf-8
"""Trie Python implementation unit tests."""

import unittest
import random
from Trie import Trie


class TrieTest(unittest.TestCase):
    def test_adding(self):
        trie = Trie()
        trie.add_key("semir")
        trie.add_key("semiramida")

    def test_searching(self):
        trie = Trie()
        trie.add_key("semir")
        self.assertTrue(trie.in_tree("semir"))
        self.assertFalse(trie.in_tree("semiramida"))
        trie.add_key("semiramida")
        self.assertTrue(trie.in_tree("semiramida"))

    def test_efficiency(self):
        trie = Trie()
        alphabet = "abcdefghijklmnouprstuvwxyz"
        words = []
        for x in range(1000):
            word = "".join([alphabet[random.randrange(len(alphabet))] for x in range(1000)])
            words.append(word)
        for x in range(500):
            trie.add_key(words[x])
        for x in range(500):
            self.assertTrue(trie.in_tree(words[x]))
        for x in range(500, 1000):
            if words[x] not in words[:500]:
                self.assertFalse(trie.in_tree(words[x]))


if __name__ == "__main__":
    unittest.main()
