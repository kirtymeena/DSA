# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:25:42 2020

@author: kirty
"""

arr =[3,8,6,12,10,7]

def partition(arr,p=5):
   i=0
   j=len(arr)-1
   temp=[]
  
   
   for i in range(len(arr)):
       if arr[i]<=arr[p]:
           temp.append(arr[i])
           i
   for j in range(len(arr)):
       if arr[j]>arr[p]:
           temp.append(arr[j])
           
   arr = temp
   del temp
           
    
   return arr
print(partition(arr,5))

# time complexity - O(n)
# aux space - O(n)
            
            
            
            
            
     