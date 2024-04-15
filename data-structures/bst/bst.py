from typing import Union


class BinarySearchTreeNode:
    """
    Binary Search Tree Node class.
    """

    def __init__(self, value: int):
        self.value = value
        self.left: Union[BinarySearchTreeNode, None] = None
        self.right: Union[BinarySearchTreeNode, None] = None

    def insert(self, value: int):
        """
        Insert a value in the BST.
        """
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNode(value)

        elif value > self.value:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)

    def find(self, value: int) -> bool:
        """
        Find a value in the BST.
        """
        if self is None:
            return False

        if self.value is value:
            return True

        if value < self.value:
            if self.left is not None:
                return self.left.find(value)
            else:
                return False
        else:
            if self.right is not None:
                return self.right.find(value)
            else:
                return False

    def delete(self, value: int):
        """
        Delete a value in the BST.
        """
        if self.value == value:
            # case with no children
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.right
            elif self.left is None:
                return self.right
            else:
                min_value = self.right.__min_value__()
                self.value = min_value
                self.right = self.right.delete(min_value)
                return self

        if self.value > value:
            if self.left is not None:
                self.left = self.left.delete(value)
        else:
            if self.right is not None:
                self.right = self.right.delete(value)
        return self

    def __min_value__(self) -> int:
        if self.left is None:
            return self.value
        return self.left.__min_value__()


class BinarySearchTree:
    """
    Binary Search Tree class.
    """

    def __init__(self, value: int):
        self.root = BinarySearchTreeNode(value)

    def insert(self, value: int):
        """
        Insert a value in the BST.
        """
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)

    def find(self, value: int):
        """
        Find a value in the BST.
        """
        if self.root is None:
            return False
        else:
            return self.root.find(value)

    def delete(self, value: int):
        """
        Delete a value in the BST.
        """
        self.root = self.root.delete(value)
