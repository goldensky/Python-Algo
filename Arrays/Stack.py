import unittest


class Empty(BaseException):
    pass


class ArrayStack:
    __DEFAULT_CAPACITY = 10

    def __init__(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self.__size = 0
        self.__data = [None] * self.__capacity

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __resize(self):
        if self.__size == self.__capacity:
            old = self.__data
            self.__capacity *= 2
            self.__data = [None] * self.__capacity
            for i, item in enumerate(old):
                self.__data[i] = item
        elif self.__capacity > self.__DEFAULT_CAPACITY and self.__size <= self.__capacity >> 2:
            old = self.__data
            self.__capacity >>= 1
            self.__data = [None] * self.__capacity
            for i in range(self.__size):
                self.__data[i] = old[i]

    def push(self, item):
        self.__resize()
        self.__data[self.__size] = item
        self.__size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        self.__size -= 1
        element = self.__data[self.__size]
        self.__data[self.__size] = None
        self.__resize()
        return element

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.__data[self.__size - 1]


class TestArrayStack(unittest.TestCase):
    def test_create_stack(self):
        s = ArrayStack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.top(), 2)

    def test_pop_element_from_stack(self):
        s = ArrayStack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertFalse(s.is_empty())
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.top(), 2)

    def test_resize_stack(self):
        s = ArrayStack()
        self.assertTrue(s.is_empty())
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        s.push(5)
        s.push(6)
        s.push(7)
        s.push(8)
        s.push(9)
        s.push(10)
        data = s._ArrayStack__data
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        s.push(11)
        self.assertEqual(len(s), 11)
        self.assertEqual(s._ArrayStack__capacity, 20)

        data = s._ArrayStack__data
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, None, None, None, None,
             None, None, None, None, None]
        )

        #
        for i in range(12, 12 + 15):
            s.push(i)

        self.assertEqual(s._ArrayStack__capacity, 40)

        for i in range(20):
            s.pop()

        self.assertEqual(s._ArrayStack__capacity, 20)


if __name__ == "__main__":
    unittest.main()
