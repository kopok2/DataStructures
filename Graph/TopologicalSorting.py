# coding=utf-8
"""Topological sorting for directed acyclic graph (DAG)."""


def topological_sorting(adjacency):
    vertices = len(adjacency)
    visited = [False for e in range(vertices)]
    stack = []
    for x in range(vertices):
        if not visited[x]:
            visited[x] = True
            to_visit = adjacency[x]
            rev_stack = [x]
            while to_visit:
                visiting = to_visit.pop(0)
                if not visited[visiting]:
                    rev_stack.append(visiting)
                    visited[visiting] = True
                    to_visit += adjacency[visiting]
            stack += rev_stack[::-1]
    return stack


if __name__ == "__main__":
    adj = [[], [], [3], [1], [0, 1], [2, 0]]
    print(topological_sorting(adj))
