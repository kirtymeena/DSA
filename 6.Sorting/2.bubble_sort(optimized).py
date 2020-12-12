# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:45:53 2020

@author: Kirty
"""

arr = [2,10,8,7]
import time
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        swapped = False 
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
            
        if swapped == False:
            break
        
    print(time.time())
    return arr 
print(bubble_sort(arr))
#  time complexity - O(n)

                
            