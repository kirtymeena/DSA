# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:19:01 2020

@author: Kirty
"""
n=int(input())
arr=list()
for arr in range(n):
    arr = input().split()
arr = [int(i) for i in arr]

def rotate(arr,k):
    for i in range(k):
        ele=arr.pop(0)
        arr.append(ele)
    return arr
print(rotate(arr,2))

# time complexity - O(n)
# aux space - O(1)
