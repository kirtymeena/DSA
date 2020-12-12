# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 07:31:28 2020

@author: Kirty
"""
arr = [10,20,30,40,50,60]
def BinarySearch(arr,x):
    low=0
    high = len(arr)
    
    while low<high:
        
        mid=low+(high-1)//2
        
        if arr[mid]==x:
            
            return mid
        elif arr[mid]>x:
            high = mid-1
        else:
            low= mid+1
    
    return -1
    
print(BinarySearch(arr,60))

# time complexity - O(log(n))
# aux space complexity - O(1)

# array should be sorted 
            
            
        
    