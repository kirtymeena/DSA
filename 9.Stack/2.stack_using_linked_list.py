# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 13:29:44 2020

@author: kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
    
class stack:
    def __init__(self):
        self.top = None
    
    def push(self,data):
        node = Node(data)
        if self.top is None:
            self.top = node
            return
        
        if self.top:
            node.next = self.top 
            self.top = node 
            return 
    def pop(self):
        if self.IsEmpty():
           print("Empty")
        
        cur = self.top 
        if cur:
            print(cur.data)
            self.top = cur.next
            cur = None
            return 
    def IsEmpty(self):
        if self.top is None:
            return True 
        else:
            return False
    
            
s = stack() 
s.push(1)
s.push(2)
s.push(3)

s.pop()
s.pop()
s.pop()
# print(s.IsEmpty())

        
        
        