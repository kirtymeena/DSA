# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:40:51 2020

@author: Kirty
"""
arr=[10,20,30,40,50]
def BinarySearch_recursive(arr,x,low,high):
    
    
    if low<=high:
    
        mid = low+(high-low)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return BinarySearch_recursive(arr, x, low, mid-1)
        else:
            return BinarySearch_recursive(arr, x, mid+1, high)
    else:
        return -1
        

print(BinarySearch_recursive(arr, 50, 0, len(arr)))
    
    
    