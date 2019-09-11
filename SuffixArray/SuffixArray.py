# coding=utf-8
"""Suffix Array Python implementation."""


class Suffix:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        if self.value[0] == other.value[0]:
            if len(self.value) > 1 and len(other.value) > 1:
                return self.value[1] > other.value[1]
            elif len(self.value) > 1:
                return True
            else:
                return False
        else:
            return self.value[0] > other.value[0]


class SuffixArray:
    def __init__(self, word):
        self.words = [Suffix(word[x:]) for x in range(len(word))]
        self.words.sort(reverse=True)


if __name__ == "__main__":
    sa = SuffixArray("banana")
    for w in sa.words:
        print(w.value)
