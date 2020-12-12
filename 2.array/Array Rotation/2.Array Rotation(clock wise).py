# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 16:48:26 2020

@author: Kirty
"""

"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements clockwise

arr = 1,2,3,4,5,6,7
output: 7,1,2,3,4,5,6
"""

arr = [1,2,3,4,5]
def ClockwiseRotate(arr,d,n):
    temp=[]
    for i in range(d):
        temp.append(i)
    
    for j in range(len(temp)):
        ele = arr.pop(-1)
        arr.insert(0,ele)
    return arr

print(ClockwiseRotate(arr,1,6))

# time complexity -- O(n) --- because time increses as input increses

        
    