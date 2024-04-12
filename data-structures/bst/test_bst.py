from bst import BinarySearchTree

def test_insert():
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.root.value == 5
    assert bst.root.left.value == 3
    assert bst.root.right.value == 7
    assert bst.root.left.left.value == 2
    assert bst.root.left.right.value == 4
    assert bst.root.right.left.value == 6
    assert bst.root.right.right.value == 8

def test_find():
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    assert bst.find(5) is True
    assert bst.find(3) is True
    assert bst.find(7) is True
    assert bst.find(2) is True
    assert bst.find(4) is True
    assert bst.find(6) is True
    assert bst.find(8) is True
    assert bst.find(1) is False
    assert bst.find(9) is False

def test_delete():
    bst = BinarySearchTree(5)
    bst.insert(7)
    bst.insert(2)
    bst.insert(5)
    assert bst.find(2) is True
    bst.delete(2)
    assert bst.find(2) is False
    bst.delete(7)
    assert bst.find(7) is False
    bst.delete(5)
    assert bst.find(5) is False
    assert bst.root is None
    
def test_delete_with_subtrees():
    bst = BinarySearchTree(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    bst.delete(3)
    assert bst.find(3) is False
    assert bst.root.left.value == 4
    assert bst.root.left.left.value == 2
    assert bst.root.left.right is None
    assert bst.root.right.value == 7
    assert bst.root.right.left.value == 6
    assert bst.root.right.right.value == 8
