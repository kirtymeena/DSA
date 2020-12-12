# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 15:10:37 2020

@author: Kirty
"""
# complete it 



txt = "heyhello"
pat = "hell"

def getarr(pat):
    arr = [0]*len(pat)
    i=0
    j=1
    
    arr[0]=0
    while i<len(pat):
       if pat[i] == pat[j]:
            i += 1
            arr[j] = i
            j += 1

        # The first character didn't match:
       elif i == 0:
            arr[j] = 0
            j += 1

        # Mismatch after at least one matching character:
       else:
            i = arr[i - 1]
    return arr
print(getarr(pat))
            
            