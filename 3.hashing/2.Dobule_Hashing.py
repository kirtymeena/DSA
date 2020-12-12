# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 17:14:11 2020

@author: Kirty
"""
class DoubleHashing:
    def __init__(self):
        self.capacity = 0
        
        self.table = []
        
        self.m=7
        
        for i in range(self.m):
            self.table.append(-1)
            
    def h1(self,key):
        return key%self.m
    
    def h2(self,key):
        return 6-(key%6)
    
    def insert(self,key):
        
            index = self.h1(key)
            if self.table[index]!=-1 or self.table[index]==-2:
                i=0
               
                while True:
                    hs = (self.h1(key)+i*self.h2(key))%self.m
                    if self.table[hs]==-1 or self.table[hs]==-2:
                        self.table[hs]=key
                        break
                    i+=1
                    
            else:
                self.table[index]=key
            self.capacity+=1
        
        
    def display(self):
       for i in range(len(self.table)):
           if self.table[i]!=-1:
               print(i,"-->",self.table[i])
           else:
               print(i)
    def search(self,key):
        if key in self.table:
            print(True)
        else:
            print(False)
    def delete(self,key):
        for i in range(len(self.table)):
            if self.table[i]==key:
                self.table[i]=-2
                
                
        
            
            
            
        
        
dh = DoubleHashing()
dh.insert(49)
dh.insert(63)
dh.insert(56)
dh.insert(52)
dh.insert(54)
dh.insert(48)

dh.delete(56)
dh.insert(56)
dh.display()
            
        
        
        
        
        
        
        
