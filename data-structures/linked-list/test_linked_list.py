from linked_list import LinkedList


def test_create_linked_list():
    linked_list = LinkedList()
    assert linked_list.head is None
    assert linked_list.tail is None
    assert linked_list.size == 0


def test_add_node():
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.head.value == 1
    assert linked_list.tail.value == 1
    assert linked_list.size == 1


def test_next_references():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.head.next.value == 2
    assert linked_list.head.next.next.value == 3
    assert linked_list.head.next.next.next is None
    assert linked_list.tail.value == 3
    assert linked_list.size == 3


def test_delete_last():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    popped_node = linked_list.pop()
    assert popped_node.value == 3
    assert linked_list.head.next.next is None
    assert linked_list.tail.value == 2
    assert linked_list.size == 2


def test_delete_first():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    removed_node = linked_list.shift()
    assert removed_node.value == 1
    assert linked_list.head.value == 2
    assert linked_list.head.next.value == 3
    assert linked_list.tail.value == 3
    assert linked_list.size == 2


def test_access_at_index():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    assert linked_list.at(0).value == 1
    assert linked_list.at(1).value == 2
    assert linked_list.at(2).value == 3
    assert linked_list.at(3) is None
    assert linked_list.size == 3


def test_insert_at_index():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.insert(1, 4)
    assert linked_list.head.value == 1
    assert linked_list.head.next.value == 4
    assert linked_list.head.next.next.value == 3
    assert linked_list.at(0).value == 1
    assert linked_list.at(1).value == 4
    assert linked_list.at(2).value == 3
    assert linked_list.at(3) is None
    assert linked_list.size == 4
