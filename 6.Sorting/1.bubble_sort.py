 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
arr = [2,10,8,7]
import time 


def bubble_sort(arr):
    n=len(arr)
    
    for i in range(n-1):
       j=i
       while j<n-1:
           if arr[j]>arr[j+1]:
               arr[j],arr[j+1] = arr[j+1],arr[j]
           j+=1 
    print(time.time())     
    return arr
            
       
print(bubble_sort(arr))
# time complexity - O(n^2) 
# aux space - O(1)
