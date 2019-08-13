# coding=utf-8
"""Check whether graph is bipartite."""


def is_bipartite(edges):
    vertex = max(max([e[0] for e in edges]), max([e[1] for e in edges]))
    adj = [[] for x in range(vertex)]
    for e in edges:
        adj[e[0] - 1].append(e[1])
        adj[e[1] - 1].append(e[0])
    color = [None for x in range(vertex)]
    to_visit = [(1, 1)]
    while to_visit:
        visiting = to_visit.pop(0)
        if color[visiting[0] - 1] is None:
            color[visiting[0] - 1] = visiting[1]
            to_visit += [(x, -visiting[1]) for x in adj[visiting[0] - 1]]
        elif color[visiting[0] - 1] != visiting[1]:
            return False
    return True


if __name__ == "__main__":
    edges = [
        [1, 2],
        [5, 2],
        [4, 2],
        [1, 3],
        [4, 3]
    ]
    print(is_bipartite(edges))

    edges = [
        [1, 2],
        [5, 2],
        [4, 2],
        [1, 3],
        [4, 3],
        [3, 2]
    ]
    print(is_bipartite(edges))
