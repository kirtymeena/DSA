# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 12:23:58 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        cur_node = self.head 
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        while cur_node.next:
           cur_node = cur_node.next
           
        cur_node.next = new_node
    def printList(self):
       cur_node = self.head 
       
       while cur_node:
           print(cur_node.data,end = " ")
           cur_node = cur_node.next 
           
    def deleteNode(self,key):
        cur_node = self.head 
        prev = None
        
        if key==self.head.data:
            self.head = self.head.next 
            return 
        
        while cur_node.data!=key and cur_node:
            prev = cur_node
            cur_node = cur_node.next 
        prev.next = cur_node.next 
        cur_node = None
    def PosDelete(self,pos):
        position = 1
        cur = self.head 
        
        if self.head and position==pos:
            self.head = self.head.next 
        
        prev = None
        while cur  and position!=pos:
            position+=1
            prev = cur
            cur =cur.next
            
        if prev:
            prev.next = cur.next 
            cur = None
    def __len__(self):
        count = 1
        cur = self.head 
        
        while cur:
            count+=1
            cur = cur.next 
        return count
    
    def deleteMid(self):
        # time complexity - O(N)
        # space -O(1)
        cur = self.head 
        mid = 1
        prev = None
        while cur and mid!=self.__len__()//2:
            mid+=1
            prev = cur
            cur = cur.next
        prev.next = cur.next 
        cur = None
    def countParirs(self,X,h1,h2):
        # time complexity - O(N+M)
        # space complexity - O(N+M)
        s = set()
        cur1 = h1
        cur2 = h2
        while cur1:
            s.add(cur1.data)
            cur1 = cur1.next
        count = 0
        while cur2:
            if X-cur2.data in s:
                count+=1
            cur2 = cur2.next 
        return count
    def mergeSort(self,h):
        pass
    def getMiddle()
    def partition(self,h):
        mid = 1
        
        cur = h
        prev =None
        while cur and mid != self.__len__()//2:
            mid+=1
            prev = cur
            cur = cur.next 
        slow = prev 
        fast = cur
    
        
            
            
        
        
            
            
            
        
        
        
            
            
            
            
            
            
        
        
        
ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)

# ll.deleteNode(2)
# ll.PosDelete(1)
# ll.deleteMid()
# -------------------------------------------------------
# count pairs
# l1 = LinkedList()
# l2 = LinkedList()

# l1.push(1)
# l1.push(2)
# l1.push(3)
# l1.push(4)
# l1.push(5)
# l1.push(6)

# l2.push(11)
# l2.push(12)
# l2.push(13)
# print(ll.countParirs(15, l1.head, l2.head))
# ----------------------------------------------------------
ll.partition(ll.head)
ll.printList()
        
          
            
            
        
        