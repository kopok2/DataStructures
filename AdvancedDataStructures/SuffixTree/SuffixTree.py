# coding=utf-8
"""Suffix tree Python implementation."""


class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}


class STrie:
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


class SuffixTree:
    def __init__(self, string):
        self.str = string
        self.tree = STrie()
        for x in range(1, len(string) + 1):
            self.tree.add_key(string[len(string) - x:])

    def has_pattern(self, pattern):
        return self.tree.in_tree(pattern)


if __name__ == "__main__":
    st = SuffixTree("banana")
    print(st.has_pattern("banan"))
    print(st.has_pattern("bananan"))
