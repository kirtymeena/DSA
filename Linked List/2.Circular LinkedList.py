# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 12:43:26 2020

@author: Kirty
"""

"""
TODO:
    prepend
    delete at pos
    remove using datakey
    check wether the list is circular

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLL:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        new_node = Node(data)
        
        
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            
        cur_node = self.head
        while cur_node.next!=self.head:
            cur_node = cur_node.next 
        cur_node.next = new_node
        new_node.next = self.head
            
    def printLL(self):
        cur_node = self.head
        if self.head is None:
            return
        
        while cur_node:
            print(cur_node.data)
            
            if cur_node.next == self.head:
                break
            cur_node = cur_node.next
           
             
    def prepend(self,data):
        new_node = Node(data)
        cur_node = self.head
        
       
        
        new_node.next = self.head 
        if self.head is None:
           new_node.next = new_node
        else:
            while cur_node.next!=self.head:
                cur_node = cur_node.next
        cur_node.next = new_node
        self.head = new_node
                
            
                
        
        
    
    def __len__(self):
        count = 0
        cur_node = self.head 
        while cur_node :
            count+=1
            if cur_node.next == self.head:
                break 
            cur_node = cur_node.next 
            
        return count
    
    def split_list(self):
       size =len(self)
       
       
       
       if size ==0:
           return None 
       if size ==1:
           return self.head 
       mid = size//2
       
       
       count= 0 
       cur_node = self.head
       prev = None
       
       while cur_node and count<mid:
           count+=1
           prev = cur_node 
           cur_node = cur_node.next 
       prev.next = self.head 
       
       split_clist = CircularLL()
     
       while cur_node.next!=self.head:
           split_clist.insert(cur_node.data)
           cur_node = cur_node.next
       split_clist.insert(cur_node.data)
       self.printLL() 
       print("\n")
       split_clist.printLL()
     
      
    def remove_node(self,val):       
       if self.head.data==val:
           cur_node = self.head
           while cur_node.next!=self.head:
               cur_node = cur_node.next
           cur_node.next = self.head.next 
           self.head = self.head.next
           
       node = self.head  
       prev = None
       while node and node.data!=val:
           prev = node
          
           if node.next==self.head:
               break
           node= node.next
       prev.next = node.next 
       node  = None
           
    
    def isCLL(self):
        cur_node = self.head
        while cur_node.next:
             cur_node = cur_node.next
             if cur_node.next == self.head:
                return True
            
        return False
    def swap_first_last_node(self):
        cur_node = self.head 
        prev = None
        while cur_node:
            prev = cur_node
            if cur_node.next == self.head:
                break
            cur_node = cur_node.next
        self.head.data , cur_node.data = cur_node.data , self.head.data
            
           
         
      
       
    
                    
               
       
      
        
       
            
            
        
            

cll = CircularLL()
cll.insert(2)
cll.insert(9)
cll.insert(1)
cll.insert(5)
cll.swap_first_last_node()
# cll.remove_node(1)
# cll.sort_list()
# cll.prepend(6)
# print(cll.split_list())
# cll.isCLL()
print(cll.printLL())        
        
            
            
        