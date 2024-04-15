from typing import Union


class DoublyLinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next: Union[DoublyLinkedListNode, None] = None
        self.prev: Union[DoublyLinkedListNode, None] = None


class DoublyLinkedList:
    size = 0
    head: Union[DoublyLinkedListNode, None] = None
    tail: Union[DoublyLinkedListNode, None] = None

    def __init__(self, value: int = None):
        if value is not None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head

    def append(self, value: int) -> None:
        if self.head is None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head
        else:
            node = DoublyLinkedListNode(value)
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    def prepend(self, value: int) -> None:
        if self.head is None:
            self.head = DoublyLinkedListNode(value)
            self.tail = self.head
        else:
            node = DoublyLinkedListNode(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1

    def shift(self) -> Union[DoublyLinkedListNode, None]:
        if self.head is None:
            return
        tmp = self.head
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1
        return tmp

    def pop(self) -> Union[DoublyLinkedListNode, None]:
        if self.tail is None:
            return
        prev_node = None
        next_node = self.head
        while next_node is not self.tail:
            prev_node = next_node
            next_node = next_node.next
        prev_node.next = None
        self.tail = prev_node
        self.size -= 1
        return next_node

    def delete(self, value: int) -> Union[DoublyLinkedListNode, None]:
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

    def at(self, index: int) -> Union[DoublyLinkedListNode, None]:
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
        # out of bounds
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.prepend(value)
            return
        # insert new tail - O(1)
        elif index == self.size - 1:
            self.append(value)
            return
        # traverse - O(N)
        else:
            curr_node = self.head.next
            idx = 1
            while curr_node is not None and idx < index:
                curr_node = curr_node.next
                idx += 1

            if index != idx or curr_node is None:
                return

            node = DoublyLinkedListNode(value)
            self.size += 1

            prev_node = curr_node.prev

            prev_node.next = node
            node.prev = prev_node

            node.next = curr_node
            curr_node.prev = node
