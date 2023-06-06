import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return "->".join(result) + "->"

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print("")

    def push_ahead(self, value):
        node = Node(value)

        node.next = self.head
        self.head = node

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        node.next = temp.next
        temp.next = node

    def insert_after_data(self, data, new_value):
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next

        if temp and temp.data == data:
            node = Node(new_value)
            node.next = temp.next
            temp.next = node

    def delete_by_value(self, value):
        if self.head and self.head.data == value:
            self.head = self.head.next

        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next and temp.next.data == value:
            temp.next = temp.next.next

    def delete_kth_node(self, k):
        if not self.head:
            return
        if k == 1:
            self.head = self.head.next
            return

        prev = None
        temp = self.head
        while temp.next and k > 1:
            prev = temp
            temp = temp.next
            k -= 1

        if k == 1:
            prev.next = temp.next


class TestLinkedList(unittest.TestCase):
    def test_create_linked_list(self):
        l = LinkedList()
        l.push_ahead(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        result = l.traversal()
        self.assertEqual(result, "1->2->3->4->5->")

    def test_insert_after_value(self):
        l = LinkedList()
        l.push_ahead(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        result = l.traversal()
        self.assertEqual(result, "1->2->3->4->5->")

        l.insert_after_data(1, 100)
        l.insert_after_data(5, 50)
        l.insert_after_data(6, 500)
        result = l.traversal()
        self.assertEqual(result, "1->100->2->3->4->5->50->")

    def test_delete_kth_node(self):
        l = LinkedList()
        l.push_ahead(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        result = l.traversal()
        self.assertEqual(result, "1->2->3->4->5->")

        # l.print_list()
        l.delete_kth_node(1)
        l.delete_kth_node(4)

        result = l.traversal()
        self.assertEqual(result, "2->3->4->")

        l.delete_kth_node(2)
        result = l.traversal()
        self.assertEqual(result, "2->4->")

    def test_delete_by_value(self):
        l = LinkedList()
        l.push_ahead(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        result = l.traversal()
        self.assertEqual(result, "1->2->3->4->5->")

        l.delete_by_value(4)
        l.delete_by_value(1)
        l.delete_by_value(5)
        l.delete_by_value(34)
        result = l.traversal()
        self.assertEqual(result, "2->3->")


if __name__ == "__main__":
    unittest.main()