# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:44:15 2020

@author: kirty
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.output = []
        self.precedence = {"+":1,"-":1,"/":2,"*":2,"^":3}
        
        
    
    def IsEmpty(self):
        if self.stack ==[]:
            return True
        
    def push(self,data):
        self.stack.append(data)
        
    def pop(self):
        if not self.IsEmpty():
           return self.stack.pop()
        return "$"
     
    def IsFull(self):
        if len(self.stack)-1==self.capacity:
            print("Full")
            return True
    
    def peek(self):
        if self.IsEmpty():
            return "Empty"
        return self.stack[-1]
    
    def evalution_of_postfix(self,exp):
        # converting postfix to infex and then solving it 
        
        for i in exp:
            s=""
            if i.isnumeric():
                self.push(i)
            
            else:
                if i in ["+",'-','*','/','^']:
                   
                    
                
                
                
                
    
    
s = Stack()
# postfix exp is given 
exp="32*3+"