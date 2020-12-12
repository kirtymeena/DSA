# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:50:56 2020

@author: Kirty
"""

class Node:
    def __init__(self,data):
        self.data = data 
       
    
class Stack :
    def __init__(self):
        self.s1 = []
        self.s2 = []
        self.tail=None
        
        
    
    def push(self,data):
        self.s1.append(Node(data))
    
    def pop(self):
        return self.s1.pop().data
    
    def merge(self,stack):
       for i in range(len(self.s2)):
           self.s1.append(self.s2[i])
    def display(self):
        for i in range(len(self.s1)):
            print(self.s1[i].data)
    def merge(self,stack):
        pass
    
    
        
        


s1= Stack()
s2 = Stack() 

s1.push(1)
s1.push(2)
s2.push(3)
s2.push(4)
s1.merge(s2)
print(s1.display())