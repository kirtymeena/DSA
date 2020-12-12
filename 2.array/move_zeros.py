# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:24:29 2020

@author: Kirty
"""
arr=[8,5,0,10,0,20]

def move_zeros(arr):
    for i in arr:
        if i==0:
            arr.remove(i)
            arr.append(i)
            
    return arr 
print(move_zeros(arr))

# time complexity - O(n)
# auxiliary space - O(1)