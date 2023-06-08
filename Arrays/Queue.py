import unittest


class Empty(BaseException):
    pass


class ArrayQueue:
    __DEFAULT_CAPACITY = 10

    def __init__(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self.__data = [None] * self.__capacity
        self.__front = 0
        self.__size = 0

    def __len__(self):
        return self.__size

    def is_empty(self):
        return self.__size == 0

    def __resize(self):
        if self.__size == self.__capacity:
            old = self.__data
            self.__capacity *= 2
            self.__data = [None] * self.__capacity

            for i in range(self.__size):
                self.__data[i] = old[self.__front]
                self.__front = (self.__front + 1) % self.__capacity

            self.__front = 0

        elif self.__capacity > self.__DEFAULT_CAPACITY and self.__size <= self.__capacity >> 2:
            old = self.__data
            new_capacity = self.__capacity >> 1

            self.__data = [None] * new_capacity
            for i in range(self.__size):
                self.__data[i] = old[self.__front]
                self.__front = (self.__front + 1) % self.__capacity

            self.__front = 0
            self.__capacity = new_capacity

    def enqueue(self, item):
        self.__resize()
        position = (self.__front + self.__size) % self.__capacity
        self.__data[position] = item
        self.__size += 1

    def first(self):
        if self.is_empty():
            raise Empty("Empty Queue")
        return self.__data[self.__front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Empty Queue")
        element = self.__data[self.__front]
        self.__data[self.__front] = None
        self.__front = (self.__front + 1) % self.__capacity
        self.__size -= 1
        self.__resize()
        return element


class TestArrayQueue(unittest.TestCase):
    def test_create_queue(self):
        q = ArrayQueue()
        self.assertTrue(q.is_empty())

        q.enqueue(1)
        self.assertFalse(q.is_empty())

    def test_enqueue_and_dequeue(self):
        q = ArrayQueue()
        self.assertTrue(q.is_empty())

        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 3)

        data = q._ArrayQueue__data
        self.assertEqual(
            data,
            [1, 2, 3, None, None, None, None, None, None, None]
        )

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.first(), 3)
        self.assertEqual(len(q), 1)

    def test_resize_queue(self):
        q = ArrayQueue()
        self.assertTrue(q.is_empty())

        for i in range(1, 10 + 1):
            q.enqueue(i)

        self.assertFalse(q.is_empty())
        self.assertEqual(len(q), 10)
        self.assertEqual(q.first(), 1)

        data = q._ArrayQueue__data
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )
        q.enqueue(11)
        data = q._ArrayQueue__data

        self.assertEqual(len(q), 11)

        self.assertEqual(q._ArrayQueue__capacity, 20)
        self.assertEqual(
            data,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, None, None, None, None,
             None, None, None, None, None
             ]
        )

        data = q._ArrayQueue__data

        #
        for i in range(5 + 1):
            q.dequeue()

        data = q._ArrayQueue__data
        self.assertEqual(
            data,
            [7, 8, 9, 10, 11, None, None, None, None, None]
        )


if __name__ == "__main__":
    unittest.main()
