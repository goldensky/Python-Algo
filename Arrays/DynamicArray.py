import unittest


class DynamicArray:
    __DEFAULT_CAPACITY = 8

    def __init__(self):
        self.__capacity = self.__DEFAULT_CAPACITY
        self._data = [None] * self.__capacity
        self.__size = 0

    def __len__(self):
        return self.__size

    def __resize(self):
        if self.__size == self.__capacity:
            old = self._data
            self.__capacity *= 2
            self._data = [None] * self.__capacity
            for i, item in enumerate(old):
                self._data[i] = item

        elif self.__capacity > self.__DEFAULT_CAPACITY and self.__size <= self.__capacity >> 2:
            old = self._data
            self.__capacity >>= 1
            self._data = [None] * self.__capacity
            for i in range(self.__capacity):
                self._data[i] = old[i]
                if old[i] is None:
                    break

    def append(self, item):
        self.__resize()
        self._data[self.__size] = item
        self.__size += 1

    def pop(self, index=None):
        if index is None:
            self.__size -= 1
            element = self._data[self.__size]
            self._data[self.__size] = None

        else:
            element = self._data[index]

            k = index
            while k < self.__size:
                self._data[k] = self._data[k + 1]
                k += 1
            self._data[k] = None
            self.__size -= 1
        self.__resize()
        return element

    def copy(self):
        obj = DynamicArray()
        obj._data = [None] * self.__capacity
        for i, item in enumerate(self._data):
            obj._data[i] = item

        obj.__size = self.__size
        return obj

    def index(self, value):
        for i, item in enumerate(self._data):
            if item == value:
                return i
        raise ValueError(f"{value} is not in the DynamicArray")

    def count(self, value):
        c = 0
        for item in self._data:
            if item == value:
                c += 1
        return c

    def remove(self, value):
        try:
            index = self.index(value)
            k = index
            while k < self.__size:
                self._data[k] = self._data[k + 1]
                k += 1
            self.__size -= 1
            self._data[self.__size] = None

        except ValueError as err:
            raise ValueError(f"{value} is not in the DynamicArray")
        self.__resize()

    def insert(self, index, value):
        self.__resize()
        if index > self.__size:
            index = self.__size

        if index == self.__size:
            self.append(value)

        else:
            k = self.__size
            while k > index:
                self._data[k] = self._data[k - 1]
                k -= 1
            self._data[k] = value
            self.__size += 1

    def extend(self, dynamic_array):
        if self.__size + dynamic_array.__size < self.__capacity:
            for i in range(dynamic_array.__size):
                self._data[self.__size] = dynamic_array._data[i]
                self.__size += 1

        else:
            self.__capacity = len(self._data) + len(dynamic_array._data)
            old = self._data
            self._data = [None] * self.__capacity

            for i, item in enumerate(old):
                self._data[i] = item

            for i in range(dynamic_array.__size):
                self._data[self.__size] = dynamic_array._data[i]
                self.__size += 1

    def reverse(self):
        i = 0
        k = self.__size - 1
        old = self._data
        self._data = [None] * self.__capacity

        while k >= 0:
            self._data[i] = old[k]
            k -= 1
            i += 1


