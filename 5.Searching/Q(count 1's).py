# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:34:16 2020

@author: Kirty
"""

arr=[1,1,1,1,0,0,0,0]

def count_1(arr,low,high):
    if low<=high:
        mid = low+(high-low)//2
        if (arr[mid]==high or arr[mid+1]==0and (arr[mid]==1)):
            return mid + 1
        elif arr[mid]==1:
            return count_1(arr,mid+1,high)
        else:
            return count_1(arr,low,mid-1)
print(count_1(arr,0,len(arr)-1))
# time-O(log(n))
        