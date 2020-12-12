# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 06:31:56 2020

@author: Kirty
"""

def queue(arr,k):
    stack =[]
    for i in range(k):
        stack.insert(0,(arr.pop(0)))
    for i in range(len(stack)):
        arr.insert(0,stack.pop())
    return arr
        
print(queue([1,2,3,4,5],3))
    
        