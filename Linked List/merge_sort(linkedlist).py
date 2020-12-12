# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 09:28:01 2020

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
    
    def Mid(self,h):
        a = h 
        b = h
        if a is None:
            return
        if b is None:
            return 
        while a.next and b.next.next:
            a = b.next
            b = b.next.next
       
        return a    
    def merge_sort(self,h):
        if h is None or h.next is None:
            return
        middle = self.Mid(h)
        nextmid = middle.next 
        middle.next = None
        
        left = self.merge_sort(h)
        right = self.merge_sort(h)
        
        sortedlist = self.merge(left,right)
        return sortedlist
    
    def merge(self,a,b):
        if a is None:
            return
        if b is None:
            return 
        if a.data <= b.data:
            result =a 
            result.next = self.merge(a.next,b)
        else:
            result = b
            result.next = self.merge(a,b.next)
        return result
    
        
        
    
ll = LinkedList()
ll.insert(15)
ll.insert(10)
ll.insert(5)
ll.insert(20)
ll.insert(3)
ll.insert(2)

ll.merge_sort(ll.head)
ll.printList()
            
            
            
        