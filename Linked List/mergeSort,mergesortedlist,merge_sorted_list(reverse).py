# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:03:47 2020

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
    def getMiddle(self,head):
       if(head == None):
           return head 
       
       slow = head 
       fast = head 
       
       while fast.next and fast.next.next :
           slow = slow.next 
           fast = fast.next.next 
       return slow 
    def partition(self,head):
       if head == None or head.next == None:
           return head 
       middle = self.getMiddle(head)
       nextToMiddle = middle.next
       
       middle.next = None
       L=self.partition(head)
       R= self.partition(nextToMiddle)
       
       lis = self.mergeSort(L,R)
       return lis
    def mergeSort(self,a,b):
       result = None
       
       if a == None:
           return b 
       if b ==None:
           return a
       if a.data<=b.data :
           result = a 
           result.next = self.mergeSort(a.next,b)
       else:
           result = b
           result.next =  self.mergeSort(a, b.next)
       return result
   
    def merge_reverse(self,a,b):
        result  = None
        while a and b:
            if a.data<b.data:
                newNode = a
                a = a.next 
                newNode.next = result 
                result = newNode
                
            else:
                newNode = b
                b = b.next 
                newNode.next = result 
                result = newNode 
        while b:
            newNode = b
            b= b.next 
            newNode.next =result 
            result = newNode 
        
        while a:
            newNode = a
            a = a.next
            newNode.next = result 
            result = newNode 
        while newNode:
            print(newNode.data)
            newNode = newNode.next 
            
    def zigzag(self):
        cur = self.head
        p = None
        q = None
        while cur.next:
            if cur.next is None:
                break
            q = cur.next 
            p = cur.next.next 
            
            q,p= p,q 
            cur = cur.next
           
            
            
            
   
def merge_2_ll(l1,l2):
     
       dummyNode = Node(0)
       tail = dummyNode
     
      
       while True:
           
           
           if l1 is None:
               tail.next=l2
               break
           if l2 is None:
              tail.next =l1
              break
           
           if l1.data<=l2.data:
               tail.next = l1 
               l1 = l1.next 
           else:
               tail.next = l2 
               l2 = l2.next 
           tail = tail.next
       return dummyNode

           

        
        
       
           
      
               
        
        
            
          
             
             
             
       
            
            
ll=LinkedList()

# l1 = LinkedList()
# l2 = LinkedList()

# l1.insert(2)
# l1.insert(8)
# l1.insert(16)

# l2.insert(1)
# l2.insert(3)
# l2.insert(4)
# l2.insert(7)
# l2.insert(9)

# merge_2_ll(l1.head, l2.head)
# l1.merge_reverse(l1.head, l2.head)
    
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5) 
ll.zigzag()
ll.printList()
# ll.partition(ll.head)  

 

   
        