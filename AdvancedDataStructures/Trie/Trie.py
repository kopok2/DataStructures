# coding=utf-8
"""Trie Python implementation."""


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_key(self, key):
        position = self.root
        traversal = list(key)
        while traversal:
            adding = traversal.pop(0)
            if adding in position.children.keys():
                if len(traversal):
                    position = position.children[adding]
                else:
                    position.children[adding].is_end = True
            else:
                position.children[adding] = TrieNode()
                if len(traversal):
                    position = position.children[adding]
                else:
                    position.children[adding].is_end = True

    def in_tree(self, key):
        position = self.root
        traversal = list(key)
        while traversal:
            searching = traversal.pop(0)
            if searching in position.children.keys():
                position = position.children[searching]
            else:
                return False
        return True
