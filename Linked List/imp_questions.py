# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 12:51:06 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    
    def printList(self):
        cur_node = self.head
        
       
        
        while cur_node:
             print(cur_node.data)
            
             cur_node = cur_node.next
    
       
    
        
    
    
   
ll=LinkedList()
ll.insert(1)
ll.insert(2)


ll.printList()