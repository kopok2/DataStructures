# coding=utf-8
"""Given list of tickets find itinerary."""

from HashTable import HashTable


def find_itinerary(tickets):
    ht = HashTable()
    ht.store([(x[1], x[0]) for x in tickets])
    for t in tickets:
        if not ht.get(t[0]):
            start = t[0]
            break
    ht.store(tickets)
    result = []
    while ht.get(start):
        result.append((start, ht.get(start)))
        start = ht.get(start)
    return result


if __name__ == "__main__":
    tickets = [(1, 2), (2, 3), (3, 4), (5, 6), (4, 5)]
    print(find_itinerary(tickets))
