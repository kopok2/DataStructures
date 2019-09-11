# coding=utf-8
"""LRU Cache Python implementation."""

from collections import deque


class LRUObject:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.cache = deque(maxlen=max_size)
        self.links = {}

    def cache_data(self, key, data):
        cache_object = LRUObject(key, data)
        if len(self.cache) >= self.max_size:
            removing = self.cache.popleft()
            del self.links[removing.key]
        self.cache.append(cache_object)
        self.links[key] = cache_object

    def refer(self, key):
        if key in self.links:
            self.cache.remove(self.cache[self.cache.index(self.links[key])])
            self.cache.append(self.links[key])
            return self.links[key]
        else:
            return None


if __name__ == "__main__":
    lru_cache = LRUCache(3)
    lru_cache.cache_data(1, 12)
    lru_cache.cache_data(2, 13)
    lru_cache.cache_data(3, 14)
    lru_cache.cache_data(4, 15)
    print(lru_cache.refer(2))
    print(lru_cache.refer(4))
    print(lru_cache.refer(1))
