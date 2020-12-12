# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:44:56 2020

@author: Kirty
"""
arr=[1,2,3,4]

def reverse(arr):
    j=len(arr)-1
    for i in range(len(arr)):
        if j<i:
            arr[i],arr[j] = arr[j],arr[i]
             
        j=j-1
    return arr 
print(reverse(arr))

# time complexity: O(N)
# aux space : O(1)
            
        
            