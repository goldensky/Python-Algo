import unittest

from LL_1 import LinkedList, Node


def check_palindrom(lst):  # T = O(n), S = O(n)
    temp = lst.head
    stack = []

    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = lst.head

    while temp != None:
        if temp.data != stack.pop():
            return False

        temp = temp.next
    return True


def reverse_list(head):
    previous = None
    current = head
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous


def is_palindrome(lst):  # T = O(n), S = O(1)
    slow = fast = lst.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow = reverse_list(slow)
    head = lst.head
    while slow:
        if slow.data != head.data:
            return False
        slow = slow.next
        head = head.next
    return True


class TestLLCheckPalindrom(unittest.TestCase):
    def test_1(self):
        l = LinkedList()
        l.push_front(1)
        l.push_back(2)
        l.push_back(3)
        l.push_back(4)
        l.push_back(3)
        l.push_back(2)
        l.push_back(1)
        self.assertTrue(check_palindrom(l))

    def test_2(self):
        l = LinkedList()
        l.push_front(1)
        l.push_back(2)
        l.push_back(3)
        l.push_back(4)
        l.push_back(3)
        l.push_back(2)
        l.push_back(1)
        l.push_back(10)

        self.assertFalse(check_palindrom(l))

    def test_3(self):
        l = LinkedList(Node(5, Node(5, Node(5, Node(5)))))
        self.assertTrue(check_palindrom(l))

    def test_ispalindrome_1(self):
        l = LinkedList(Node(5, Node(5, Node(5, Node(5)))))
        self.assertTrue(is_palindrome(l))

    def test_ispalindrome_2(self):
        l = LinkedList(Node(1, Node(2, Node(2, Node(1)))))
        self.assertTrue(is_palindrome(l))

    def test_ispalindrome_3(self):
        l = LinkedList(Node(1, Node(2, Node(3, Node(2, Node(1))))))
        self.assertTrue(is_palindrome(l))

    def test_ispalindrome_4(self):
        l = LinkedList(Node(1, Node(2, Node(1, Node(1)))))
        self.assertFalse(is_palindrome(l))

    def test_ispalindrome_5(self):
        l = LinkedList(Node(1, Node(2, Node(3, Node(4, Node(1))))))
        self.assertFalse(is_palindrome(l))


if __name__ == "__main__":
    unittest.main()
