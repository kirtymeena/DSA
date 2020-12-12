# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:37:45 2020

@author: Kirty
"""

arr= [0, -1, 2, -3, 1]
s=-2
def sum_(arr,s):
    d = set()
    for i in arr:
        if s-i not in d:
            d.add(i)
            
        else :
         return(s-i,i)
       
            
            
print(sum_(arr,s))