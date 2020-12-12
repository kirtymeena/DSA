# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:59:47 2020

@author: Kirty
"""
text = "geeksforgeeks"
pattern = "no"

def findPerm(text,pattern):
    t=0
    for i in range(len(text)):
        if t  == len(pattern):
            break
        
        if text[i]==pattern[t]:
            t+=1
        else:
            t=0
    if t<len(pattern):
        return "No"
    else:
        return 'Yes'
       
       
    
print(findPerm(text, pattern))
# O(n)
# sapce aux -O(1)