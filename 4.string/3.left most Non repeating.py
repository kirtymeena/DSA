# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 09:43:40 2020

@author: Kirty
"""

s = "aabbcc"

def NonRepeated(s):
    for c in s:
        if s.count(c)==1:
            return c
    return -1

            
    
    
    
print(NonRepeated(s))