# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:45:02 2020

@author: kirty
"""
arr = [10,5,30,15,7]
def mergeSort(arr):
   
   if len(arr)>1:
        m = len(arr)//2
        
        L = arr[:m]
        R = arr[m:]            
        
        mergeSort(L)
        mergeSort(R)
        
        i=0
        j=0
        k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                k+=1
                i+=1
            else:
                arr[k] = R[j]
                k+=1
                j+=1
        while i<len(L):
            arr[k]=L[i]
            k+=1
            i+=1
        while j<len(R):
            arr[k]=R[j]
            k+=1
            j+=1
   return arr
print(mergeSort(arr))
# time complexity- O(nlogn)
# aux space - O(n)
# stable - yes (in place sorting)

        
        
    