import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self, node=None):
        self.__head = None
        self.__tail = None
        self.size = 1 if node is not None else 0

    def __len__(self):
        return self.size

    def push_front(self, value):
        node = Node(value)
        self.size += 1

        if self.__head is None:
            self.__head = node
            self.__tail = node

        else:
            node.next = self.__head
            self.__head.prev = node
            self.__head = node

    def push_back(self, value):
        node = Node(value)
        self.size += 1

        if self.__head is None:
            self.__head = node
            self.__tail = node
        else:
            self.__tail.next = node
            node.prev = self.__tail
            self.__tail = node

    def traversal(self):
        result = []
        temp = self.__head
        while temp:
            result.append(str(temp.data))
            temp = temp.next
        return "->".join(result) + "->"

    def insert_after_node(self, left_node, value):
        node = Node(value)
        self.size += 1

        right_node = left_node.next
        node.next = right_node
        right_node.prev = node

        node.prev = left_node
        left_node.next = node

    def find_node(self, value):
        if not self.__head and not self.__tail:
            return

        if self.__head.data == value:
            return self.__head

        if self.__tail.data == value:
            return self.__tail

        temp = self.__head
        while temp.next and temp.data != value:
            temp = temp.next

        if temp and temp.data == value:
            return temp
        return None

    def pop_front(self):
        if not self.__head:
            return
        self.size -= 1
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
            return
        node = self.__head.next
        self.__head = node
        node.prev = None

    def pop_back(self):
        if not self.__tail:
            return

        self.size -= 1
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
            return
        node = self.__tail
        left = self.__tail.prev
        left.next = None
        self.__tail = left
        node.prev = None

    def delete_node(self, node):
        if not node:
            return

        if node.data == self.__head.data:
            self.pop_front()
            return

        if node.data == self.__tail.data:
            self.pop_back()
            return

        try:
            left_node = node.prev
            right_node = node.next

            left_node.next = right_node
            right_node.prev = left_node
            self.size -= 1

        except AttributeError as err:
            return


class TestDoublyLinkedList(unittest.TestCase):
    def test_push_front(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->")

        self.assertEqual(a.size, 3)

    def test_push_back(self):
        a = DoublyLinkedList()
        a.push_back(1)
        a.push_back(2)
        a.push_back(3)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->")

    def test_find_node(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        a.push_back(4)
        a.push_back(5)
        a.push_back(6)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->4->5->6->")

        self.assertEqual(a.find_node(1).data, 1)
        self.assertEqual(a.find_node(3).data, 3)
        self.assertEqual(a.find_node(6).data, 6)

    def test_insert_after_first_node(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->")

        node_1 = a.find_node(1)
        a.insert_after_node(node_1, 100)
        result = a.traversal()
        self.assertEqual(result, "1->100->2->3->")

    def test_insert_after_node_inside_list(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        a.push_back(4)
        a.push_back(5)
        a.push_back(6)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->4->5->6->")
        self.assertEqual(a.size, 6)

        node_3 = a.find_node(3)
        a.insert_after_node(node_3, 100)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->100->4->5->6->")
        self.assertEqual(a.size, 7)

    def test_pop_front(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->")
        self.assertEqual(a.size, 3)

        node = a.find_node(1)
        self.assertEqual(node.data, 1)
        a.pop_front()
        result = a.traversal()
        self.assertEqual(result, "2->3->")
        self.assertEqual(a.size, 2)

    def test_pop_back(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->")
        self.assertEqual(a.size, 3)

        node = a.find_node(3)
        self.assertEqual(node.data, 3)
        a.pop_back()
        result = a.traversal()
        self.assertEqual(result, "1->2->")
        self.assertEqual(a.size, 2)

    def test_delete_node_inside_list__node_exist(self):
        a = DoublyLinkedList()
        a.push_front(3)
        a.push_front(2)
        a.push_front(1)
        a.push_back(4)
        a.push_back(5)
        a.push_back(6)
        result = a.traversal()
        self.assertEqual(result, "1->2->3->4->5->6->")
        self.assertEqual(a.size, 6)

        node = a.find_node(3)
        a.delete_node(node)
        result = a.traversal()
        self.assertEqual(result, "1->2->4->5->6->")
        self.assertEqual(a.size, 5)


if __name__ == "__main__":
    unittest.main()
