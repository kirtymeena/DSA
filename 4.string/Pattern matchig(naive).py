# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 09:53:02 2020

@author: Kirty
"""

txt="ABABAB"
pat = "ABA"
def pattern_matching_naive(txt,pat):
    N=len(txt)
    M=len(pat)
    for i in range(N-M+1):
        j=0
        while j<M:
            if txt[i+j]!=pat[j]:
                break
            j+=1
        if j==len(pat):
            print("index",i)
            
        
print(pattern_matching_naive(txt,pat))
                
# time complexity - O((N-M+1)*M)
# aux complexity - O(1)


"""
naive solution of pattern matching algorithm 
"""