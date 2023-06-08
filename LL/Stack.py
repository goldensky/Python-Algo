import unittest


class Empty(BaseException):
    pass


class Node:
    def __init__(self, data, next):
        self._data = data
        self._next = next


class Stack:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, value):
        node = Node(value, self._head)
        self._head = node
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("Empty Stack error")

        return self._head._data

    def pop(self):
        if self.is_empty():
            raise Empty("Empty Stack Error")
        element = self._head._data

        self._head = self._head._next
        self._size -= 1
        return element


class TestStack(unittest.TestCase):
    def test_create_stack(self):
        s = Stack()
        self.assertTrue(s.is_empty())

        s.push(1)
        self.assertEqual(s.top(), 1)
        self.assertFalse(s.is_empty())

        s.push(2)
        self.assertEqual(s.top(), 2)
        s.push(3)
        self.assertEqual(s.top(), 3)

        self.assertEqual(len(s), 3)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.top(), 3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

        self.assertTrue(s.is_empty())


if __name__ == "__main__":
    unittest.main()
