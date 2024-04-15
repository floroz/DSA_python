from array_list import ArrayList


def test_create_empty_array_list():
    arr = ArrayList()
    assert arr.length == 0


def test_push_element_to_array_list():
    arr = ArrayList()
    arr.push(1)
    assert arr.length == 1


def test_pop_element_from_array_list():
    arr = ArrayList()
    arr.push(1)
    assert arr.pop() == 1
    assert arr.length == 0


def test_shift():
    arr = ArrayList()
    arr.push(1)
    arr.push(2)
    assert arr.shift() == 1
    assert arr.length == 1


def test_unshift():
    arr = ArrayList()
    arr.push(1)
    arr.unshift(2)
    assert arr.at(0) == 2
    assert arr.at(1) == 1


def test_double_capacity_when_pushing_beyond_capacity():
    arr = ArrayList(1)
    arr.push(1)
    arr.push(2)
    assert arr.length == 2


def test_access_given_index():
    arr = ArrayList(3)
    arr.push(1)
    arr.push(2)
    assert arr.at(0) == 1
    assert arr.at(1) == 2


def test_insert_at_given_index():
    arr = ArrayList(3)
    arr.push(1)
    arr.push(2)
    arr.insert(1, 3)
    assert arr.at(1) == 3


def test_not_insert_at_out_of_bounds_index():
    arr = ArrayList(3)
    arr.push(1)  # push 1 to index 0
    arr.push(2)  # push 2 to index 1
    arr.insert(3, 3)  # insert 3 to index 3
    assert arr.at(0) == 1
    assert arr.at(1) == 2
    assert arr.at(2) is None
    assert arr.length == 2
    assert arr.at(3) is None
