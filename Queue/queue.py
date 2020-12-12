# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
class queue:
    def __init__(self):
        self.q=[]
        self.front = 0   #front+=-1
        self.rear = 0    #rear+=1
        
    def enq(self,data):
        
        self.q.append(data)
    def dq(self):
        
        print(self.q.pop(0))
q = queue()
q.enq(1)
q.enq(2)
q.enq(3)

q.dq()
q.dq()
q.dq()

    
    
