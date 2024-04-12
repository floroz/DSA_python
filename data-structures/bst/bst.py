from typing import Union


class BinarySearchTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Union[BinarySearchTreeNode, None] = None
        self.right: Union[BinarySearchTreeNode, None] = None
    
    def insert(self, value: int) -> None:
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
    
    def find(self, value: int):
        if (self == None):
            return False
        
        if (self.value == value):
            return True
        
        if (value < self.value):
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
        if self.value == value:
            # case with no children
            if self.left == None and self.right == None:
                return None
            elif self.right == None:
                return self.right
            elif self.left == None:
                return self.right
            else:
                min_value = self.right.__min_value()
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
    
    def __min_value(self) -> int:
        if self.left is None:
            return self.value
        return self.left.__min_value()
    
class BinarySearchTree:
    def __init__(self, value: int):
        self.root = BinarySearchTreeNode(value)
    
    def insert(self, value: int):
        if self.root is None:
            self.root = BinarySearchTreeNode(value)
        else:
            self.root.insert(value)
    
    def find(self, value: int):
        if self.root is None:
            return False
        else:
            return self.root.find(value)
    
    def delete(self, value: int):
       self.root = self.root.delete(value)