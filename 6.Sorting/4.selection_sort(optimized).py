# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:52:57 2020

@author: kirty
"""

arr = [10,5,8,20,2,18]
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_idx = i 
        
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr 
print(selection_sort(arr))
# time complexity - O(n2)
# aux space - O(1)
            
                
                