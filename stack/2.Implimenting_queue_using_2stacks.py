# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:39:04 2020

@author: Kirty
"""





class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 =[]
        
# implementing queue using stacks --- Enqueue opr costly
    # s1=[1,2] s2=[]
    def enQ(self,data):
        # O(N)
        while len(self.s1)!=0:
            self.s2.append(self.s1.pop())
        self.s1.append(data)
       
        
        while len(self.s2)!=0:
            self.s1.append(self.s2.pop())
    
    def DQ(self):
        # O(1)
        if self.s1!=0:
            print(self.s1.pop())
        
    def printQ(self):
        print(self.s1)
    
    # Dequeue opr costly
    
    def enqueue(self,data):
        # O(1)
        self.s1.append(data)
        
        
    def dequeue(self):
        # O(N)
        if len(self.s1)>0 and len(self.s2)==0:
            while len(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        
        else:
            return self.s2.pop()
       
        

s= Stack()
# s.enQ(1)
# s.enQ(2)
# s.enQ(3)

# s.DQ()
# s.DQ()
# s.DQ()

s.enqueue(1)
s.enqueue(2)
s.enqueue(3)

print(s.dequeue())
print(s.dequeue())
print(s.dequeue())

# s.printQ()


        
            
        
        