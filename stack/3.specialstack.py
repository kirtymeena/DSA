# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 12:29:56 2020

@author: Kirty
"""

class SpecialStack:
    def __init__(self):
        self.stk =[]
        self.top = -1
        self.max = 5
    def isFull(self):
        
        if len(self.stk) == self.max:
            return True
        else:
            return False
    def push(self,data):
        # O(1)
        if self.isFull():
            return "Stack is full"
        else:
            self.top+=1
            self.stk.append(data)
    def isEmpty(self):
        # O(n)
        if self.stk ==[]:
            return True
        else:
            return False
    def pop(self):
        # O(1)
        if self.isEmpty():
            return "Stack is empty"
        else:
            self.top-=1
            return self.stk.pop()
    def __min__(self):
        # O(1)
        return min(self.stk)
ss = SpecialStack()
ss.push(1)
ss.push(2)
ss.push(3)
ss.push(4)
ss.push(5)


print(ss.__min__())
print(" ")

print(ss.pop())
print(ss.pop())
print(ss.pop())
print(ss.pop())
print(ss.pop())

print(" ")
print(ss.isEmpty())

print(ss.isFull())
        
        
            