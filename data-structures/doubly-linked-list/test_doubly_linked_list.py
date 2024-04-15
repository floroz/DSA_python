from doubly_linked_list import DoublyLinkedList


def test_create_linked_list():
    linked_list = DoublyLinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0


def test_add_node():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    assert linked_list.head.prev is None
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.size == 1


def test_append():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next is None
    assert linked_list.tail.value == 3
    assert linked_list.tail.prev.value == 2
    assert linked_list.tail.prev.prev.value == 1
    assert linked_list.tail.prev.prev.prev is None
    assert linked_list.size == 3


def test_prepend():
    linked_list = DoublyLinkedList()
    linked_list.prepend(1)
    linked_list.prepend(2)
    linked_list.prepend(3)
    assert linked_list.head.value == 3
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 1
    assert linked_list.head.next.next.next is None
    assert linked_list.tail.value == 1
    assert linked_list.tail.prev.value == 2
    assert linked_list.tail.prev.prev.value == 3
    assert linked_list.tail.prev.prev.prev is None
    assert linked_list.size == 3


def test_pop():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    popped_node = linked_list.pop()
    assert popped_node.value == 3
    assert linked_list.head.next.next is None
    assert linked_list.tail.value == 2
    assert linked_list.tail.prev.value == 1
    assert linked_list.size == 2


def test_shift():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    removed_node = linked_list.shift()
    assert removed_node.value == 1
    assert linked_list.head.value == 2
    assert linked_list.head.next.value == 3
    assert linked_list.head.prev is None
    assert linked_list.tail.value == 3
    assert linked_list.tail.prev.value == 2
    assert linked_list.size == 2


def test_access_at_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.at(0).value == 1
    assert linked_list.at(1).value == 2
    assert linked_list.at(2).value == 3
    assert linked_list.at(3) is None
    assert linked_list.size == 3


def test_insert_at_index():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(1, 4)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 4
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.prev.value == 4
    assert linked_list.head.next.next.next.value == 3
    assert linked_list.at(0).value == 1
    assert linked_list.at(1).value == 4
    assert linked_list.at(2).value == 2
    assert linked_list.at(3).value == 3
    assert linked_list.at(4) is None
    assert linked_list.size == 4


def test_insert_new_head():
    linked_list = DoublyLinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(0, 4)
    assert linked_list.head.value == 4
    assert linked_list.head.next.value == 1
    assert linked_list.head.next.next.value == 2
    assert linked_list.head.next.next.prev.value == 1
    assert linked_list.head.next.next.next.value == 3
    assert linked_list.at(0).value == 4
    assert linked_list.at(1).value == 1
    assert linked_list.at(2).value == 2
    assert linked_list.at(3).value == 3
    assert linked_list.at(4) is None
    assert linked_list.size == 4