class TestDynamicArray(unittest.TestCase):
    def test_append(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)

        self.assertEqual(
            array._data,
            [1, 2, 3, None, None, None, None, None]
        )
        self.assertEqual(len(array), 3)

    def test_pop(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)

        # 1
        self.assertEqual(
            array._data,
            [1, 2, 3, 4, 5, None, None, None]
        )
        self.assertEqual(len(array), 5)
        self.assertEqual(array.pop(), 5)

        self.assertEqual(
            array._data,
            [1, 2, 3, 4, None, None, None, None]
        )
        self.assertEqual(len(array), 4)

        # 2
        self.assertEqual(array.pop(0), 1)
        self.assertEqual(
            array._data,
            [2, 3, 4, None, None, None, None, None]
        )
        self.assertEqual(len(array), 3)

        # 3
        self.assertEqual(array.pop(1), 3)
        self.assertEqual(
            array._data,
            [2, 4, None, None, None, None, None, None]
        )
        self.assertEqual(len(array), 2)

    def test_resize(self):
        array = DynamicArray()
        for i in range(1, 8 + 1):
            array.append(i)
        self.assertEqual(
            array._data,
            [1, 2, 3, 4, 5, 6, 7, 8]
        )
        self.assertEqual(len(array), 8)

        array.append(9)
        self.assertEqual(
            array._data,
            [1, 2, 3, 4, 5, 6, 7, 8,
             9, None, None, None, None, None, None, None
             ]
        )
        self.assertEqual(len(array), 9)
        self.assertEqual(array._DynamicArray__capacity, 16)

        for i in range(5):
            array.pop()

        self.assertEqual(
            array._data,
            [1, 2, 3, 4, None, None, None, None]
        )
        self.assertEqual(len(array), 4)

    def test_index(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(100)
        array.append(500)
        self.assertEqual(array.index(1), 0)
        self.assertEqual(array.index(100), 3)
        self.assertEqual(array.index(500), 4)

    def test_copy(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(100)
        array.append(500)

        array_copy = array.copy()
        self.assertTrue(isinstance(array_copy, DynamicArray))
        self.assertEqual(
            array_copy._data,
            [1, 2, 3, 100, 500, None, None, None]
        )
        self.assertEqual(len(array_copy), 5)
        self.assertEqual(len(array_copy), len(array))

    def test_remove(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(100)
        array.append(500)
        self.assertEqual(
            array._data,
            [1, 2, 3, 100, 500, None, None, None]
        )
        self.assertEqual(len(array), 5)

        #
        array.remove(1)
        self.assertEqual(
            array._data,
            [2, 3, 100, 500, None, None, None, None]
        )
        self.assertEqual(len(array), 4)
        #
        array.remove(500)
        self.assertEqual(
            array._data,
            [2, 3, 100, None, None, None, None, None]
        )
        self.assertEqual(len(array), 3)
        #
        array.remove(3)
        self.assertEqual(
            array._data,
            [2, 100, None, None, None, None, None, None]
        )
        self.assertEqual(len(array), 2)

    def test_insert(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(100)
        array.append(500)
        self.assertEqual(
            array._data,
            [1, 2, 3, 100, 500, None, None, None]
        )
        self.assertEqual(len(array), 5)
        #
        array.insert(0, 200)
        self.assertEqual(
            array._data,
            [200, 1, 2, 3, 100, 500, None, None]
        )
        self.assertEqual(len(array), 6)
        #
        array.insert(1, 300)
        self.assertEqual(
            array._data,
            [200, 300, 1, 2, 3, 100, 500, None]
        )
        self.assertEqual(len(array), 7)

    def test_count(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(1)
        self.assertEqual(array.count(1), 2)

    def test_reverse(self):
        array = DynamicArray()
        array.append(1)
        array.append(2)
        array.append(3)
        array.append(4)
        array.append(5)
        self.assertEqual(
            array._data,
            [1, 2, 3, 4, 5, None, None, None]
        )
        self.assertEqual(len(array), 5)

        array.reverse()

        self.assertEqual(
            array._data,
            [5, 4, 3, 2, 1, None, None, None]
        )
        self.assertEqual(len(array), 5)

    def test_extend(self):
        array_1 = DynamicArray()
        array_1.append(1)
        array_1.append(2)
        array_1.append(3)
        self.assertEqual(
            array_1._data,
            [1, 2, 3, None, None, None, None, None]
        )
        self.assertEqual(len(array_1), 3)

        #
        array_2 = DynamicArray()
        array_2.append(10)
        array_2.append(20)

        self.assertEqual(
            array_2._data,
            [10, 20, None, None, None, None, None, None]
        )
        self.assertEqual(len(array_2), 2)
        #
        array_1.extend(array_2)

        self.assertEqual(
            array_1._data,
            [1, 2, 3, 10, 20, None, None, None]
        )
        self.assertEqual(len(array_1), 5)


if __name__ == "__main__":
    unittest.main()
