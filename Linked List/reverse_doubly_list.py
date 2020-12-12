# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:11:31 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None
        self.prev = None
    
class DLL:
    def __init__(self):
        self.head = None
    def insert(self,data):
        new_node = Node(data)
        
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return 
       
        cur = self.head 
        while cur.next:
            cur = cur.next
        new_node.prev = cur
        cur.next=new_node
        new_node.next  = None
        
            
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next 
    
    def reverse(self):
        cur = self.head
       
        prev = None
        while cur:
          nxt = cur.next
          cur.next = prev
          prev = cur
          cur = nxt
        self.head = prev 
        print(self.head.data)
    
        
          
        
dll=DLL()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.reverse()
dll.print_list()
        
            
        
        