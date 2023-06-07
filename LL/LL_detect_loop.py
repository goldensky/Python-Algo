import unittest

from LL_1 import LinkedList


class LLDetectLoop(LinkedList):
    def __init__(self):
        super().__init__()
        self.flag = 0

    def detect_loop_1(self):
        s = set()

        if self.head is None:
            return False

        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

    def detect_loop_2(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False


class TestDetectLoop(unittest.TestCase):
    def test_1(self):
        l = LLDetectLoop()
        l.push_back(1)
        l.push_back(2)
        l.push_back(3)
        l.push_back(4)
        l.push_back(5)
        print(l.traversal())

        l.head.next.next.next.next = l.head
        print(l.detect_loop_1())

    def test_2(self):
        l = LLDetectLoop()
        l.push_back(1)
        l.push_back(2)
        l.push_back(3)
        l.push_back(4)
        l.push_back(5)
        print(l.traversal())

        l.head.next.next.next.next = l.head
        print(l.detect_loop_2())


if __name__ == "__main__":
    unittest.main()
