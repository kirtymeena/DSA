# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:51:15 2020

@author: kirty
"""
# implementation using array
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
    
        
    def IsBalanced(self,exp):
        lis = []
        for i in exp:
            lis.append(i)
        # print(lis)
        
        for j in range(len(lis)):
            if lis[j] in ["[","{","("]:
                self.push(lis[j])
            
            else:
                
                
                if lis[j]==")":
                    if self.peek()=="(":
                        self.pop()
                    
                elif lis[j]=="]":
                    if self.peek()=="[":
                        self.pop()
                elif lis[j]=="}":
                    if self.peek()=="{":
                        self.pop()
        
       
        if len(self.stack)==0:
            return "Balanced"
        return "Not Balanced"
    
    def IsOperand(self,op):
        return op.isalpha()
        
    def precedence(self,opr):
        d = {"+":1,"-":1,"*":2,"/":2,"^":3}
        if opr in d:
           return d[opr]
      
       
    def IsGreater(self,i):
        try:
            a = self.precedence[i]
            b =self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
       
                
    
    def infix_to_postfix(self,exp):  # "A+(B*C-(D/E^F)*G)*H"
       
        
        
        for j in exp:
            
            if self.IsOperand(j):
                self.output.append(j)
                
            elif j=="(":
                self.push(j)
                
            elif j==")":
                
                while self.peek()!="(" and not self.IsEmpty():
                  if self.peek!="(":
                      self.output.append(self.pop())
                  
                if not self.IsEmpty() and self.peek()!="(":
                    return -1
                
                else:
                    self.pop()
                    
            else:
                while not self.IsEmpty() and self.IsGreater(j):
                    self.output.append(self.pop())
               
                self.push(j)
            
        while len(self.stack)!=0:
            self.output.append(self.pop())
        return "".join(self.output)
            
        
                        
                    
                    
                    
                        
            
            
                    
                
    
        

        
        
        
                        
                    
                
                
            
            
            
        
        
        
    

s = Stack()
exp="(a+b)*(c+d)"
# print(s.IsBalanced(exp))
# print(s.infix_to_postfix(exp))

# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# s.push(50)
# print(s.peek())













        

            
            
        
        