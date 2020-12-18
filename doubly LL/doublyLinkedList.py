# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 13:43:33 2020

@author: kirty
"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None 
    
class DLL:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        node = Node(data)
        cur = self.head 
        
        if self.head is None:
            self.head = node
            node.prev = None 
            return 
        while cur.next:
            cur = cur.next 
        cur.next = node
        node.prev = cur 
    
    def print_list(self):
        cur = self.head 
        while cur:
            print(cur.data,end=" ")
            
            cur = cur.next
    def insert_at_front(self,data):
        # time complexiy -O(1)
        node = Node(data)
        
        if self.head is None:
            self.head = node
            node.prev = None
            return
        self.head.prev = node
        node.next= self.head 
        self.head = node
    
    def insert_at_end(self,data): #o(n)
        node = Node(data)
        cur = self.head
        prev = None
        
        if self.head is None:
            return 
        while cur:
            prev = cur 
            cur = cur.next
        prev.next = node 
        node.prev = prev
    
    def reverse(self):
        # time complexity - O(n)
        cur = self.head 
        
       
        while cur:
            prev = cur.prev
            cur.prev = cur.next 
            cur.next = prev 
            cur = cur.prev  
        self.head = prev.prev
    
    def delete_head(self):
        # time complexity - O(1)
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return 
        self.head = self.head.next 
        self.head.prev = None
        
    def delete_last_node(self):
        # time complexity - O(n)
        cur = self.head 
        if self.head is None:
            return 
        if self.head.next is None:
            self.head = None
            return 
            
        while cur.next.next:
            cur = cur.next
        cur.next = None
    
    def insert_at_pos(self,key,data):
        node = Node(data)
        cur = self.head 
        count = 1
        prev = None
        
        if count==key:
            node.next = self.head 
            node.prev = None
            self.head = node
            return 
        if self.head is None:
            return 
        
        while cur and count!=key:
            count+=1
            prev = cur
            cur = cur.next
         
        node.prev = cur.prev
        node.next = prev.next
        prev.next = node
    
    def insert_in_sorted_list(self,data):
        node = Node(data)
        cur = self.head 
        prev = None
        
        if self.head.data>=node.data:
            node.next = self.head 
            node.prev = None
            self.head  = node
            return 
        while cur.next:
            prev = cur 
            cur=  cur.next
           
            if cur.data>=node.data:
                node.next = prev.next
                node.prev = prev
                prev.next = node
                return
        node.prev = cur 
        cur.next = node 
        
      
                
        
           
                
               
                
                
                
        
        
        
        
        
        
        
            
        
            
        
        
            
        
        
            
            
           
            
            
            
        
        
        
        
        
dl = DLL()
dl.insert(10)
dl.insert(22)
dl.insert(30)
dl.insert(40)
dl.insert(50)
# ----------------------------------------
# dl.insert_at_front(20)
# dl.insert_at_end(20)
# dl.reverse()
# dl.delete_head()
# dl.delete_last_node()
# dl.insert_at_pos(3, 10)
dl.insert_in_sorted_list(90)
dl.print_list()

           
    