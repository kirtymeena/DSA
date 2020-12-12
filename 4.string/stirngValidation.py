# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:24:19 2020

@author: Kirty
"""

s = "1+2+5=0"

add=0
for i in range(len(s)-1):
    if s[i] not in ['+',"-","="]:
        add+=int(s[i])
if add == int(s[len(s)-1]):
    print("Valid")
else:
    print("Invalid")
    
        
        