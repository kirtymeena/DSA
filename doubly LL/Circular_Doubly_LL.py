# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 16:55:19 2020

@author: kirty
"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None
    
class CDLL:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        cur = self.head 
        node=  Node(data)
        if self.head is None:
            self.head = node
            self.head.next = node
            node.prev = None
            return 
        prev = None
        
        
        while cur :
            prev = cur
            if cur.next == self.head:
                break
            
            cur = cur.next 
        prev.next = node
        node.prev = cur 
        node.next = self.head 
        self.head.prev = node
        
    
    def print_list(self):
        cur = self.head 
        while cur:
            print(cur.data,end=" ")
            if cur.next == self.head:
                break
            cur = cur.next 
    def IsDoubly_circular(self):
        cur = self.head 
        if self.head is None:
            return
        while cur:
            if cur.next == self.head and self.head.prev == cur:
                
                return True 
            cur  =cur.next 
        
        
        
                
        
    
      
    
cd = CDLL()
cd.insert(1)
cd.insert(2)
cd.insert(3)
cd.insert(4)
# cd.check()
print(cd.IsDoubly_circular())
cd.print_list()
            
        
        
        
        