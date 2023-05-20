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


def sum_to_k(lst: List[int], k: int) -> List[(int, int)]:
    lst.sort()
    total_result = []
    for index, item in enumerate(lst):
        index_y = binary_search(lst, k - item)
        if index_y > -1:
            total_result.append((item, lst[index_y]))

    return total_result


class TestSumToK(unittest.TestCase):
    def test_sum_to_k_1(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 12
        estimated_result = [(0, 12), (5, 7), (7, 5), (12, 0)]

        self.assertEqual(sum_to_k(lst, key), estimated_result)

    def test_sum_to_k_2(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 15
        estimated_result = [(3, 12), (12, 3)]

        self.assertEqual(sum_to_k(lst, key), estimated_result)

    def test_sum_to_k_3(self):
        lst = [12, 5, 28, 23, 4, 3, 7, -1, 0]
        lst.sort()
        key = 90
        estimated_result = []

        self.assertEqual(sum_to_k(lst, key), estimated_result)


if __name__ == '__main__':
    unittest.main()
