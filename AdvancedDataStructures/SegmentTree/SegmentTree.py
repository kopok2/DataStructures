# coding=utf-8
"""Segment tree Python implementation."""


class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None


class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.root = None

    def construct(self):
        """Construct segment tree from given array."""
        for x in range(self.elements):
