# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 18:12:25 2020

@author: kirty
"""

arr = [50,20,40,60,10,20]
def insertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key 
    return arr 
print(insertionSort(arr))
            
# time complexity = o(n2) - worst case 
# best case - O(n) - when arr is sorted 
