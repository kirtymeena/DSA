# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:06:13 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
         
        if self.head is None:
            self.head = new_node
            new_node.next = None
            new_node.prev = None
            
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        
        cur_node.next = new_node
        new_node.prev = cur_node 
        new_node.next = None
        
    def print_DLL(self):
        cur_node =self.head 
        while cur_node:
            print(cur_node.data)
            
            cur_node = cur_node.next
            
    def delete_node(self,node):
        cur_node = self.head
        prev = None
        
        while cur_node:
            if cur_node.data==node and cur_node == self.head:
                if not cur_node.next:
                    cur_node=None
                    self.head = None
                    return 
                else:
                    nxt = cur_node.next 
                    cur_node.next = None
                    nxt.prev = None
                    cur_node = None
                    self.head = nxt 
                    return
            elif cur_node.data == node:
                if cur_node.next:
                    nxt = cur_node.next
                    prev = cur_node.prev 
                    prev.next = nxt
                    nxt.prev = prev
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return 
            else:
                prev = cur_node.prev 
                prev.next = None
                cur_node.prev = None
                cur_node = None
                
        cur_node = cur_node.next
dll = DoublyLL()
dll.insert(1)
dll.insert(2)
dll.insert(3)
dll.insert(4)
dll.delete_node(2)
dll.print_DLL()
            
        