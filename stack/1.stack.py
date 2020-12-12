# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 08:00:06 2020

@author: Kirty
"""

class stack:
    def __init__(self):
        self.stk =[] 
        
        
       
        
    def push(self,data):
        # O(1)
        return self.stk.append(data)
    def pop(self):
        # O(1)
        return self.stk.pop()
    def top(self):
        if not self.isEmpty():
            return self.stk[-1]
        else:
            return False
    def __len__(self):
        return len(self.stk)
    def print_stack(self):
        print( self.stk)
    def isEmpty(self):
        if len(self.stk) ==0:
            return True
        else:
            return False
        
    def stock_span(self):
        prices = list(map(int,(input().split())))
        span=[]
        for i in range(len(prices)):
            if self.isEmpty() and i==0:
                self.push(i)
                span.append(1)
           
            elif prices[self.top()]>prices[i]:
                self.push(i)
                span.append(1)
            else:
                while prices[self.top()]<prices[i] and not self.isEmpty():
                    self.pop()
                if self.isEmpty():
                   span.append(i+1)
                   self.push(i)
                else:
                    span.append(i-self.top())
                    self.push(i)
        print(span)
    def sort_Stack(self):
        aux = []
        while(not self.isEmpty()):
            temp = self.top()
            self.pop()
            while len(aux)!=0 and aux[-1]>temp:
                self.push(aux[-1])
                aux.pop()
            aux.append(temp)
        return aux
        
            
    def paranthese_cheker(self,ss):
        for i in range(len(ss)):
            if ss[i]in ["(","{","["]:
                self.push(ss[i])
            
           
            if self.isEmpty():
                return False
            elif ss[i]==")":
                char=self.pop()
                if char!="(":
                    return False
            elif ss[i]=="]":
                char=self.pop()
                if char!="[":
                    return False
                
            elif ss[i]=="}":
                char=self.pop()
                if char!="{":
                    return False
               
        print(self.stk)
        if self.isEmpty():
            return "balanced"
        else:
            return "not balanced"
                
        
        
        
        
                       
            
               
               
               
            
        
            
            
            
            
        
                
            
   
        
        

s= stack()

# s.push(1)
# s.push(2)
# s.push(5)
# s.push(3)
# s.push(4)
# print(s.sort_Stack())
print(s.paranthese_cheker("{}"))
# s.stock_span()


# print(s.top())

# s.print_stack()


# print(s.isEmpty())