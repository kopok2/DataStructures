# coding=utf-8
"""Adjacency list graph Python implementation."""


class Graph:
    def __init__(self, edges, vertex_count, directed=False):
        """Creates graph from list of egdes.

        Args:
            edges: list of tuples (from, to, weight).
            vertex_count: number of vertices in graph.
        """
        self.edges = edges
        self.vertex_count = vertex_count
        self.directed = directed
        self.adjacent = [[] for x in range(vertex_count)]
        for edge in self.edges:
            self.adjacent[edge[0] - 1].append(edge[1])
            if not directed:
                self.adjacent[edge[1] - 1].append(edge[0])

    def __str__(self):
        result = "Graph with {0} vertices.\n".format(self.vertex_count)
        for x in range(self.vertex_count):
            result += "Vertex {0} is connected to: {1}.\n".format(x + 1, self.adjacent[x])
        return result

    def breadth_first_search(self):
        visited = [False for x in range(self.vertex_count)]
        to_visit = [1]
        traversal = []
        while to_visit:
            visiting = to_visit.pop(0)
            if not visited[visiting - 1]:
                traversal.append(visiting)
                visited[visiting - 1] = True
                to_visit += [x for x in self.adjacent[visiting - 1] if not visited[x - 1]]
        return traversal

    def depth_first_traversal(self):
        visited = [False for x in range(self.vertex_count)]
        to_visit = [1]
        traversal = []
        while to_visit:
            visiting = to_visit[-1]
            if not visited[visiting - 1]:
                traversal.append(visiting)
            visited[visiting - 1] = True

            if not sum([0 if visited[x - 1] else 1 for x in self.adjacent[visiting - 1]]):
                to_visit.pop(-1)
            else:
                for adj in self.adjacent[visiting - 1]:
                    if not visited[adj - 1]:
                        to_visit.append(adj)
                        break
        return traversal

    def has_cycle(self):
        if self.directed:
            visited = [False for x in range(self.vertex_count)]
            to_visit = [1]
            while to_visit:
                visiting = to_visit[-1]
                if visited[visiting - 1]:
                    return True
                visited[visiting - 1] = True

                if not sum([0 if visited[x - 1] else 1 for x in self.adjacent[visiting - 1]]):
                    to_visit.pop(-1)
                else:
                    for adj in self.adjacent[visiting - 1]:
                        if not visited[adj - 1]:
                            to_visit.append(adj)
                            break
            return False


if __name__ == "__main__":
    edges = [
        [0, 1, 1],
        [0, 4, 1],
        [1, 2, 1],
        [1, 3, 1],
        [1, 4, 1],
        [2, 3, 1],
        [3, 4, 1]
    ]
    edges = [[x[0] + 1, x[1] + 1, x[2]] for x in edges]
    graph = Graph(edges, 5)
    print(graph)
    print(graph.breadth_first_search())
    print(graph.depth_first_traversal())

    edges2 = [
        [0, 2, 1],
        [0, 1, 1],
        [1, 2, 1],
        [2, 3, 1],
        [2, 0, 1],
        [3, 3, 1]
    ]
    g2 = Graph(edges2, 4, directed=True)
    print(g2)
    print(g2.has_cycle())

    edges3 = [
        [0, 2, 1],
        [0, 1, 1],
        [2, 3, 1]
    ]
    g3 = Graph(edges3, 4, directed=True)
    print(g3)
    print(g3.has_cycle())
