# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 18:39:52 2020

@author: kirty
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = Node(data)
        
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
            return 
            
        
        cur = self.head 
        while cur.next:
            if cur.next ==self.head:
                break
            cur = cur.next
            
            
        new_node.next = self.head
        cur.next = new_node
    def print_list(self):
        cur = self.head 
        
        while cur:
            print(cur.data,end=" ")
            if cur.next == self.head:
                break
            cur = cur.next 
    
    def insert_atFront_naive(self,data):
        # time complexity - O(n)
        node = Node(data)
        
        if self.head is None:
            self.head = node 
            node.next = self.head 
            return 
        
        cur = self.head 
        while cur:
            if cur.next == self.head:
                break
            cur = cur.next 
            
        cur.next = node
        node.next = self.head
        self.head = node
        
                
        
        
        
    
    def insert_at_front(self,data):
        # time complexity-O(1)
        node = Node(data)
        
        if self.head is None:
            self.head = node
            node.next = self.head 
            return 
        
            
        node.next = self.head.next
        self.head.next = node
        node.data,self.head.data = self.head.data,node.data
    
    def insert_at_end_naive(self,data):
        # time complexity -O(n)
        node = Node(data)
        
        cur = self.head
        
        if self.head is None:
            self.head = node
            return 
        while cur:
            if cur.next == self.head :
                break
            cur = cur.next 
        
        
        cur.next = node
        node.next = self.head 
    
    def insert_at_end_efficient(self,data):
        # time complexity - O(1)
        node = Node(data)
        
        if self.head is None:
            self.head = node
            return
        
        if self.head.next is None:
            self.head.next = node
            return 
        
        
        # insert node after head
        node.next = self.head.next
        
        # node pointer points to the elements after head 
        self.head.next = node
        
        # swtich the data of head and node
        self.head.data,node.data = node.data,self.head.data 
        
        # make node as head 
        self.head = node
    
    def delete_head_naive(self):
        # time complexity - O(1)
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return 
        
        self.head.data,self.head.next.data = self.head.next.data,self.head.data
        self.head.next = self.head.next.next 
    
    def del_kth_node(self,pos):
        # time complexity - O(n)
        count = 1
        cur = self.head
        
        if self.head is None:
            return
        
        if count == pos:
            self.head = None 
            return 
        prev = None
        while cur and count!=pos:
             
            count+=1
            prev = cur
            cur = cur.next
        if cur and prev:
            prev.next = cur.next 
            cur.next = None
    
    def __len__(self):
        count=1
        cur = self.head 
        while cur:
            
            if cur.next == self.head:
                break
            count+=1
            cur=cur.next
        
        return count 
    
    def Iscircular(self):
        cur = self.head 
        
        while cur:
            if cur.next == self.head :
                return True 
            cur = cur.next 
        return False 
   
    
        
    def insert_at_pos(self,pos,x):
        cur = self.head 
        node = Node(x)
        prev = None
        count = 1
        while cur and count!=pos:
            count+=1
            if cur.next is None:
                break
            prev = cur
            cur = cur.next 
        node.next = cur
        prev.next = node
        
        
            
         
        
        
         

    

    
    
        
               
          
         
        
        
        

cl = CLL()

cl.insert(10)
cl.insert(20)
cl.insert(30)
cl.insert(40)

# -----------------------------------------------------------
# cl.insert_at_front(10)
# cl.insert_atFront_naive(10)
# cl.insert_at_end(20)
# cl.insert_atFront_naive(20)
# cl.insert_at_end_naive(20)
# cl.insert_at_end_efficient(20)
# cl.delete_head_naive()
# cl.del_kth_node(.2)
# print(cl.__len__())
# print(cl.Iscircular())
# cl.insert_at_pos(2, 100)
cl.print_list()
    

