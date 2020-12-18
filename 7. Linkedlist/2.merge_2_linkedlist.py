# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 16:20:46 2020

@author: kirty
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,data):
        # time complexity - O(n)
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node 
            return 
            
        cur_node = self.head 
        while cur_node.next:
            cur_node = cur_node.next 
        cur_node.next = new_node
    
    def print_list(self):
        cur_node = self.head
        
        while cur_node:
            print(cur_node.data ,"-->", end=" ")
            cur_node = cur_node.next
        print(None,"\n")
    
    def merge_list(self,headA,headB):
        curA = headA
        curB = headB
        dummyNode = Node(0)
        tail  = dummyNode
        
        
        while True:
            if curA is None:
                tail.next = curB
                break
            if curB is None:
                tail.next = curA
                break
            if curA.data<=curB.data:
                tail.next = curA
                curA = curA.next 
            else:
                tail.next = curB 
                curB = curB.next 
            tail = tail.next 
        cur = dummyNode.next 
        while cur:
            print(cur.data,end="-->")
            cur = cur.next 
            
            
            
            
            
                    
        
ll1 = LinkedList()
ll2 = LinkedList()


ll1.insert(5)
ll1.insert(10)
ll1.insert(15)
ll1.insert(40)

ll2.insert(2)
ll2.insert(3)
ll2.insert(20)

print(ll1.merge_list(ll1.head,ll2.head))



