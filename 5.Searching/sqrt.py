# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:00:07 2020

@author: Kirty
"""

def sqrt(x):
    start = 1
    end= x
    
    if x==0 or x==1:
        return x
    while start<end:
        mid = (start+end)//2
        
        if mid*mid == x:
            return mid 
        elif mid*mid<x:
            start = mid+1
            ans = mid
            
            
        else:
            end=mid-1
    return ans
print(sqrt(9))
            