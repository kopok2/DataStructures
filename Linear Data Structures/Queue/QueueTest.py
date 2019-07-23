import unittest
from Queue import Queue


class TestQueue(unittest.TestCase):
    def test_enqueueing(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual([1, 2, 3], q.get_items())

    def test_dequeueing(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        r = q.dequeue()
        self.assertEqual([2, 3], q.get_items())
        self.assertEqual(1, r)

    def test_front(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        r = q.dequeue()
        self.assertEqual(2, q.front())

    def test_rear(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        r = q.dequeue()
        self.assertEqual(3, q.rear())

    def test_is_empty(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.dequeue()
        q.dequeue()
        self.assertFalse(q.is_empty())
        q.dequeue()
        self.assertTrue(q.is_empty())


if __name__ == "__main__":
    unittest.main()
