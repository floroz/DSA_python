from typing import Union


class LinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next: Union[LinkedListNode, None] = None


class LinkedList:
    size = 0
    head: Union[LinkedListNode, None] = None
    tail: Union[LinkedListNode, None] = None

    def __init__(self, value: int = None):
        if value is not None:
            self.head = LinkedListNode(value)
            self.tail = self.head

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            node = LinkedListNode(value)
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: int) -> None:
        if self.head is None:
            self.head = LinkedListNode(value)
            self.tail = self.head
        else:
            node = LinkedListNode(value)
            node.next = self.head
            self.head = node
        self.size += 1

    def shift(self) -> Union[LinkedListNode, None]:
        if self.head is None:
            return
        tmp = self.head
        self.head = self.head.next
        self.size -= 1
        return tmp

    def pop(self) -> Union[LinkedListNode, None]:
        if self.tail is None:
            return
        prev_node = None
        next_node = self.head
        while next_node is not self.tail:
            prev_node = next_node
            next_node = next_node.next
        tmp = self.tail
        prev_node.next = None
        self.tail = prev_node
        self.size -= 1
        return tmp

    def delete(self, value: int) -> Union[LinkedListNode, None]:
        if self.head is None:
            return
        if self.head.value is value:
            return self.shift()
        prev_node = None
        curr_node = self.head
        while value is not curr_node.value and curr_node is not None:
            prev_node = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev_node.next = curr_node.next
        self.size -= 1
        return curr_node

    def at(self, index: int) -> Union[LinkedListNode, None]:
        if self.head is None:
            return
        curr_node = self.head
        idx = 0
        while curr_node is not None and idx < index:
            curr_node = curr_node.next
            idx += 1
        if index != idx:
            return None
        return curr_node

    def insert(self, index, value) -> None:
        if index == 0:
            if self.head is None:
                self.head = LinkedListNode(value)
                self.size += 1
            else:
                node = LinkedListNode(value)
                node.next = self.head
                self.head = node
        prev_node = self.head
        curr_node = self.head.next
        idx = 1
        while curr_node is not None and idx < index:
            curr_node = curr_node.next
            idx += 1
        if index != idx:
            return None
        node = LinkedListNode(value)
        prev_node.next = node
        node.next = curr_node.next
        self.size += 1
