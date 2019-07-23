"""Sliding Window Maximum - Maximum of all subarrays of size k

Given an array and an integer K, find the maximum for each and every contiguous subarray of size k.
"""

from Deque import Deque


def sliding_window_maximum(array, k):
    dq = Deque()
    swm = []
    for i in range(k):
        while not dq.is_empty() and array[i] >= array[dq.get_last()]:
            dq.delete_last()
        dq.insert_last(i)

    for i in range(k, len(array)):
        swm.append(array[dq.get_front()])
        while not dq.is_empty() and dq.get_front() <= i - k:
            dq.delete_front()
        while not dq.is_empty() and array[i] >= array[dq.get_last()]:
            dq.delete_last()
        dq.insert_last(i)
    swm.append(array[dq.get_front()])
    return swm


if __name__ == "__main__":
    print(sliding_window_maximum([12, 1, 78, 90, 57, 89, 56], 3))
