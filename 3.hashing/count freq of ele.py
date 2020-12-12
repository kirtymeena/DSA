# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:42:35 2020

@author: Kirty
"""

def freq(arr):
    
    d = dict()
    for i in arr:
        d[i] = arr.count(i)
    print(d)

        
        
freq([10,12,10,15,20,12,12])
# time complexity = O(n)
# aux space = O(n)