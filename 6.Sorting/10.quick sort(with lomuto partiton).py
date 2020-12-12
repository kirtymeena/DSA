# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 08:44:06 2020

@author: kirty
"""

# arr = [10,80,30,90,40,50,70]
arr=[10,50,100,200]

def quickSort(arr,l,h):
    if l<h:
        p = partition(arr,l,h)
        quickSort(arr,l,p-1)
        quickSort(arr,p+1,h)
    return arr

def partition(arr,l,h):
    pi=arr[h]
    i=l-1
    j=l
    
    
    while j<=h-1:
        if arr[j]<pi:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
        j+=1
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return i+1

print(quickSort(arr,0,len(arr)-1))

# worst case - O(n2)
# best and avg case - O(nlogn)
# aux space - O(1)

# lomuto and hoare partitioning does not provide stability
# naive partitioning provides stability