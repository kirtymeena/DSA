# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:46:42 2020

@author: Kirty
"""

s1 = "ABCD"
s2 = "AA"

def IsRotation(s1,s2):
   str = s1+s2
   t =0
   for i in range(len(str)):
       if t==len(s2):
           break
       if str[i]==s2[t]:
           t+=1
       else:
           t=0
   if t<len(s2):
       return "Yes"
   else:
       return "NO"

print(IsRotation(s1, s2))
# time complexity-O(N)
# aux space - O(1)