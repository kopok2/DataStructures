import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_simple_list(self):
        sl = LinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        self.assertEqual(sl.get_items(), [12, "semir", 12.123])


if __name__ == "__main__":
    unittest.main()
