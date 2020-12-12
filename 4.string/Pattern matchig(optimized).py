# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 10:52:14 2020

@author: Kirty
"""

txt = "ABCDABCE"
pat = "ABCE"

def pattern_matching_optimized(txt,pat):
    N=len(txt)
    M=len(pat)
    i=0
    while i<=N-M+1:
        for j in range(M):
            if txt[i+j]!=pat[j]:
                break
            j+=1
       
        if j==M:
            print(i)
            i=i+j
        elif j==0:
            i=i+1
        else:
            i+=j
       
pattern_matching_optimized(txt, pat)
# time complexity - O(n)
#aux space  - O(1)

"""
problem is when pattern has repeatations
ex:   txt : ABABABBAB
      pat : ABAB      --- there is repeatation
      
"""
            
            
            