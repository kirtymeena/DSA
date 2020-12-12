# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:14:17 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        
        
    def push(self,data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node 
           
        
        else:
            new_node.next = self.head
            self.head = new_node
    def pop(self):
        if self.isEmpty():
            return"Stack is empty"
        popNode = self.head 
        self.head = self.head.next 
        popNode.next = None
        return popNode.data
    
    def isEmpty(self):
        if self.head is None:
            return "Empty"
    def peek(self):
        return self.head.data
        

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.isEmpty())