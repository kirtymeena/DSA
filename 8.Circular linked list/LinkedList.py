# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:19:21 2020

@author: kirty
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next = None 

class linkedList:
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
        print(None,end=" ")
        
        
    def rprint(self,head):
        # recursivly printing the list
        if head is None:
            return
        print(head.data)
        
        self.rprint(head.next)
        
        
    def prepend(self,data):
        # time complexity - O(1)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def find_ele(self,x):
        # time complexity - O(n)
        # aux sapce - o(1) 
        cur = self.head
        index = 0
        if self.head is None:
            return 
        
        if self.head.data == x:
            return index+1 
        while cur:
            
            if cur.data == x:
                return index
            
            index+=1
            
            cur = cur.next 
        return -1
    
    def del_head(self):
      # time complexity - O(1)
        
        if self.head is None:
            return 
    
        self.head = self.head.next 
        
    def last_node(self):
        # time complexity - O(n)
        
        cur = self.head 
        
        if self.head is None:
            return 
        if self.head.next is None:
           return None
       
        while cur.next.next:
             cur = cur.next
        
        cur.next = None
    
    def insert_at_pos(self,val,pos):
        # time complexity - O(n)
        cur = self.head 
        count = 1
        prev = None
        node = Node(val)
        if self.head is None:
            return
        if pos==1:
            node.next = self.head.next
            self.head = node
        
        while cur and count<=pos:
            count+=1
            prev = cur
            cur = cur.next 
           
            
        if cur is None:
            return None
        else:
            node.next = prev.next 
            prev.next = node 
    
    def sorted_insert(self,data):
        # time complexity - O(position) --the position at which we have to insert data
        node = Node(data)
        cur = self.head 
        prev = None
        
        if self.head is None:
            self.head = node
            return 
            
        if self.head.data>=node.data:
            node.next = self.head.next
            self.head = node
        
        while cur:
            prev = cur 
            cur = cur.next 
            if cur and cur.data>=node.data:
                break
        
        node.next = prev.next 
        prev.next = node
    
    def middle(self):
        # there are 2 traversal
        # time complexity - O(n) (middle_efficient is the  optimized code)
        size = 0
        cur= self.head 
        curr = self.head
        
        if self.head is None:
            return 
        
        while cur :
            size+=1
            cur = cur.next
        mid = size//2
        count=0
        while curr and count!=mid:
            count+=1
            curr = curr.next 
        print(curr.data)
        
    def middle_efficient(self):
        # time complexity - O(n)
        slow = self.head
        fast = self.head 
        
        if self.head is None:
            return 
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)
        
    def nth_node_from_end(self,key):
        # time complexity - O(n)
        
        cur = self.head 
        
        count = 0
        while cur:
           count+=1
           cur = cur.next 
        
        
        if key>count:
            return 
        
        curr = self.head 
        
        while curr.next and count!=key:
            count=count-1
            curr = curr.next 
        
        print(curr.data)
    
    def nth_node_from_end_efficient(self,key):
        # time complexity - O(n) 
        # without finding length of the list
        slow = self.head 
        fast = self.head 
        
        
        for i in range(key):
            if fast is None:
                return 
            fast=fast.next 
        
        
        while fast:
            slow = slow.next 
            fast = fast.next 
        print(slow.data)
        
    def remove_dup(self):
        # time complexity - O(n)
       cur = self.head
        
       while cur and cur.next:
            if cur.data == cur.next.data:
                cur.next = cur.next.next 
        
            else:
                cur = cur.next
    def sum_of_list(self):
        cur = self.head 
        s = 0
        while cur:
            s+=cur.data
            cur = cur.next 
        print(s)
        
    def max_min(self):
        cur = self.head
        
        
        min=self.head.data
        max = self.head.data
        while cur:
            # finding min
            if min>cur.data:
                min= cur.data
            # finding max
            if max<cur.data:
                max = cur.data
            cur = cur.next
        return max,min 
    
    
    def __len__(self):
        count = 0
        cur = self.head 
        while cur:
            count+=1
            cur = cur.next 
        return count
    
    def insert_at_middle(self,data):
        size = self.__len__()//2
        cur = self.head 
        count = 0
        node = Node(data)
        
        while cur and count!=size:
            count+=1
            cur = cur.next 
        node.next = cur.next 
        cur.next = node
    
    def del_at_pos(self,key):
        count = 1
        cur  = self.head 
        prev = None
        
        if count == key:
            self.head = self.head.next 
            return 
        while cur and count!=key:
            count+=1
            prev = cur
            cur = cur.next 
        prev.next = cur.next 
        
    def IsSorted(self):
        cur = self.head 
        
        
        while cur and cur.next:
           if cur.data<=cur.next.data:
               return False 
           cur = cur.next 
        return True
           
        
                
                
        
        
            
            
        
        
        
           
    
            
        
        
                
            
                
                
                
    
        
        
        
    
        
    
        
ll=linkedList()

ll.insert(90)
ll.insert(80)
ll.insert(70)
ll.insert(50)
ll.insert(50)
ll.insert(40)



# ------------------------------------
# ll.prepend(10)
# print(ll.find_ele(10))
# ll.del_head()
# print(ll.last_node())
# print(ll.insert_at_pos(100,1))
# ll.sorted_insert(56)
# ll.middle()
# ll.middle_efficient()
# ll.nth_node_from_end(1)
# ll.nth_node_from_end_efficient(3)
# ll.reverse_list()
# ll.remove_dup()
# ll.sum_of_list()
# print(ll.max_min())
# ll.insert_at_middle(3)
# ll.del_at_pos(5)
print(ll.IsSorted())
# -----------------------------------------
ll.print_list()
            