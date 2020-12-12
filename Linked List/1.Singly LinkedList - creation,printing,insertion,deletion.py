# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:24:56 2020

@author: Kirty
"""



"""
todo questions:
     # deleting complete linked list
     # detecting loop
     #count the number of loops
     # remove dup from unsorted list
"""



# creating nodes
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
        
    # deletion by key--(data)
    def delete(self,key):
        cur_node = self.head
        prev = None
        
        if cur_node and  cur_node.data==key:
            self.head = cur_node.next
            cur_node = None
            return 
        
        while cur_node.data!=key:
            prev= cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return "Node does not exist"
        
        prev.next = cur_node.next
    
    def delete_at_position(self,pos):
        cur_node = self.head
        prev = None
        
        count = 1
        
        if cur_node and count==pos:
            self.head = cur_node.next
            cur_node = None
            return 
            
        while count!=pos and cur_node:
            count+=1
            prev = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return "node does not exist"
        prev.next = cur_node.next
    
    # itrative -- len of the list
    def List_len(self):
        cur_node = self.head
        count = 0
        
        if self.head is None:
            return count
        while cur_node:
            count+=1
            cur_node = cur_node.next
        return count
    
    
    # find the element
    def Find_ele(self,val):
        cur_node = self.head
        
        if cur_node is None:
            return 
        while cur_node and cur_node.data!=val:
            cur_node = cur_node.next
        
        # return cur_node.data
            
        if cur_node :
            return "Yes"
        else:
            return "No"
    
    def find_nth_node(self,index):
        cur_node = self.head
        count = 1
        
        if cur_node is None:
           return 
        while cur_node and count!=index:
           count+=1
           cur_node = cur_node.next 
        if cur_node:
            
            return cur_node.data 
        else:
            return False
         
   
    def reverse_list(self):
        cur_node = self.head
        prev= None
        while cur_node:
           next = cur_node.next 
           cur_node.next = prev 
           prev = cur_node 
           cur_node = next
        self.head = prev
    
    # find nth node from end of the list
    def end_nth_node(self,index):
        cur_node = self.head 
        prev = None
        count = 1
        
        if cur_node is None:
            return
        # reverseing the list
        while cur_node:
            next = cur_node.next 
            cur_node.next = prev
            prev  =cur_node
            cur_node = next
        self.head = prev
        
        while prev and count!=index:
           count+=1
           prev = prev.next 
        if prev:
          return prev.data
        else:
            return "Out of index"
    
    def middle_of_list(self):
        cur_node = self.head 
        count = 1
        index = 1
        node = self.head
        # len of list
        while cur_node:
            count+=1
            cur_node = cur_node.next 
        mid = count//2
        
        # finding mid element
        while node and index!=mid:
            index+=1
            node = node.next 
        return node.data 
    
    def count_int(self,key):
        cur_node = self.head 
        count = 0
       
        
        while cur_node and key:
            if cur_node.data == key:
                count+=1
            cur_node = cur_node.next 
        return count
    
    def palindrome(self):
        stack = []
        cur_node = self.head 
        
        while cur_node:
            stack.append(cur_node.data) 
               
            cur_node = cur_node.next
        node = self.head
        
        while node:
            i =stack.pop()
            if i == node.data:
                return True
            else:
                return False
            
            node = node.next 
            
    # removing duplicate from sorted list
    def remove_dup(self):
        cur_node = self.head
        
        if cur_node is None:
            return
        while cur_node:
            
            temp = cur_node.next
            if cur_node.data == cur_node.next.data:
                new = cur_node.next.next
                cur_node.next = None
                cur_node.next = new 

            cur_node = cur_node.next 
    def swap_nodes(self,key1,key2):
        
        
        cur1= self.head 
        prev1 = None
           
        if key1==key2:
             return
           
        while cur1 and cur1.data!= key1:
             prev1 = cur1
             cur1 = cur1.next 
           
        cur2 = self.head 
        prev2 = None
           
        while cur2 and cur2.data!=key2:
              prev2 = cur2
              cur2 = cur2.next 
           
        if not cur1 and not cur2:
             return
           
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2 
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        cur1.next,cur2.next = cur2.next,cur1.next 
        
        
    def paiwise_swap(self):
        node = self.head 
        prev=None
        
        while node :
            if node.next is None:
                break
            prev = node 
            node = node.next
            prev.data,node.data = node.data,prev.data
            node = node.next
           
            
    def move_last_to_front_element(self):
        cur_node = self.head 
        prev  = None
        
        while cur_node  :
            prev = cur_node 
            cur_node= cur_node.next 
        self.head.data, prev.data = prev.data, self.head.data 
    
    def prepend(self,data):
        new_node = Node(data)
        old_node = self.head
        
        if self.head is None:
            self.head = new_node
            new_node.next = old_node
        
        self.head = new_node 
        new_node.next = old_node
    
    def after_node_insertion(self,prev_node,data):
        new_node = Node(data)
        
        
        if not prev_node:
            print("Node is not in the list")
            return 
        else:
            new_node.next = prev_node.next
            prev_node.next = new_node 
            
    def inserting_at_end(self,data):
        cur_node = self.head
        last_node = None
        new_node = Node(data)
        
        if self.head is None:
            return
        
        while cur_node:
            last_node = cur_node
            cur_node = cur_node.next 
        last_node.next = new_node
        new_node.next = None
        
    # reversing the list using stack
    def reverse_LL(self):
        stack=[]
        cur_node =self.head 
        
        while cur_node:
            stack.append(cur_node.data)
            cur_node = cur_node.next 
        for i in range(len(stack)):
           print(stack.pop())
           
    # convert singly to circular list 
    def singly_to_circular(self):
        cur_node = self.head 
        
        while cur_node.next:
           
            cur_node = cur_node.next 
        cur_node.next = self.head
        
        node = self.head
        
        while node:
            print(node.data)
            if node.next == self.head:
                break 
            node= node.next
    
    # rotate a linked list
    def rotate(self,k):
        p=self.head 
        q= self.head
        count = 1
        
        if not k:
            return 
        
        while p.next and count<k:
            
            p = p.next 
            count+=1
            
        if p is None:
            return 
        
        while q.next :
            q = q.next 
            
        q.next = self.head 
        self.head = p.next
        p.next = None
    
    
   
    def addition(self):
          p = 1
          q = ll.head
          sum = self.reverse_list.LinkedList()
          carry = 0
          while p and q:
              
              if not q:
                 j = 0
              else:
                 j = q.data
              s = p+j+carry  
              if s>=10:
                  carry = 1
                  r = s%10
                  s.insert(r)
              else:
                  carry = 0
                  sum.insert(s)
              if q :
                  q = q.next 
          sum.printList()
    def reorder(self):
        cur_node = self.head
        node = self.head
        
        count=1
        while cur_node:
            count+=1
            cur_node = cur_node.next
        pos = 1
        while node and pos!=count//2:
            pos+=1
            node = node.next
        s = node
        q = node.next 
        
        s.next = None
        
        cur = q
        prev = None
        while cur:
          nxt = cur.next
          cur.next = prev
          prev = cur
          cur = nxt
        q = prev 
       
        
        
        
        
        
        curr = self.head 
       
        
        while curr and q:
         
            n = curr.next
            curr.next = q
            q = q.next
            s = curr.next
            s.next = n
            curr = n
    def even_odd(self,n):
        cur_node = self.head 
        even =" "
        odd =" "
        while cur_node:
            if int(cur_node.data)%2==0:
                even+=str(cur_node.data)+" "
            else:
                odd +=str(cur_node.data)+" "
            cur_node = cur_node.next 
        print(even)
        print(odd)
    
    def sort_0_1_2(self):
        cur = self.head 
        
        count = [0,0,0]
        while cur:
            count[cur.data]+=1
            cur = cur.next 
        i=0 
        ptr = self.head 
        
        while ptr:
            if count[i] ==0:
                i+=1
            else:
                ptr.data=i
                count[i]-=1
                ptr = ptr.next 
                
    def remove_dup_ele(self):
        curNode = self.head.next 
        prevNode = self.head 
        keys=set([prevNode.data])
        
        while curNode:
            data = curNode.data
            if data in keys:
                prevNode.next = curNode.next 
                curNode = curNode.next
            else:
                keys.add(data)
                prevNode = curNode
                curNode = curNode.next
                
        cur_node = self.head 
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next 
        
    def intersection_point(self,head1,head2 ):
        cur = self.head 
        sec = self.head 
        
        while cur and sec and cur!=sec:
            cur = cur.next 
            sec = sec.next 
            
            if cur==sec:
                return cur.data 
            if not cur:
                cur = head2 
            if not sec:
                sec = head1
   
        
       
        
        
                
        
        
        
                    
               
            
                
            
            
            
        
                
        
                
                
        
        
        
        
       
       
        
            
       

             
ll=LinkedList()

    
    
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll.evenOdd()
# ll.even_odd()
# ll.reorder()


# ll.sort_0_1_2()
# ll.remove_dup_ele()
ll.printList()







# ll.rotate(2)

# print(ll.singly_to_circular())

# print(ll.reverse_LL())

# ll.inserting_at_end("S")

# print(ll.after_node_insertion(ll.head.next.next,"L"))

# ll.prepend(1)

# ll.move_last_to_front_element()

# ll.paiwise_swap()

# ll.remove_dup()

# ll.swap_nodes(12,20)

# print(ll.palindrome())

# print(ll.count_int(1))

# print(ll.middle_of_list())

# print(ll.end_nth_node(6))

# ll.delete_at_position(4)

# ll.delete_LinkedList()

# print(ll.List_len())

# print(ll.Find_ele("H"))

# print(ll.find_nth_node(2))

# ll.reverse_list()

# print(ll.printList())

# l1 = LinkedList() 
# l2 = LinkedList()
        
        
# l1.insert(1)
# l1.insert(2)
# l1.insert(3)
# l1.insert(4)       
          
# l1.addition()