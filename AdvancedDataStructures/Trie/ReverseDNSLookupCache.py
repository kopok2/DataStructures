# coding=utf-8
"""Reverse/Forward DNS Lookup Cache using Trie Python implementation."""


class DNSTrieNode:
    def __init__(self):
        self.is_end = False
        self.value = None
        self.children = {}


class DNSTrie:
    def __init__(self):
        self.root = DNSTrieNode()

    def add_domain(self, key, domain):
        position = self.root
        traversal = list(key)
        while traversal:
            adding = traversal.pop(0)
            if adding in position.children.keys():
                if len(traversal):
                    position = position.children[adding]
                else:
                    position.children[adding].value = domain
                    position.children[adding].is_end = True
            else:
                position.children[adding] = DNSTrieNode()
                if len(traversal):
                    position = position.children[adding]
                else:
                    position.children[adding].value = domain
                    position.children[adding].is_end = True

    def get_domain(self, key):
        position = self.root
        traversal = list(key)
        while traversal:
            searching = traversal.pop(0)
            if searching in position.children.keys():
                position = position.children[searching]
            else:
                return False
        if position.is_end:
            return position.value
        else:
            return False


if __name__ == "__main__":
    dnst = DNSTrie()
    for ip, domain in [("107.108.11.123", "www.samsung.com"), ("107.109.123.255", "www.samsung.net"), ("74.125.200.106", "www.google.in")]:
        dnst.add_domain(ip, domain)

    print(dnst.get_domain("107.109.123.255"))
    print(dnst.get_domain("107.109.123.250"))

    for domain, ip in [("107.108.11.123", "www.samsung.com"), ("107.109.123.255", "www.samsung.net"), ("74.125.200.106", "www.google.in")]:
        dnst.add_domain(ip, domain)

    print(dnst.get_domain("www.samsung.com"))
    print(dnst.get_domain("www.samsung.net"))
    print(dnst.get_domain("www.samsung.neto"))
