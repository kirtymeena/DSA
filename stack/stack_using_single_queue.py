# -*- coding: utf-8 -*-


# implemting stack using single queue

class queue:
    def __init__(self):
        self.q = []
        self.stack = []
    
    def push(self,data):
        self.q.insert(0,data) 
        
    def pop(self):
        if len(self.q):
            return self.q.pop()
        else:
            return
    def Getstack(self):
        while len(self.q):
            self.stack.append((self.pop()))
            
        while len(self.stack)!=0:
           print(self.stack.pop())
        
q = queue()
q.push(1)
q.push(2)
q.push(3)



q.Getstack()

        
