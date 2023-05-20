import unittest
import math
from typing import List


def koko_eat_bananas(arr: List[int], h: int) -> int:
    if len(arr) > h:
        return -1

    arr.sort()
    l = 1
    r = arr[-1]

    while r - l > 1:
        m = (r + l) // 2  # bananas per hour
        count = 0

        for i in arr:
            count += math.ceil(i / m)
        if count > h:
            l = m
        else:
            r = m
    return r


class TestKokoEatBanans(unittest.TestCase):
    def test_1(self):
        lst = [3, 6, 7, 11]
        lst.sort()
        hours = 8
        self.assertEqual(koko_eat_bananas(lst, hours), 4)

    def test_2(self):
        lst = [30, 11, 23, 4, 20]
        lst.sort()
        hours = 5
        self.assertEqual(koko_eat_bananas(lst, hours), 30)

    def test_3(self):
        lst = [30, 11, 23, 4, 20]
        lst.sort()
        hours = 6
        self.assertEqual(koko_eat_bananas(lst, hours), 23)

    def test_4(self):
        lst = [30, 11, 23, 4, 20]
        lst.sort()
        hours = 3
        self.assertEqual(koko_eat_bananas(lst, hours), -1)


if __name__ == '__main__':
    unittest.main()
