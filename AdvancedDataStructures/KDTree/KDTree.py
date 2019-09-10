# coding=utf-8
"""K-Dimensional Tree Python implementation."""

K = 2


class Node:
    def __init__(self, point):
        self.point = point
        self.left = None
        self.right = None


def search_rec(root, point, depth):
    if not root:
        return None
    if are_point_same(root.point, point):
        return True
    cd = depth % K
    if point[cd] < root.point[cd]:
        return search_rec(root.left, point, depth + 1)
    return search_rec(root.right, point, depth + 1)


def search(root, point):
    return search_rec(root, point, 0)


def insert_rec(root, point, depth):
    if not root:
        return Node(point)
    cd = depth % K
    if point[cd] < root.point[cd]:
        root.left = insert_rec(root.left, point, depth + 1)
    else:
        root.right = insert_rec(root.right, point, depth + 1)
    return root


def insert(root, point):
    return insert_rec(root, point, 0)


def min_node(x, y, z, d):
    res = x
    if y:
        if y.point[d] < res.point[d]:
            res = y
    if z:
        if z.point[d] < res.point[d]:
            res = z
    return res


def find_min_rec(root, d, depth):
    if not root:
        return None
    cd = depth % K
    if cd == d:
        if not root.left:
            return root
        return find_min_rec(root.left, d, depth + 1)
    return min_node(root, find_min_rec(root.left, d, depth + 1), find_min_rec(root.right, d, depth + 1), d)


def find_min(root, d):
    return find_min_rec(root, d, 0)


def are_point_same(p1, p2):
    for i in range(K):
        if p1[i] != p2[i]:
            return False
    return True


def delete_node_rec(root, point, depth):
    if not root:
        return None
    cd = depth % K
    if are_point_same(root.point, point):
        if root.right:
            mint = find_min(root.right, cd)
            root.point = mint.point[::]
            root.right = delete_node_rec(root.right, mint.point, depth + 1)
        elif root.left:
            mint = find_min(root.left, cd)
            root.point = mint.point[::]
            root.right = delete_node_rec(root.left, mint.point, depth + 1)
        else:
            del root
            return None
        return root
    if point[cd] < root.point[cd]:
        root.left = delete_node_rec(root.left, point, depth + 1)
    else:
        root.right = delete_node_rec(root.right, point, depth + 1)
    return root


def delete_node(root, point):
    return delete_node_rec(root, point , 0)


if __name__ == "__main__":
    points = [
              [30, 40],
              [5, 25],
              [70, 70],
              [10, 12],
              [50, 30],
              [35, 45]
    ]
    root = None
    for p in points:
        root = insert(root, p)
    print(search(root, [30, 40]))
    root = delete_node(root, points[0])
    print(root.point)
    print(search(root, [30, 40]))
    print(search(root, [70, 70]))
