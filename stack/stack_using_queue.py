# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 13:56:32 2020

@author: Kirty
"""
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    # push operation is expensive
    
    def push(self,data):
        self.q2.put(data)
        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            
        self.q = self.q1
        self.q1 = self.q2
        self.q2 = self.q 
    
    def pop(self):
        if  self.q1.empty():
            return
        
        print(self.q1.get())
    def top(self):
        return self.q1.queue[0]
    
    
    # by making pop opeartion costly
    
s= Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
s.pop()
s.pop()
s.pop()


        
            
            
    
    
        