import unittest
from DoublyLinkedList import DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_simple_list(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        self.assertEqual(sl.get_items(), [12, "semir", 12.123])

    def test_front_insertion(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        sl.add_to_front(32)
        self.assertEqual(sl.get_items(), [32, 12, "semir", 12.123])

    def test_inline_insertion(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        n = sl.first.next_item
        sl.insert_after(n, 34)
        self.assertEqual(sl.get_items(), [12, "semir", 34, 12.123])

    def test_index_insertion(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        sl.insert_at_index(2, 34)
        self.assertEqual(sl.get_items(), [12, "semir", 34, 12.123])

    def test_index_deletion(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        sl.delete_at_index(1)
        self.assertEqual(sl.get_items(), [12, 12.123])

    def test_list_length(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        x = len(sl)
        self.assertEqual(x, 3)

    def test_swap_nodes(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        n1 = sl.first
        n2 = n1.get_next().get_next()
        sl.swap_nodes(n1, n2)
        self.assertEqual(sl.get_items(), [12.123, "semir", 12])

    def test_reverse(self):
        sl = DoublyLinkedList()
        sl.append(12)
        sl.append("semir")
        sl.append(12.123)
        sl.reverse()
        self.assertEqual(sl.get_items(), [12.123, "semir", 12])


if __name__ == "__main__":
    unittest.main()
