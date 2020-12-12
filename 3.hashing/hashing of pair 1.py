# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:54:03 2020

@author: Kirty
"""

# Given an array of pairs, find all symmetric pairs in it
# hashing of pair 1

arr=[[11,20],[30,40],[5,10],[40,30],[10,5]]

d = {}

for i in range(len(arr)):
    first = arr[i][0] 
    sec = arr[i][1]
    if sec in d.keys() and d[sec]==first:
        print((sec,first))
    else:
        d[first]=sec


# time complexity - O(n)
# aux space = O(n)

            
    
