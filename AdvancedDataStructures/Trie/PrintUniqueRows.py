# coding=utf-8
"""Print unique rows in table.
Trie data structure Python solution.
"""


from Trie import Trie


def print_unique(table):
    t = Trie()
    for row in table:
        if not t.in_tree(row):
            print(row)
            t.add_key(row)


if __name__ == "__main__":
    table = [
        "semir",
        "dahak",
        "semir",
        "semiriana",
        "sem"
    ]
    print_unique(table)
