# coding=utf-8
"""Longest prefix matching using trie Python implementation."""


from Trie import Trie


def lmp(in_str, dictionary):
    t = Trie()
    for word in dictionary:
        t.add_key(word)
    position = t.root
    traversal = list(in_str)
    match = ''
    found = ''
    while traversal:
        searching = traversal.pop(0)
        if searching in position.children.keys():
            match += searching
            if position.is_end:
                found = match
            position = position.children[searching]
        else:
            return found
    if position.is_end:
        found = match
    return found


if __name__ == "__main__":
    dictionary = ["are", "area", "base", "cat", "cater", "basement"]
    words = ["caterer", "basement", "are", "arex", "basemexz", "xyz"]
    for w in words:
        print(w, lmp(w, dictionary))
