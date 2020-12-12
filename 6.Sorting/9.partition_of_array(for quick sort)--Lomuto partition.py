# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:25:06 2020

@author: kirty
"""

# arr = [70,60,40,80,30]
# arr = [30,40,20,50,80]
arr = [10,80,30,90,40,50,70]
l=0
h=len(arr)-1
def partition(arr,l,h):
    p = arr[h]
    i = l-1
    j=l
    
    while j<=h-1:
        if arr[j]<p:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return arr
print(partition(arr,l,h))
# time complexity - O(n)
# aux space - O(1)

# better than naive 
