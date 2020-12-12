# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 09:40:51 2020

@author: kirty
"""

a = [10,15,20,40]
b = [5,6,6,10,15]

def merge_sort(a,b):
    i=0
    j=0
    m= len(a)
    n = len(b)
    while i<m and j<n:
        
        
        if a[i]<=b[j]:
            print(a[i] ,end=" ")
            i+=1
        else:
            print(b[j],end=" ")
            j+=1
            
       
        
    while i<m:
        print(a[i],end=" ")
        i+=1
    while j<n:
        print(b[j],end=" ")
        j+=1
   
            
            
merge_sort(a, b)
# time Compexity - O(m+n)
# aux space - O(1)           
        
        
            
