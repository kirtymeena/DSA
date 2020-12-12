# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:52:27 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.random = None


def __init__(self):
        self.head = None
        
def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
    
    
def printList(root):
        cur_node = root
        
       
        count = 1
        while cur_node:
             print(cur_node.data,cur_node.random.data)
             if cur_node.data<cur_node.random.data:
                 count+=1
             cur_node = cur_node.next
        print(count ) 
        
def clone(originalList):
        cur_node = originalList 
        
        prev = None
        
        while cur_node:
            prev = cur_node
            nxt = cur_node.next
            new_node = Node(prev.data)
            
            prev.next = new_node 
            new_node.next =  nxt 
            cur_node = nxt 
            
        count = 0    
        cur_node = originalList  
        while cur_node:
            cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next
        
        cur_node = originalList  
        dup_node = originalList.next
        while cur_node.next:
            temp = cur_node.next 
            cur_node.next = cur_node.next.next 
            cur_node = temp
        return dup_node
            
            
            

originalList  = Node(1) 
originalList.next = Node(2) 
originalList.next.next = Node(3) 
originalList.next.next.next = Node(4) 
originalList.next.next.next.next = Node(5) 


originalList.random = originalList.next.next
  
# 2's random points to 1 
originalList.next.random = originalList
  
# 3's random points to 5 
originalList.next.next.random = originalList.next.next.next.next
  
# 4's random points to 5 
originalList.next.next.next.random = originalList.next.next.next.next
  
# 5's random points to 2 
originalList.next.next.next.next.random =originalList.next
  
'''Print the original linked list'''
print('Original list:') 
printList(originalList) 
  
'''Create a duplicate linked list'''
cloned_list = clone(originalList) 
  
'''Print the duplicate linked list'''
print('\nCloned list:') 
printList(cloned_list) 
           
           
            
            