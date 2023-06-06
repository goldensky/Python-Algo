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

    def __add__(self, other):  # c = c + 100
        if not isinstance(other, (int, Clock)):
            raise TypeError("not int or Clock instance")
        if isinstance(other, Clock):
            other = other.seconds
        return Clock(self.seconds + other)

    def __radd__(self, other):  # c = 100 + c
        return self + other

    def __iadd__(self, other):  # c += 100
        if not isinstance(other, (int, Clock)):
            raise TypeError("not int or Clock instance")

        s = other if isinstance(other, int) else other.seconds
        self.seconds += s
        return self


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
        print(c)
        self.assertEqual(c.get_time(), "02:11:17")


if __name__ == '__main__':
    unittest.main()
