# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 11:53:23 2020

@author: Kirty
"""

votes =  [ "john","johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"]

def winner(votes):
    d = {}
    lis=[]
    for i in votes:
        d[i] = votes.count(i)
    for key in d:
       lis.append(d[key])
    print(lis)  
       
    
        
   
    
print(winner(votes))