import unittest


class Empty(BaseException):
    pass


class ArrayDeque:
    __DEFAULT_CAPACITY = 10

    def __init__(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self.__data = [None] * self.__capacity
        self.__size = 0
        self.__front = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.__data[self.__front]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        back = (self.__front + self.__size - 1) % self.__capacity
        return self.__data[back]

    def add_first(self, value):
        self.__resize()
        self.__front = (self.__front - 1) % self.__capacity
        self.__data[self.__front] = value
        self.__size += 1

    def add_last(self, value):
        self.__resize()
        position = (self.__front + self.__size) % self.__capacity
        self.__data[position] = value
        self.__size += 1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        first = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        self.__resize()
        return first

    def delete_last(self):
        if self.is_empty():
            raise Empty("Deque is empty")

        back = (self.__front + self.__size - 1) % self.__capacity
        last = self.__data[back]
        self.__data[back] = None
        self.__size -= 1
        self.__resize()
        return last

    def __resize(self):
        if self.__size == self.__capacity:
            new_capacity = self.__capacity * 2
            old = self.__data
            self.__data = [None] * new_capacity
            for i in range(self.__size):
                self.__data[i] = old[self.__front]
                self.__front = (self.__front + 1) % self.__capacity

            self.__front = 0
            self.__capacity = new_capacity

        elif self.__capacity > self.__DEFAULT_CAPACITY and self.__size <= self.__capacity >> 2:
            new_capacity = self.__capacity >> 1
            old = self.__data
            self.__data = [None] * new_capacity
            for i in range(self.__size):
                self.__data[i] = old[self.__front]
                self.__front = (self.__front + 1) % self.__capacity
            self.__capacity = new_capacity
            self.__front = 0


class TestArrayDeque(unittest.TestCase):
    def test_create_deque(self):
        d = ArrayDeque()
        self.assertTrue(d.is_empty())

        d.add_first(1)
        d.add_last(2)

        self.assertEqual(d.first(), 1)
        self.assertEqual(d.last(), 2)

    def test_delete_last(self):
        d = ArrayDeque()
        self.assertTrue(d.is_empty())

        d.add_first(1)
        d.add_last(2)
        d.add_last(3)
        d.add_last(4)
        d.add_last(5)

        self.assertEqual(d.first(), 1)
        self.assertEqual(d.last(), 5)

        self.assertEqual(d.delete_first(), 1)
        self.assertEqual(d.delete_last(), 5)

    def test_resize_1(self):
        d = ArrayDeque()
        self.assertTrue(d.is_empty())

        for i in range(1, 10 + 1):
            d.add_last(i)

        data = d._ArrayDeque__data

        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertEqual(len(d), 10)

        d.add_last(11)
        self.assertEqual(d._ArrayDeque__capacity, 20)

        data = d._ArrayDeque__data
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, None, None, None, None,
             None, None, None, None, None,
             ]
        )

    def test_resize_2(self):
        d = ArrayDeque()
        self.assertTrue(d.is_empty())

        for i in range(10, 0, -1):
            d.add_first(i)

        data = d._ArrayDeque__data

        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        self.assertEqual(len(d), 10)

        d.add_last(11)
        self.assertEqual(d._ArrayDeque__capacity, 20)

        data = d._ArrayDeque__data
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, None, None, None, None,
             None, None, None, None, None,
             ]
        )
        self.assertEqual(d.delete_last(), 11)
        self.assertEqual(d.delete_last(), 10)
        self.assertEqual(d.delete_last(), 9)
        self.assertEqual(d.delete_last(), 8)

        self.assertEqual(d.delete_first(), 1)
        self.assertEqual(d.delete_first(), 2)

        data = d._ArrayDeque__data
        self.assertEqual(
            data,
            [3, 4, 5, 6, 7, None, None, None, None, None]
        )
        self.assertEqual(len(d), 5)


if __name__ == "__main__":
    unittest.main()
