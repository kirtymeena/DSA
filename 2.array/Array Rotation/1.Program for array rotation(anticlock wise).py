# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:09:06 2020

@author: Kirty
"""

"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements
    
        arr = 1,2,3,4,5,6,7

Rotation of the above array by 2 will make array
        arr = 3,4,5,6,1,2

"""
arr=[1, 2, 3, 4, 5, 6, 7]

def Rotation(arr,d,n):
    temp=[]
    for i in range(d):
        temp.append(i)
   
    
    for j in range(len(temp)):
        ele = arr.pop(0)
        arr.append(ele)
    return arr
    
    
           
print(Rotation(arr,3,6))



"""
LOGIC:
    1. d ko sotre kiya temp me temp=[0,1]
    2. element pop karwaya from arr len(temp) bar 0th index ke 
              arr.pop(j) karne se 1 and 3 pop hote h ---- ie; 0th index ka element--1
                                                              1th index ka element kya h? --3
              to esliye 0 index ka karwaya h kyuki elements shift ho jate h automatically
    3. popped element ko append kar diya
    
    
    koi extra array me output nhi aaraha h esliye:
        space -- O(1)
        time complexity -- O(n)-- because time increses as input increses
        
              
    
"""
            
            
        
    