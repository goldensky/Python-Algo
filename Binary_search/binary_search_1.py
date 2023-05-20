import unittest
from typing import List


def binary_search(lst: List[int], key: int) -> int:
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == key:

            return mid
        elif lst[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_1(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 5
        self.assertEqual(binary_search(lst, key), 4)

    def test_binary_search_2(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 7
        self.assertEqual(binary_search(lst, key), 5)

    def test_binary_search_3(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = -3
        self.assertEqual(binary_search(lst, key), -1)

    def test_binary_search_4(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 80
        self.assertEqual(binary_search(lst, key), -1)

    def test_binary_search_5(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 20
        self.assertEqual(binary_search(lst, key), -1)

    def test_binary_search_6(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = -1
        self.assertEqual(binary_search(lst, key), 0)

    def test_binary_search_7(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 28
        self.assertEqual(binary_search(lst, key), 8)


if __name__ == '__main__':
    unittest.main()
