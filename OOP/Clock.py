import unittest


class Clock:
    __DAY = 86400

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("not int")
        self.seconds = seconds % self.__DAY

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.get_format(h)}:{self.get_format(m)}:{self.get_format(s)}"

    @classmethod
    def get_format(self, t):
        return str(t).rjust(2, "0")

    def __str__(self):
        result = self.get_time()
        return result

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("not int or Clock instance")
        return other if isinstance(other, int) else other.seconds

    def __add__(self, other):  # c = c + 100
        s = self.__verify_data(other)
        return Clock(self.seconds + s)

    def __radd__(self, other):  # c = 100 + c
        return self + other

    def __iadd__(self, other):  # c += 100
        s = self.__verify_data(other)
        self.seconds += s
        return self

    def __sub__(self, other):
        s = self.__verify_data(other)
        return Clock(self.seconds - s)

    def __isub__(self, other):
        s = self.__verify_data(other)
        return Clock(self.seconds - s)

    def __eq__(self, other):
        s = self.__verify_data(other)
        return self.seconds == s

    def __lt__(self, other):
        s = self.__verify_data(other)
        return self.seconds < s


class TestClock(unittest.TestCase):
    def test__add__(self):
        t = 60 * 60 * 2 + 6 * 60 + 17
        c = Clock(t)
        self.assertEqual(c.get_time(), "02:06:17")

        c.seconds = c.seconds + 5 * 60
        self.assertEqual(c.get_time(), "02:11:17")

        c = c + 2 * 60 + 30
        self.assertEqual(c.get_time(), "02:13:47")

    def test__radd__(self):
        t = 60 * 60 * 2 + 6 * 60 + 17
        c = Clock(t)
        self.assertEqual(c.get_time(), "02:06:17")

        c = 30 + c
        self.assertEqual(c.get_time(), "02:06:47")

        c2 = Clock(60 * 5)
        self.assertEqual(c2.get_time(), "00:05:00")

        c3 = c + c2
        self.assertEqual(c3.get_time(), "02:11:47")

    def test__iadd__(self):
        t = 60 * 60 * 2 + 6 * 60 + 17
        c = Clock(t)
        self.assertEqual(c.get_time(), "02:06:17")
        c += 5 * 60
        self.assertEqual(c.get_time(), "02:11:17")

    def test__sub__(self):
        t = 60 * 60 * 2 + 6 * 60 + 17
        c = Clock(t)
        self.assertEqual(c.get_time(), "02:06:17")
        t2 = 60 * 5 + 5

        c = c - t2
        self.assertEqual(c.get_time(), "02:01:12")

        c2 = Clock(3600 + 10)
        c3 = c - c2
        self.assertEqual(c3.get_time(), "01:01:02")

    def test__isub__(self):
        t = 3600 * 3 + 6 * 60 + 17
        c = Clock(t)
        self.assertEqual(c.get_time(), "03:06:17")

        t2 = 3600 + 60 * 2 + 5
        c -= t2
        self.assertEqual(c.get_time(), "02:04:12")

        t3 = 3600 + 60 + 2
        c3 = Clock(t3)
        self.assertEqual(c3.get_time(), "01:01:02")
        c -= c3
        self.assertEqual(c.get_time(), "01:03:10")

    def test__eq__(self):
        t = 3600 * 3 + 6 * 60 + 17
        c1 = Clock(t)
        self.assertEqual(c1.get_time(), "03:06:17")

        c2 = Clock(t)
        self.assertEqual(c2.get_time(), "03:06:17")

        self.assertEqual(c1, c2)

    def test__eq__2(self):
        c1 = Clock(100)
        c2 = Clock(100)
        self.assertTrue(c1 == c2)

    def test__eq__3(self):
        c1 = Clock(100)
        c2 = Clock(200)
        self.assertTrue(c1 != c2)
        self.assertFalse(c1 == c2)

    def test__lt__(self):
        c1 = Clock(100)
        c2 = Clock(200)
        print(c1 < c2)
        self.assertTrue(c1 < c2)
        self.assertTrue(c2 > c1)


if __name__ == '__main__':
    unittest.main()
