# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:16:58 2020

@author: Kirty
"""

def distinct(arr):
   s = set([])
   
   for i in arr:
       s.add(i)
       
   return len(s)
print(distinct([10,20,30,20,30,40]))
# time complexity = O(n)
# aux space - O(n)