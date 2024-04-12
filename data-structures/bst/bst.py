from typing import Union

class BinarySearchTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left: Union[BinarySearchTreeNode, None] = None
        self.right: Union[BinarySearchTreeNode, None] = None
    
    def insert(self, value: int) -> None:
        if (value == self.value):
            return
        if (value < self.value):
           if (self.left):
               self.left.insert(value)
           else:
               self.left = BinarySearchTreeNode(value)
        
        else:
            if (self.right):
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)
    
    def find(self, value: int):
        pass
    
    def delete(self, value: int):
        pass
    
    
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
        self.root.delete(value)