# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:24:31 2020

@author: Kirty
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self,root):
        self.root = Node(root)
        
        
        
    def printTree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preorder(tree.root,'')
        if traversal_type =="inorder":
            return self.inorder(tree.root,"")
        
    def preorder(self,start,traversal):
        if start:
            traversal+=str(start.value)+"-"
            traversal= self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        
        return traversal
    
    def inorder(self,start,traversal):
        if start:
            while start.left is not None:
                start = start.left
            traversal = self.inorder(start.left, traversal)
            traversal+=str(start.value)+"-"
            traversal = self.inorder(start.right,traversal)
        return traversal
            
            
            
"""
                     1
                  /     \
                 2       3
               /   \    /  \
              4     5  6   7 

"""      

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right=Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left=Node(6)
tree.root.right.right = Node(7)

print(tree.printTree("inorder"))
