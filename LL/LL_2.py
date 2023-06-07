import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            self.tail = node
            return

        node.next = self.head
        self.head = node

    def push_back(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        node.next = None
        self.tail = node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("")

    def traversal(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next

        return "->".join(result) + "->"

    def insert_after_data(self, data, new_value):
        node = Node(new_value)
        if self.head and self.head.data == data:
            node.next = self.head.next
            self.head.next = node
            return

        temp = self.head

        while temp.next and temp.data != data:
            temp = temp.next

        if temp.next and temp.data == data:
            node.next = temp.next
            temp.next = node


class TestLinkedList(unittest.TestCase):
    def test_1(self):
        l = LinkedList()
        l.push_front(10)
        l.push_back(1)
        l.push_back(2)
        l.push_back(3)
        l.push_front(20)
        print(l.traversal())

        self.assertEqual(l.traversal(), "20->10->1->2->3->")

        l.insert_after_data(20, 100)
        l.insert_after_data(100, 1000)
        print(l.traversal())

        self.assertEqual(l.traversal(), "20->100->1000->10->1->2->3->")


if __name__ == "__main__":
    unittest.main()
