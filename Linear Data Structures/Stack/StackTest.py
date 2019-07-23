import unittest
from Stack import Stack


class TestStack(unittest.TestCase):
    def test_addition(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.get_items(), [1])

    def test_pop(self):
        s = Stack()
        s.push(2)
        s.push(1)
        self.assertEqual(1, s.pop())
        self.assertEqual(2, s.pop())
        self.assertEqual([], s.get_items())

    def test_peek(self):
        s = Stack()
        s.push(2)
        s.push(1)
        self.assertEqual(1, s.peek())
        self.assertEqual(1, s.peek())
        s.pop()
        self.assertEqual(2, s.peek())

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(2)
        s.push(1)
        self.assertFalse(s.is_empty())
        s.pop()
        s.pop()
        self.assertTrue(s.is_empty())


if __name__ == "__main__":
    unittest.main()
