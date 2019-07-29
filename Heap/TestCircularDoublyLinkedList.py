# encoding-utf-8
import unittest
from CircularDoublyLinkedList import CircularDoublyLinkedList


class TestCircularDoublyLinkedList(unittest.TestCase):
    def test_simple_list(self):
        cdll = CircularDoublyLinkedList(17)
        cdll.insert_new_node(24)
        cdll.insert_new_node(23)
        cdll.insert_new_node(7)
        cdll.insert_new_node(3)
        self.assertEqual(cdll.get_items(), [17, 24, 23, 7, 3])

    def test_delete_node(self):
        cdll = CircularDoublyLinkedList(17)
        cdll.insert_new_node(24)
        cdll.insert_new_node(23)
        cdll.insert_new_node(7)
        cdll.insert_new_node(3)
        cdll.delete_node(cdll.first)
        self.assertEqual(cdll.get_items(), [24, 23, 7, 3])

    def test_merge_cdlls(self):
        cdll1 = CircularDoublyLinkedList(17)
        cdll1.insert_new_node(24)
        cdll1.insert_new_node(23)
        cdll1.insert_new_node(7)
        cdll1.insert_new_node(3)
        cdll2 = CircularDoublyLinkedList(17)
        cdll2.insert_new_node(24)
        cdll2.insert_new_node(23)
        cdll2.insert_new_node(7)
        cdll2.insert_new_node(3)
        cdll1.merge_cdlls(cdll2)
        self.assertEqual(cdll1.get_items(), [17, 24, 23, 7, 3, 24, 23, 7, 3, 17])


if __name__ == "__main__":
    unittest.main()
