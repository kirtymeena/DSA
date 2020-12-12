# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:43:53 2020

@author: Kirty
"""

arr = [10,5,8,20,2,18]

def selectionsort(arr):
    n = len(arr)
    temp = []
    for i in range(n):
        temp.append(min(arr))
        arr.remove(min(arr))
    arr = temp
    return arr
        
       
print(selectionsort(arr))
        
# time complexity = O(n )  
# aux space - O(n) 