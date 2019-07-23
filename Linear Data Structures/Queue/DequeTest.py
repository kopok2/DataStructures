import unittest
from Deque import Deque


class TestLinkedList(unittest.TestCase):
    def test_insert_front(self):
        d = Deque()
        d.insert_front(1)
        d.insert_front(2)
        d.insert_front(3)
        self.assertEqual([3, 2, 1], d.get_items())

    def test_insert_last(self):
        d = Deque()
        d.insert_last(1)
        d.insert_last(2)
        d.insert_last(3)
        self.assertEqual([1, 2, 3], d.get_items())

    def test_delete_front(self):
        d = Deque()
        d.insert_front(1)
        d.insert_front(2)
        d.insert_front(3)
        d.delete_front()
        d.delete_front()
        self.assertEqual([1], d.get_items())

    def test_delete_last(self):
        d = Deque()
        d.insert_front(1)
        d.insert_front(2)
        d.insert_front(3)
        d.delete_last()
        d.delete_last()
        self.assertEqual([3], d.get_items())

    def test_get_front(self):
        d = Deque()
        d.insert_front(1)
        self.assertEqual(1, d.get_front())
        d.insert_front(2)
        d.insert_front(3)
        self.assertEqual(3, d.get_front())
        d.delete_last()
        d.delete_last()
        self.assertEqual(3, d.get_front())

    def test_get_last(self):
        d = Deque()
        d.insert_front(1)
        self.assertEqual(1, d.get_last())
        d.insert_front(2)
        d.insert_front(3)
        self.assertEqual(1, d.get_last())
        d.delete_last()
        d.delete_last()
        self.assertEqual(3, d.get_last())

    def test_is_empty(self):
        d = Deque()
        self.assertTrue(d.is_empty())
        d.insert_front(1)
        self.assertFalse(d.is_empty())
        d.insert_front(2)
        d.insert_front(3)
        self.assertFalse(d.is_empty())
        d.delete_last()
        d.delete_last()
        d.delete_last()
        self.assertTrue(d.is_empty())


if __name__ == "__main__":
    unittest.main()
