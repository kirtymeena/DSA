# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 14:11:02 2020

@author: Kirty
"""

s1="listen"
s2 = "silent"
def Isanagram(s1,s2):
    
    if sorted(s1)==sorted(s2):
        return "anagram"
    else:
        return "Not an anagram"
                
   
print(Isanagram(s1,s2))

# time complexity = O(1)
# aux space = O(1)